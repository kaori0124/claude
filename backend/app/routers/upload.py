import uuid
from pathlib import Path

from fastapi import APIRouter, HTTPException, UploadFile

from ..config import (
    ALLOWED_AUDIO_EXTENSIONS,
    ALLOWED_IMAGE_EXTENSIONS,
    ALLOWED_VIDEO_EXTENSIONS,
    AUDIO_DIR,
    IMAGE_DIR,
    MAX_AUDIO_SIZE,
    MAX_IMAGE_SIZE,
    MAX_VIDEO_SIZE,
    VIDEO_DIR,
)
from ..models import UploadResponse

router = APIRouter(prefix="/api/upload", tags=["upload"])


async def _save_file(
    file: UploadFile,
    dest_dir: Path,
    allowed_ext: set[str],
    max_size: int,
) -> UploadResponse:
    if not file.filename:
        raise HTTPException(400, "ファイル名がありません")

    ext = Path(file.filename).suffix.lower()
    if ext not in allowed_ext:
        raise HTTPException(
            400,
            f"非対応のファイル形式です: {ext}。対応形式: {', '.join(allowed_ext)}",
        )

    content = await file.read()
    if len(content) > max_size:
        raise HTTPException(
            400,
            f"ファイルサイズが上限({max_size // (1024*1024)}MB)を超えています",
        )

    file_id = uuid.uuid4().hex
    dest_path = dest_dir / f"{file_id}{ext}"
    dest_path.write_bytes(content)

    return UploadResponse(
        id=file_id,
        filename=file.filename,
        size=len(content),
    )


@router.post("/audio", response_model=UploadResponse)
async def upload_audio(file: UploadFile):
    """音源ファイル(MP3, M4A)をアップロード"""
    return await _save_file(file, AUDIO_DIR, ALLOWED_AUDIO_EXTENSIONS, MAX_AUDIO_SIZE)


@router.post("/image", response_model=UploadResponse)
async def upload_image(file: UploadFile):
    """背景画像をアップロード"""
    return await _save_file(
        file, IMAGE_DIR, ALLOWED_IMAGE_EXTENSIONS, MAX_IMAGE_SIZE
    )


@router.post("/video", response_model=UploadResponse)
async def upload_video(file: UploadFile):
    """背景動画をアップロード"""
    return await _save_file(
        file, VIDEO_DIR, ALLOWED_VIDEO_EXTENSIONS, MAX_VIDEO_SIZE
    )
