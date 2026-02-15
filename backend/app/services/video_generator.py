import asyncio
import subprocess
from pathlib import Path
from typing import Callable

from ..config import AUDIO_DIR, IMAGE_DIR, OUTPUT_DIR, VIDEO_DIR
from ..models import ProjectConfig


def _find_file(directory: Path, file_id: str) -> Path | None:
    """IDからファイルを検索"""
    for f in directory.iterdir():
        if f.stem == file_id:
            return f
    return None


def _build_filter_complex(config: ProjectConfig) -> str:
    """FFmpeg filter_complexを構築"""
    filters = []
    brightness = config.background_brightness

    # Build lyrics overlay using drawtext filters
    for i, line in enumerate(config.lyrics):
        escaped_text = line.text.replace("'", "'\\''").replace(":", "\\:")
        font = config.font
        filters.append(
            f"drawtext=text='{escaped_text}'"
            f":fontsize={font.size}"
            f":fontcolor={font.highlight_color}"
            f":borderw={font.stroke_width}"
            f":bordercolor={font.stroke_color}"
            f":x=(w-text_w)/2"
            f":y=h-h/4"
            f":enable='between(t,{line.start_time},{line.end_time})'"
        )

    # Brightness adjustment
    brightness_val = brightness * 2 - 1  # Map 0..1 to -1..1
    base_filter = f"eq=brightness={brightness_val:.2f}"

    all_filters = ",".join([base_filter] + filters)
    return all_filters


async def generate_video(
    config: ProjectConfig,
    progress_callback: Callable[[float], None] | None = None,
) -> Path:
    """FFmpegを使用してカラオケ動画を生成"""

    # Find audio file
    audio_path = _find_file(AUDIO_DIR, config.audio_id)
    if not audio_path:
        raise FileNotFoundError(f"音源が見つかりません: {config.audio_id}")

    # Get audio duration
    probe_cmd = [
        "ffprobe", "-v", "quiet", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path),
    ]
    result = subprocess.run(probe_cmd, capture_output=True, text=True)
    duration = float(result.stdout.strip())

    width, height = config.resolution
    output_path = OUTPUT_DIR / f"{config.audio_id}_output.mp4"

    # Build background: use section media or black background
    bg_inputs = []
    has_section_media = any(line.media_id for line in config.lyrics)

    if has_section_media:
        # Create a concat list of media segments
        segments = _build_media_segments(config, duration)
        bg_inputs = segments
    else:
        bg_inputs = ["-f", "lavfi", "-i", f"color=c=black:s={width}x{height}:d={duration}"]

    filter_complex = _build_filter_complex(config)

    cmd = [
        "ffmpeg", "-y",
        *bg_inputs,
        "-i", str(audio_path),
        "-vf", filter_complex,
        "-c:v", "libx264",
        "-preset", "medium",
        "-crf", "23",
        "-c:a", "aac",
        "-b:a", "192k",
        "-s", f"{width}x{height}",
        "-shortest",
        str(output_path),
    ]

    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    _, stderr = await process.communicate()

    if process.returncode != 0:
        raise RuntimeError(f"FFmpegエラー: {stderr.decode()}")

    if progress_callback:
        progress_callback(1.0)

    return output_path


def _build_media_segments(config: ProjectConfig, duration: float) -> list[str]:
    """各セクションのメディアファイルをFFmpeg入力として構築"""
    # For sections with media, find the first one with media as a background
    for line in config.lyrics:
        if line.media_id:
            media_path = _find_file(IMAGE_DIR, line.media_id)
            if media_path:
                return ["-loop", "1", "-i", str(media_path), "-t", str(duration)]
            media_path = _find_file(VIDEO_DIR, line.media_id)
            if media_path:
                return ["-stream_loop", "-1", "-i", str(media_path)]

    width, height = config.resolution
    return ["-f", "lavfi", "-i", f"color=c=black:s={width}x{height}:d={duration}"]
