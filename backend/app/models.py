from pydantic import BaseModel


class LyricLine(BaseModel):
    start_time: float  # seconds
    end_time: float  # seconds
    text: str
    media_id: str | None = None  # associated image/video file id


class FontStyle(BaseModel):
    family: str = "Noto Sans JP"
    size: int = 48
    color: str = "#FFFFFF"
    highlight_color: str = "#FFD700"
    stroke_color: str = "#000000"
    stroke_width: int = 2


class ProjectConfig(BaseModel):
    audio_id: str
    lyrics: list[LyricLine]
    font: FontStyle = FontStyle()
    background_brightness: float = 0.5  # 0.0 - 1.0
    resolution: tuple[int, int] = (1920, 1080)


class UploadResponse(BaseModel):
    id: str
    filename: str
    size: int


class RenderResponse(BaseModel):
    project_id: str
    status: str


class ProjectStatus(BaseModel):
    status: str  # "pending" | "processing" | "done" | "error"
    progress: float = 0.0
    output_url: str | None = None
    error: str | None = None
