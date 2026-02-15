import React, { useState } from "react";
import { api, LyricLine, UploadResponse } from "../api/client";

interface Props {
  lyrics: LyricLine[];
  onUpdate: (lyrics: LyricLine[]) => void;
}

export default function MediaAssigner({ lyrics, onUpdate }: Props) {
  const [mediaMap, setMediaMap] = useState<Record<number, UploadResponse>>({});
  const [uploading, setUploading] = useState<number | null>(null);

  const handleUpload = async (
    index: number,
    file: File,
    type: "image" | "video"
  ) => {
    setUploading(index);
    try {
      const result =
        type === "image"
          ? await api.uploadImage(file)
          : await api.uploadVideo(file);

      setMediaMap((prev) => ({ ...prev, [index]: result }));

      const updated = [...lyrics];
      updated[index] = { ...updated[index], media_id: result.id };
      onUpdate(updated);
    } catch (err) {
      alert(err instanceof Error ? err.message : "アップロードに失敗しました");
    } finally {
      setUploading(null);
    }
  };

  if (lyrics.length === 0) return null;

  return (
    <div className="card">
      <h2>3. 背景メディア割り当て</h2>
      <p style={{ fontSize: 13, color: "#888", marginBottom: 12 }}>
        各歌詞セクションに背景画像または動画を割り当てられます（任意）
      </p>
      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        {lyrics.map((line, i) => (
          <div
            key={i}
            style={{
              display: "grid",
              gridTemplateColumns: "1fr 200px",
              gap: 8,
              alignItems: "center",
              padding: 8,
              background: "#12122e",
              borderRadius: 6,
            }}
          >
            <span style={{ fontSize: 13 }}>
              {line.text || `(行 ${i + 1})`}
            </span>
            <div style={{ display: "flex", alignItems: "center", gap: 4 }}>
              {mediaMap[i] ? (
                <span style={{ fontSize: 12, color: "#22c55e" }}>
                  {mediaMap[i].filename}
                </span>
              ) : (
                <input
                  type="file"
                  accept=".jpg,.jpeg,.png,.webp,.mp4,.mov,.avi,.webm"
                  onChange={(e) => {
                    const file = e.target.files?.[0];
                    if (!file) return;
                    const isVideo = /\.(mp4|mov|avi|webm)$/i.test(file.name);
                    handleUpload(i, file, isVideo ? "video" : "image");
                  }}
                  disabled={uploading === i}
                  style={{ fontSize: 12 }}
                />
              )}
              {uploading === i && (
                <span style={{ fontSize: 12 }}>...</span>
              )}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
