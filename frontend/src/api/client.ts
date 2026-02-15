export interface UploadResponse {
  id: string;
  filename: string;
  size: number;
}

export interface LyricLine {
  start_time: number;
  end_time: number;
  text: string;
  media_id: string | null;
}

export interface FontStyle {
  family: string;
  size: number;
  color: string;
  highlight_color: string;
  stroke_color: string;
  stroke_width: number;
}

export interface ProjectConfig {
  audio_id: string;
  lyrics: LyricLine[];
  font: FontStyle;
  background_brightness: number;
  resolution: [number, number];
}

export interface ProjectStatus {
  status: "pending" | "processing" | "done" | "error";
  progress: number;
  output_url: string | null;
  error: string | null;
}

const BASE = "/api";

async function uploadFile(
  endpoint: string,
  file: File
): Promise<UploadResponse> {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch(`${BASE}/upload/${endpoint}`, {
    method: "POST",
    body: form,
  });
  if (!res.ok) {
    const err = await res.json();
    throw new Error(err.detail || "アップロードに失敗しました");
  }
  return res.json();
}

export const api = {
  uploadAudio: (file: File) => uploadFile("audio", file),
  uploadImage: (file: File) => uploadFile("image", file),
  uploadVideo: (file: File) => uploadFile("video", file),

  async renderVideo(config: ProjectConfig): Promise<ProjectStatus> {
    const res = await fetch(`${BASE}/project/render`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(config),
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || "レンダリング開始に失敗しました");
    }
    return res.json();
  },

  async getStatus(projectId: string): Promise<ProjectStatus> {
    const res = await fetch(`${BASE}/project/status/${projectId}`);
    if (!res.ok) throw new Error("ステータス取得に失敗しました");
    return res.json();
  },
};
