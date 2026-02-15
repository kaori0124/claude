import React, { useRef, useState } from "react";
import { api, UploadResponse } from "../api/client";

interface Props {
  onUploaded: (result: UploadResponse) => void;
}

export default function AudioUploader({ onUploaded }: Props) {
  const fileRef = useRef<HTMLInputElement>(null);
  const [uploading, setUploading] = useState(false);
  const [uploaded, setUploaded] = useState<UploadResponse | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setUploading(true);
    setError(null);
    try {
      const result = await api.uploadAudio(file);
      setUploaded(result);
      onUploaded(result);
    } catch (err) {
      setError(err instanceof Error ? err.message : "アップロードに失敗しました");
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="card">
      <h2>1. 音源アップロード</h2>
      <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
        <input
          ref={fileRef}
          type="file"
          accept=".mp3,.m4a"
          onChange={handleUpload}
          disabled={uploading}
          style={{ flex: 1 }}
        />
        {uploading && <span>アップロード中...</span>}
      </div>
      {uploaded && (
        <p style={{ marginTop: 8, color: "#22c55e" }}>
          {uploaded.filename} ({(uploaded.size / 1024 / 1024).toFixed(1)} MB)
        </p>
      )}
      {error && <p style={{ marginTop: 8, color: "#ef4444" }}>{error}</p>}
    </div>
  );
}
