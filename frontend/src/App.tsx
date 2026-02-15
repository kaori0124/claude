import React, { useCallback, useRef, useState } from "react";
import {
  api,
  FontStyle,
  LyricLine,
  UploadResponse,
} from "./api/client";
import AudioUploader from "./components/AudioUploader";
import BrightnessControl from "./components/BrightnessControl";
import FontSettings from "./components/FontSettings";
import LyricsEditor from "./components/LyricsEditor";
import MediaAssigner from "./components/MediaAssigner";
import RenderButton from "./components/RenderButton";

const DEFAULT_FONT: FontStyle = {
  family: "Noto Sans JP",
  size: 48,
  color: "#FFFFFF",
  highlight_color: "#FFD700",
  stroke_color: "#000000",
  stroke_width: 2,
};

export default function App() {
  const [audio, setAudio] = useState<UploadResponse | null>(null);
  const [lyrics, setLyrics] = useState<LyricLine[]>([]);
  const [font, setFont] = useState<FontStyle>(DEFAULT_FONT);
  const [brightness, setBrightness] = useState(0.5);
  const [rendering, setRendering] = useState(false);
  const [progress, setProgress] = useState(0);
  const [outputUrl, setOutputUrl] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const pollingRef = useRef<number | null>(null);

  const stopPolling = useCallback(() => {
    if (pollingRef.current !== null) {
      clearInterval(pollingRef.current);
      pollingRef.current = null;
    }
  }, []);

  const pollStatus = useCallback(
    (projectId: string) => {
      pollingRef.current = window.setInterval(async () => {
        try {
          const status = await api.getStatus(projectId);
          setProgress(status.progress);

          if (status.status === "done") {
            stopPolling();
            setRendering(false);
            setOutputUrl(status.output_url);
          } else if (status.status === "error") {
            stopPolling();
            setRendering(false);
            setError(status.error || "レンダリングに失敗しました");
          }
        } catch {
          stopPolling();
          setRendering(false);
          setError("ステータスの取得に失敗しました");
        }
      }, 1000);
    },
    [stopPolling]
  );

  const handleRender = async () => {
    if (!audio) return;

    setRendering(true);
    setProgress(0);
    setOutputUrl(null);
    setError(null);
    stopPolling();

    try {
      const result = await api.renderVideo({
        audio_id: audio.id,
        lyrics,
        font,
        background_brightness: brightness,
        resolution: [1920, 1080],
      });

      pollStatus(result.project_id);
    } catch (err) {
      setRendering(false);
      setError(
        err instanceof Error ? err.message : "レンダリングに失敗しました"
      );
    }
  };

  const canRender =
    audio !== null && lyrics.length > 0 && lyrics.some((l) => l.text.trim());

  return (
    <div>
      <h1
        style={{
          textAlign: "center",
          margin: "20px 0 32px",
          fontSize: 28,
          background: "linear-gradient(135deg, #6366f1, #a855f7)",
          WebkitBackgroundClip: "text",
          WebkitTextFillColor: "transparent",
        }}
      >
        カラオケ動画作成ツール
      </h1>

      <AudioUploader onUploaded={setAudio} />
      <LyricsEditor lyrics={lyrics} onChange={setLyrics} />
      <MediaAssigner lyrics={lyrics} onUpdate={setLyrics} />
      <FontSettings font={font} onChange={setFont} />
      <BrightnessControl value={brightness} onChange={setBrightness} />
      <RenderButton
        disabled={!canRender}
        rendering={rendering}
        progress={progress}
        outputUrl={outputUrl}
        error={error}
        onRender={handleRender}
      />
    </div>
  );
}
