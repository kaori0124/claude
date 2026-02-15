from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .config import OUTPUT_DIR
from .routers import project, upload

app = FastAPI(title="カラオケ動画作成ツール", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router)
app.include_router(project.router)

app.mount("/output", StaticFiles(directory=str(OUTPUT_DIR)), name="output")


@app.get("/api/health")
async def health():
    return {"status": "ok"}
