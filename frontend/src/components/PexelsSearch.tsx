import React, { useState } from "react";
import { api, PexelsVideo } from "../api/client";

interface Props {
  defaultQuery?: string;
  onSelect: (video: PexelsVideo) => void;
  onClose: () => void;
}

export default function PexelsSearch({ defaultQuery = "", onSelect, onClose }: Props) {
  const [query, setQuery] = useState(defaultQuery);
  const [results, setResults] = useState<PexelsVideo[]>([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [searched, setSearched] = useState(false);

  const search = async () => {
    if (!query.trim()) return;
    setLoading(true);
    setError(null);
    try {
      const videos = await api.searchPexelsVideos(query.trim());
      setResults(videos);
      setSearched(true);
    } catch (e) {
      setError(e instanceof Error ? e.message : "検索に失敗しました");
    } finally {
      setLoading(false);
    }
  };

  const handleKeyDown = (e: React.KeyboardEvent) => {
    if (e.key === "Enter") search();
  };

  return (
    <div
      style={{
        position: "fixed",
        inset: 0,
        background: "rgba(0,0,0,0.75)",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        zIndex: 1000,
      }}
      onClick={(e) => e.target === e.currentTarget && onClose()}
    >
      <div
        style={{
          background: "#1a1a3e",
          border: "1px solid #2a2a5e",
          borderRadius: 12,
          padding: 24,
          width: "min(640px, 95vw)",
          maxHeight: "80vh",
          overflowY: "auto",
        }}
      >
        <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 16 }}>
          <h3 style={{ color: "#a5b4fc", margin: 0 }}>Pexels 動画を検索</h3>
          <button className="btn-secondary" onClick={onClose} style={{ padding: "4px 12px" }}>✕</button>
        </div>

        <div style={{ display: "flex", gap: 8, marginBottom: 16 }}>
          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            onKeyDown={handleKeyDown}
            placeholder="例: music stage, night city, nature..."
            style={{ flex: 1 }}
          />
          <button className="btn-primary" onClick={search} disabled={loading} style={{ whiteSpace: "nowrap" }}>
            {loading ? "検索中..." : "検索"}
          </button>
        </div>

        {error && (
          <p style={{ color: "#ef4444", fontSize: 13, marginBottom: 12 }}>{error}</p>
        )}

        {searched && results.length === 0 && !loading && (
          <p style={{ color: "#888", fontSize: 13 }}>結果が見つかりませんでした</p>
        )}

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(180px, 1fr))", gap: 10 }}>
          {results.map((v) => (
            <div
              key={v.id}
              onClick={() => onSelect(v)}
              style={{
                cursor: "pointer",
                borderRadius: 8,
                overflow: "hidden",
                border: "2px solid transparent",
                transition: "border-color 0.15s",
              }}
              onMouseEnter={(e) => (e.currentTarget.style.borderColor = "#6366f1")}
              onMouseLeave={(e) => (e.currentTarget.style.borderColor = "transparent")}
            >
              <img
                src={v.thumbnail}
                alt=""
                style={{ width: "100%", height: 100, objectFit: "cover", display: "block" }}
              />
              <div style={{ background: "#12122e", padding: "6px 8px", fontSize: 11, color: "#888" }}>
                {v.width}×{v.height} · {v.duration}秒
              </div>
            </div>
          ))}
        </div>

        <p style={{ fontSize: 11, color: "#555", marginTop: 16, textAlign: "right" }}>
          Powered by{" "}
          <a href="https://www.pexels.com" target="_blank" rel="noreferrer" style={{ color: "#6366f1" }}>
            Pexels
          </a>
        </p>
      </div>
    </div>
  );
}
