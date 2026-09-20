"""献立プランナー CLI。献立生成・カレンダー登録・買い物リスト出力を統合する。"""

from __future__ import annotations

import argparse
import json
import random
import sys
from datetime import date
from pathlib import Path

import yaml

from .calendar_sync import clear_meal_events, sync_to_calendar
from .models import Dish, MealSlot, WeeklyPlan
from .planner import MONTH_TO_SEASON, generate_weekly_plan
from .shopping import format_shopping_list, generate_shopping_list

SEASON_JA = {
    "spring": "春", "summer": "夏", "autumn": "秋", "winter": "冬",
}


def load_config(config_path: str) -> dict:
    path = Path(config_path)
    if not path.exists():
        print(f"エラー: 設定ファイルが見つかりません: {config_path}")
        sys.exit(1)
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_dishes(config: dict) -> list[Dish]:
    return [Dish.from_dict(d) for d in config.get("dishes", [])]


def format_weekly_plan(plan: WeeklyPlan) -> str:
    lines = []
    if plan.meals:
        month = int(plan.meals[0].date.split("-")[1])
        season = MONTH_TO_SEASON.get(month, "spring")
        season_ja = SEASON_JA.get(season, "")
        lines.append("")
        lines.append("=" * 50)
        lines.append(f"  今週の献立（{season_ja}メニュー）")
        lines.append("=" * 50)

    for meal in plan.meals:
        lines.append("")
        lines.append(f"📅 {meal.date}（{meal.day_of_week}）")
        lines.append("-" * 40)
        if meal.main:
            url = f"  {meal.main.recipe_url}" if meal.main.recipe_url else ""
            lines.append(f"  🥘 メイン: {meal.main.name}{url}")
        if meal.salad:
            url = f"  {meal.salad.recipe_url}" if meal.salad.recipe_url else ""
            lines.append(f"  🥗 サラダ: {meal.salad.name}{url}")
        if meal.side:
            url = f"  {meal.side.recipe_url}" if meal.side.recipe_url else ""
            lines.append(f"  🍽  副菜:  {meal.side.name}{url}")
        time_label = f"約{meal.total_time}分" if meal.total_time > 0 else "調理なし"
        lines.append(f"  ⏱  調理: {time_label}")

    lines.append("")
    return "\n".join(lines)


def cmd_generate(args, config: dict):
    dishes = load_dishes(config)
    rules = config.get("rules", {})

    if args.seed is not None:
        random.seed(args.seed)

    start = None
    if args.start_date:
        start = date.fromisoformat(args.start_date)

    plan = generate_weekly_plan(dishes, rules, start)

    print(format_weekly_plan(plan))

    if args.shopping_list:
        shopping = generate_shopping_list(plan)
        print(format_shopping_list(shopping))

    if args.save:
        save_path = Path(args.save)
        data = {
            "meals": [
                {
                    "date": m.date,
                    "day_of_week": m.day_of_week,
                    "main": m.main.name if m.main else None,
                    "salad": m.salad.name if m.salad else None,
                    "side": m.side.name if m.side else None,
                    "total_time": m.total_time,
                }
                for m in plan.meals
            ]
        }
        save_path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
        )
        print(f"\n💾 献立を保存しました: {save_path}")

    return plan


def cmd_calendar(args, config: dict):
    dishes = load_dishes(config)
    rules = config.get("rules", {})
    cal_config = config.get("google_calendar", {})

    if args.seed is not None:
        random.seed(args.seed)

    start = None
    if args.start_date:
        start = date.fromisoformat(args.start_date)

    plan = generate_weekly_plan(dishes, rules, start)

    print(format_weekly_plan(plan))

    if args.clear:
        first = plan.meals[0].date
        last = plan.meals[-1].date
        deleted = clear_meal_events(first, last, cal_config)
        print(f"\n🗑  既存の献立イベントを {deleted} 件削除しました")

    if args.dry_run:
        print("\n📋 [ドライラン] 以下のイベントが登録されます:")
        events = sync_to_calendar(plan, cal_config, dry_run=True)
        for ev in events:
            print(f"  - {ev['start']['dateTime'][:10]}: {ev['summary']}")
    else:
        print("\n📅 Googleカレンダーに登録中...")
        results = sync_to_calendar(plan, cal_config)
        print(f"✅ {len(results)} 件のイベントを登録しました")

    shopping = generate_shopping_list(plan)
    print()
    print(format_shopping_list(shopping))


def cmd_shopping(args, config: dict):
    plan_path = Path(args.plan_file)
    if not plan_path.exists():
        print(f"エラー: 献立ファイルが見つかりません: {args.plan_file}")
        sys.exit(1)

    with open(plan_path, encoding="utf-8") as f:
        plan_data = json.load(f)

    dishes = load_dishes(config)
    dish_map = {d.name: d for d in dishes}

    plan = WeeklyPlan()
    for m in plan_data["meals"]:
        slot = MealSlot(date=m["date"], day_of_week=m["day_of_week"])
        if m.get("main") and m["main"] in dish_map:
            slot.main = dish_map[m["main"]]
        if m.get("salad") and m["salad"] in dish_map:
            slot.salad = dish_map[m["salad"]]
        if m.get("side") and m["side"] in dish_map:
            slot.side = dish_map[m["side"]]
        plan.meals.append(slot)

    shopping = generate_shopping_list(plan)
    print(format_shopping_list(shopping))


def main():
    parser = argparse.ArgumentParser(
        description="🍽 献立プランナー - 平日5日分の献立を自動生成",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
使い方の例:
  献立を生成:
    python -m meal_planner generate

  買い物リスト付きで生成:
    python -m meal_planner generate --shopping-list

  Googleカレンダーに登録（ドライラン）:
    python -m meal_planner calendar --dry-run

  Googleカレンダーに登録:
    python -m meal_planner calendar --clear
        """,
    )
    parser.add_argument(
        "-c", "--config",
        default="config.yaml",
        help="設定ファイルのパス (default: config.yaml)",
    )

    subparsers = parser.add_subparsers(dest="command", help="コマンド")

    gen = subparsers.add_parser("generate", help="平日5日分の献立を生成")
    gen.add_argument(
        "--start-date", help="開始日 (YYYY-MM-DD)。省略時は次の月曜日"
    )
    gen.add_argument(
        "--shopping-list", action="store_true", help="買い物リストも表示"
    )
    gen.add_argument("--save", help="献立をJSONファイルに保存")
    gen.add_argument("--seed", type=int, help="乱数シード（再現用）")

    cal = subparsers.add_parser("calendar", help="Googleカレンダーに献立を登録")
    cal.add_argument(
        "--start-date", help="開始日 (YYYY-MM-DD)。省略時は次の月曜日"
    )
    cal.add_argument(
        "--dry-run", action="store_true", help="実際には登録せず内容を確認"
    )
    cal.add_argument(
        "--clear", action="store_true", help="既存の献立イベントを削除してから登録"
    )
    cal.add_argument("--seed", type=int, help="乱数シード（再現用）")

    shop = subparsers.add_parser("shopping", help="保存済み献立から買い物リストを生成")
    shop.add_argument("plan_file", help="献立JSONファイルのパス")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    config = load_config(args.config)

    if args.command == "generate":
        cmd_generate(args, config)
    elif args.command == "calendar":
        cmd_calendar(args, config)
    elif args.command == "shopping":
        cmd_shopping(args, config)


if __name__ == "__main__":
    main()
