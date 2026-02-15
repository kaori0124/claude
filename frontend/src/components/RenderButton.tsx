import React from "react";

interface Props {
  disabled: boolean;
  rendering: boolean;
  progress: number;
  outputUrl: string | null;
  error: string | null;
  onRender: () => void;
}

export default function RenderButton({
  disabled,
  rendering,
  progress,
  outputUrl,
  error,
  onRender,
}: Props) {
  return (
    <div className="card">
      <h2>6. 動画出力</h2>
      <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
        <button
          className="btn-primary"
          onClick={onRender}
          disabled={disabled || rendering}
          style={{ padding: "12px 32px", fontSize: 16 }}
        >
          {rendering ? "レンダリング中..." : "1080p MP4を出力"}
        </button>

        {rendering && (
          <div style={{ flex: 1 }}>
            <div
              style={{
                background: "#2a2a5e",
                borderRadius: 4,
                height: 8,
                overflow: "hidden",
              }}
            >
              <div
                style={{
                  background: "#6366f1",
                  height: "100%",
                  width: `${progress * 100}%`,
                  transition: "width 0.3s",
                }}
              />
            </div>
            <span style={{ fontSize: 12, color: "#888" }}>
              {Math.round(progress * 100)}%
            </span>
          </div>
        )}
      </div>

      {outputUrl && (
        <div style={{ marginTop: 16 }}>
          <a
            href={outputUrl}
            download
            style={{
              color: "#22c55e",
              fontSize: 16,
              textDecoration: "underline",
            }}
          >
            動画をダウンロード
          </a>
        </div>
      )}

      {error && (
        <p style={{ marginTop: 8, color: "#ef4444" }}>{error}</p>
      )}
    </div>
  );
}
