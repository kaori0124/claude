import httpx
from fastapi import APIRouter, HTTPException, Query

from ..config import PEXELS_API_KEY

router = APIRouter(prefix="/api/pexels", tags=["pexels"])

PEXELS_VIDEO_URL = "https://api.pexels.com/videos/search"


@router.get("/search")
async def search_videos(q: str = Query(..., min_length=1), per_page: int = 6):
    """Pexels動画をキーワード検索して返す"""
    if not PEXELS_API_KEY:
        raise HTTPException(503, "Pexels APIキーが設定されていません")

    async with httpx.AsyncClient() as client:
        res = await client.get(
            PEXELS_VIDEO_URL,
            headers={"Authorization": PEXELS_API_KEY},
            params={"query": q, "per_page": per_page, "orientation": "landscape"},
            timeout=10,
        )

    if res.status_code != 200:
        raise HTTPException(502, f"Pexels APIエラー: {res.status_code}")

    data = res.json()
    videos = []
    for v in data.get("videos", []):
        # Pick the smallest HD file
        files = sorted(
            [f for f in v.get("video_files", []) if f.get("quality") in ("hd", "sd")],
            key=lambda f: f.get("width", 0),
        )
        if not files:
            continue
        file = files[0]
        videos.append({
            "id": v["id"],
            "thumbnail": v.get("image"),
            "duration": v.get("duration"),
            "url": file["link"],
            "width": file.get("width"),
            "height": file.get("height"),
        })

    return {"videos": videos}


@router.get("/proxy")
async def proxy_video(url: str = Query(...)):
    """Pexels動画URLをプロキシしてフロントに返す（CORS回避）"""
    from fastapi.responses import StreamingResponse

    allowed_host = "videos.pexels.com"
    from urllib.parse import urlparse

    parsed = urlparse(url)
    if parsed.hostname != allowed_host:
        raise HTTPException(400, "許可されていないURLです")

    async with httpx.AsyncClient(follow_redirects=True, timeout=60) as client:
        res = await client.get(url)

    if res.status_code != 200:
        raise HTTPException(502, "動画の取得に失敗しました")

    return StreamingResponse(
        iter([res.content]),
        media_type="video/mp4",
        headers={"Content-Disposition": "attachment; filename=pexels.mp4"},
    )
