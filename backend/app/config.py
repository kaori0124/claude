import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PEXELS_API_KEY = os.environ.get("PEXELS_API_KEY", "")
UPLOAD_DIR = BASE_DIR / "uploads"
AUDIO_DIR = UPLOAD_DIR / "audio"
IMAGE_DIR = UPLOAD_DIR / "images"
VIDEO_DIR = UPLOAD_DIR / "videos"
OUTPUT_DIR = UPLOAD_DIR / "output"

ALLOWED_AUDIO_EXTENSIONS = {".mp3", ".m4a"}
ALLOWED_IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".webp"}
ALLOWED_VIDEO_EXTENSIONS = {".mp4", ".mov", ".avi", ".webm"}

MAX_AUDIO_SIZE = 50 * 1024 * 1024  # 50MB
MAX_IMAGE_SIZE = 10 * 1024 * 1024  # 10MB
MAX_VIDEO_SIZE = 200 * 1024 * 1024  # 200MB
