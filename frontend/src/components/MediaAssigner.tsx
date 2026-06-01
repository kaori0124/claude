import React, { useState } from "react";
import { api, LyricLine, PexelsVideo, UploadResponse } from "../api/client";
import PexelsSearch from "./PexelsSearch";

interface Props {
  lyrics: LyricLine[];
  onUpdate: (lyrics: LyricLine[]) => void;
}

interface MediaEntry {
  source: "upload" | "pexels";
  label: string;
  uploadId?: string;
  pexelsVideo?: PexelsVideo;
}

export default function MediaAssigner({ lyrics, onUpdate }: Props) {
  const [mediaMap, setMediaMap] = useState<Record<number, MediaEntry>>({});
  const [uploading, setUploading] = useState<number | null>(null);
  const [pexelsTarget, setPexelsTarget] = useState<number | null>(null);

  const handleUpload = async (index: number, file: File, type: "image" | "video") => {
    setUploading(index);
    try {
      const result: UploadResponse =
        type === "image"
          ? await api.uploadImage(file)
          : await api.uploadVideo(file);

      setMediaMap((prev) => ({
        ...prev,
        [index]: { source: "upload", label: result.filename, uploadId: result.id },
      }));

      const updated = [...lyrics];
      updated[index] = { ...updated[index], media_id: result.id };
      onUpdate(updated);
    } catch (err) {
      alert(err instanceof Error ? err.message : "アップロードに失敗しました");
    } finally {
      setUploading(null);
    }
  };

  const handlePexelsSelect = async (index: number, video: PexelsVideo) => {
    setPexelsTarget(null);
    setUploading(index);
    try {
      // Download the Pexels video via backend proxy to save it as a local file
      const res = await fetch(`/api/pexels/proxy?url=${encodeURIComponent(video.url)}`);
      if (!res.ok) throw new Error("動画の取得に失敗しました");
      const blob = await res.blob();
      const file = new File([blob], `pexels_${video.id}.mp4`, { type: "video/mp4" });
      const result = await api.uploadVideo(file);

      setMediaMap((prev) => ({
        ...prev,
        [index]: { source: "pexels", label: `Pexels #${video.id}`, pexelsVideo: video, uploadId: result.id },
      }));

      const updated = [...lyrics];
      updated[index] = { ...updated[index], media_id: result.id };
      onUpdate(updated);
    } catch (err) {
      alert(err instanceof Error ? err.message : "動画の設定に失敗しました");
    } finally {
      setUploading(null);
    }
  };

  const handleClear = (index: number) => {
    setMediaMap((prev) => {
      const next = { ...prev };
      delete next[index];
      return next;
    });
    const updated = [...lyrics];
    updated[index] = { ...updated[index], media_id: null };
    onUpdate(updated);
  };

  if (lyrics.length === 0) return null;

  // Build a default search query from all lyrics text
  const defaultQuery = lyrics
    .map((l) => l.text)
    .join(" ")
    .slice(0, 50);

  return (
    <div className="card">
      <h2>3. 背景メディア割り当て</h2>
      <p style={{ fontSize: 13, color: "#888", marginBottom: 12 }}>
        各歌詞セクションに背景画像・動画を設定できます。Pexelsから自動検索することも可能です。
      </p>
      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        {lyrics.map((line, i) => {
          const entry = mediaMap[i];
          return (
            <div
              key={i}
              style={{
                display: "grid",
                gridTemplateColumns: "1fr auto",
                gap: 8,
                alignItems: "center",
                padding: 10,
                background: "#12122e",
                borderRadius: 6,
              }}
            >
              <span style={{ fontSize: 13, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                {line.text || `(行 ${i + 1})`}
              </span>

              <div style={{ display: "flex", alignItems: "center", gap: 6, flexShrink: 0 }}>
                {entry ? (
                  <>
                    {entry.source === "pexels" && entry.pexelsVideo && (
                      <img
                        src={entry.pexelsVideo.thumbnail}
                        alt=""
                        style={{ width: 48, height: 28, objectFit: "cover", borderRadius: 3 }}
                      />
                    )}
                    <span style={{ fontSize: 12, color: "#22c55e", maxWidth: 120, overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap" }}>
                      {entry.label}
                    </span>
                    <button
                      className="btn-danger"
                      onClick={() => handleClear(i)}
                      style={{ padding: "3px 8px", fontSize: 11 }}
                    >
                      削除
                    </button>
                  </>
                ) : uploading === i ? (
                  <span style={{ fontSize: 12, color: "#888" }}>処理中...</span>
                ) : (
                  <>
                    <button
                      className="btn-primary"
                      onClick={() => setPexelsTarget(i)}
                      style={{ padding: "5px 10px", fontSize: 12, background: "#7c3aed" }}
                    >
                      🎬 Pexels
                    </button>
                    <label
                      style={{
                        fontSize: 12,
                        padding: "5px 10px",
                        background: "#374151",
                        borderRadius: 8,
                        cursor: "pointer",
                        color: "#e0e0e0",
                        fontWeight: 600,
                      }}
                    >
                      📁 アップロード
                      <input
                        type="file"
                        accept=".jpg,.jpeg,.png,.webp,.mp4,.mov,.avi,.webm"
                        onChange={(e) => {
                          const file = e.target.files?.[0];
                          if (!file) return;
                          const isVideo = /\.(mp4|mov|avi|webm)$/i.test(file.name);
                          handleUpload(i, file, isVideo ? "video" : "image");
                        }}
                        style={{ display: "none" }}
                      />
                    </label>
                  </>
                )}
              </div>
            </div>
          );
        })}
      </div>

      {pexelsTarget !== null && (
        <PexelsSearch
          defaultQuery={defaultQuery}
          onSelect={(video) => handlePexelsSelect(pexelsTarget, video)}
          onClose={() => setPexelsTarget(null)}
        />
      )}
    </div>
  );
}
