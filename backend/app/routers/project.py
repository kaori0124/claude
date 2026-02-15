import uuid
from fastapi import APIRouter, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse

from ..config import OUTPUT_DIR
from ..models import ProjectConfig, ProjectStatus, RenderResponse
from ..services.video_generator import generate_video

router = APIRouter(prefix="/api/project", tags=["project"])

# In-memory project store (replace with DB for production)
projects: dict[str, dict] = {}


@router.post("/render", response_model=RenderResponse)
async def render_video(config: ProjectConfig, background_tasks: BackgroundTasks):
    """カラオケ動画のレンダリングを開始"""
    project_id = uuid.uuid4().hex
    projects[project_id] = {
        "status": "pending",
        "progress": 0.0,
        "output_url": None,
        "error": None,
    }

    background_tasks.add_task(_run_render, project_id, config)
    return RenderResponse(project_id=project_id, status="pending")


@router.get("/status/{project_id}", response_model=ProjectStatus)
async def get_status(project_id: str):
    """レンダリング状況を取得"""
    if project_id not in projects:
        raise HTTPException(404, "プロジェクトが見つかりません")
    p = projects[project_id]
    return ProjectStatus(**p)


@router.get("/download/{filename}")
async def download_file(filename: str):
    """生成された動画ファイルをダウンロード"""
    file_path = OUTPUT_DIR / filename
    if not file_path.exists():
        raise HTTPException(404, "ファイルが見つかりません")
    return FileResponse(
        path=str(file_path),
        media_type="video/mp4",
        filename=filename,
    )


async def _run_render(project_id: str, config: ProjectConfig):
    projects[project_id]["status"] = "processing"
    try:
        output_path = await generate_video(
            config, progress_callback=lambda p: _update_progress(project_id, p)
        )
        projects[project_id]["status"] = "done"
        projects[project_id]["progress"] = 1.0
        projects[project_id]["output_url"] = f"/api/project/download/{output_path.name}"
    except Exception as e:
        projects[project_id]["status"] = "error"
        projects[project_id]["error"] = str(e)


def _update_progress(project_id: str, progress: float):
    if project_id in projects:
        projects[project_id]["progress"] = progress
