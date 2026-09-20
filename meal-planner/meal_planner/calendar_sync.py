"""Googleカレンダーとの連携。OAuth2認証と週間献立のイベント登録を行う。"""

from __future__ import annotations

import os
from datetime import datetime, timedelta
from pathlib import Path

from .models import WeeklyPlan

SCOPES = ["https://www.googleapis.com/auth/calendar"]


def get_calendar_service(credentials_file: str, token_file: str):
    """OAuth2認証を行い、Googleカレンダーサービスを返す。

    初回実行時はブラウザが開き、Googleアカウントでの認証が必要です。
    認証済みトークンは token_file に保存され、次回以降は自動で再利用されます。
    """
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google_auth_oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build

    creds = None

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(credentials_file):
                raise FileNotFoundError(
                    f"Google Cloud の認証情報ファイルが見つかりません: {credentials_file}\n"
                    "セットアップ手順:\n"
                    "1. Google Cloud Console (https://console.cloud.google.com) にアクセス\n"
                    "2. プロジェクトを作成し、Google Calendar API を有効化\n"
                    "3. 認証情報 > OAuth 2.0 クライアントID を作成（デスクトップアプリ）\n"
                    "4. JSONをダウンロードして credentials.json として保存"
                )
            flow = InstalledAppFlow.from_client_secrets_file(
                credentials_file, SCOPES
            )
            creds = flow.run_local_server(port=0)

        Path(token_file).write_text(creds.to_json())

    return build("calendar", "v3", credentials=creds)


def sync_to_calendar(
    plan: WeeklyPlan,
    calendar_config: dict,
    dry_run: bool = False,
) -> list[dict]:
    """週間献立をGoogleカレンダーに登録する。

    dry_run=True の場合、実際には登録せず登録予定のイベント情報を返す。
    """
    calendar_id = calendar_config.get("calendar_id", "primary")
    dinner_time = calendar_config.get("dinner_time", "18:00")
    duration = calendar_config.get("event_duration_minutes", 60)
    color_id = str(calendar_config.get("event_color_id", "6"))
    credentials_file = calendar_config.get("credentials_file", "credentials.json")
    token_file = calendar_config.get("token_file", "token.json")

    events_to_create = []

    for meal in plan.meals:
        summary = f"🍽 {meal.summary()}"

        description_lines = [
            f"📅 {meal.date}（{meal.day_of_week}）の晩ごはん",
            "",
        ]
        if meal.main:
            description_lines.append(f"🥘 メイン: {meal.main.name}")
        if meal.salad:
            description_lines.append(f"🥗 サラダ: {meal.salad.name}")
        if meal.side:
            description_lines.append(f"🍽 副菜: {meal.side.name}")

        description_lines.append("")
        time_label = f"約{meal.total_time}分" if meal.total_time > 0 else "調理なし"
        description_lines.append(f"⏱ 調理時間目安: {time_label}")

        recipes = [
            d for d in meal.all_dishes if d.recipe_url
        ]
        if recipes:
            description_lines.append("")
            description_lines.append("📖 レシピ:")
            for d in recipes:
                description_lines.append(f"  {d.name}: {d.recipe_url}")

        if meal.all_ingredients:
            description_lines.append("")
            description_lines.append("📝 材料:")
            for ing in meal.all_ingredients:
                description_lines.append(f"  - {ing.name}: {ing.amount}")

        hour, minute = map(int, dinner_time.split(":"))
        start_dt = datetime.fromisoformat(meal.date).replace(
            hour=hour, minute=minute
        )
        end_dt = start_dt + timedelta(minutes=duration)

        event = {
            "summary": summary,
            "description": "\n".join(description_lines),
            "start": {
                "dateTime": start_dt.isoformat(),
                "timeZone": "Asia/Tokyo",
            },
            "end": {
                "dateTime": end_dt.isoformat(),
                "timeZone": "Asia/Tokyo",
            },
            "colorId": color_id,
        }
        events_to_create.append(event)

    if dry_run:
        return events_to_create

    service = get_calendar_service(credentials_file, token_file)

    created = []
    for event in events_to_create:
        result = service.events().insert(
            calendarId=calendar_id, body=event
        ).execute()
        created.append(result)

    return created


def clear_meal_events(
    start_date: str,
    end_date: str,
    calendar_config: dict,
) -> int:
    """指定期間の献立イベント（🍽 で始まるもの）を削除する。"""
    calendar_id = calendar_config.get("calendar_id", "primary")
    credentials_file = calendar_config.get("credentials_file", "credentials.json")
    token_file = calendar_config.get("token_file", "token.json")

    service = get_calendar_service(credentials_file, token_file)

    time_min = datetime.fromisoformat(start_date).isoformat() + "Z"
    time_max = (
        datetime.fromisoformat(end_date) + timedelta(days=1)
    ).isoformat() + "Z"

    events_result = (
        service.events()
        .list(
            calendarId=calendar_id,
            timeMin=time_min,
            timeMax=time_max,
            singleEvents=True,
            orderBy="startTime",
        )
        .execute()
    )

    deleted = 0
    for event in events_result.get("items", []):
        if event.get("summary", "").startswith("🍽"):
            service.events().delete(
                calendarId=calendar_id, eventId=event["id"]
            ).execute()
            deleted += 1

    return deleted
