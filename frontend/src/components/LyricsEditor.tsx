import React, { useState } from "react";
import { LyricLine } from "../api/client";

interface Props {
  lyrics: LyricLine[];
  onChange: (lyrics: LyricLine[]) => void;
}

function formatTime(seconds: number): string {
  const m = Math.floor(seconds / 60);
  const s = Math.floor(seconds % 60);
  const ms = Math.floor((seconds % 1) * 100);
  return `${m.toString().padStart(2, "0")}:${s.toString().padStart(2, "0")}.${ms.toString().padStart(2, "0")}`;
}

function parseTime(str: string): number {
  const parts = str.split(":");
  if (parts.length === 2) {
    const [min, secMs] = parts;
    const [sec, ms] = secMs.split(".");
    return (
      parseInt(min) * 60 +
      parseInt(sec) +
      (ms ? parseInt(ms.padEnd(2, "0")) / 100 : 0)
    );
  }
  return parseFloat(str) || 0;
}

export default function LyricsEditor({ lyrics, onChange }: Props) {
  const [bulkInput, setBulkInput] = useState("");
  const [showBulk, setShowBulk] = useState(false);

  const addLine = () => {
    const lastEnd = lyrics.length > 0 ? lyrics[lyrics.length - 1].end_time : 0;
    onChange([
      ...lyrics,
      { start_time: lastEnd, end_time: lastEnd + 5, text: "", media_id: null },
    ]);
  };

  const updateLine = (index: number, field: keyof LyricLine, value: string | number) => {
    const updated = [...lyrics];
    updated[index] = { ...updated[index], [field]: value };
    onChange(updated);
  };

  const removeLine = (index: number) => {
    onChange(lyrics.filter((_, i) => i !== index));
  };

  const parseBulk = () => {
    // Format: [MM:SS.ms] lyrics text
    const lines = bulkInput
      .split("\n")
      .filter((l) => l.trim())
      .map((line) => {
        const match = line.match(/\[(\d{2}:\d{2}\.\d{2})\]\s*(.*)/);
        if (match) {
          return { time: parseTime(match[1]), text: match[2] };
        }
        return null;
      })
      .filter((l): l is { time: number; text: string } => l !== null);

    const parsed: LyricLine[] = lines.map((line, i) => ({
      start_time: line.time,
      end_time: i < lines.length - 1 ? lines[i + 1].time : line.time + 5,
      text: line.text,
      media_id: null,
    }));

    onChange(parsed);
    setShowBulk(false);
    setBulkInput("");
  };

  return (
    <div className="card">
      <h2>2. 歌詞入力</h2>

      <div style={{ display: "flex", gap: 8, marginBottom: 16 }}>
        <button className="btn-primary" onClick={addLine}>
          行を追加
        </button>
        <button
          className="btn-secondary"
          onClick={() => setShowBulk(!showBulk)}
        >
          一括入力
        </button>
      </div>

      {showBulk && (
        <div style={{ marginBottom: 16 }}>
          <textarea
            rows={10}
            placeholder={"[00:05.00] 最初の歌詞\n[00:10.00] 次の歌詞\n[00:15.00] ..."}
            value={bulkInput}
            onChange={(e) => setBulkInput(e.target.value)}
            style={{ marginBottom: 8 }}
          />
          <button className="btn-primary" onClick={parseBulk}>
            解析して適用
          </button>
        </div>
      )}

      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        {lyrics.map((line, i) => (
          <div
            key={i}
            style={{
              display: "grid",
              gridTemplateColumns: "100px 100px 1fr 40px",
              gap: 8,
              alignItems: "center",
            }}
          >
            <input
              type="text"
              value={formatTime(line.start_time)}
              onChange={(e) =>
                updateLine(i, "start_time", parseTime(e.target.value))
              }
              placeholder="00:00.00"
              title="開始時間"
            />
            <input
              type="text"
              value={formatTime(line.end_time)}
              onChange={(e) =>
                updateLine(i, "end_time", parseTime(e.target.value))
              }
              placeholder="00:00.00"
              title="終了時間"
            />
            <input
              type="text"
              value={line.text}
              onChange={(e) => updateLine(i, "text", e.target.value)}
              placeholder="歌詞テキスト"
            />
            <button className="btn-danger" onClick={() => removeLine(i)}>
              ×
            </button>
          </div>
        ))}
      </div>

      {lyrics.length === 0 && (
        <p style={{ color: "#888", textAlign: "center", padding: 20 }}>
          「行を追加」または「一括入力」で歌詞を追加してください
        </p>
      )}
    </div>
  );
}
