import React from "react";
import { FontStyle } from "../api/client";

interface Props {
  font: FontStyle;
  onChange: (font: FontStyle) => void;
}

export default function FontSettings({ font, onChange }: Props) {
  const update = (field: keyof FontStyle, value: string | number) => {
    onChange({ ...font, [field]: value });
  };

  return (
    <div className="card">
      <h2>4. フォント設定</h2>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "1fr 1fr",
          gap: 16,
        }}
      >
        <label>
          <span style={{ display: "block", marginBottom: 4, fontSize: 13 }}>
            フォント
          </span>
          <select
            value={font.family}
            onChange={(e) => update("family", e.target.value)}
          >
            <option value="Noto Sans JP">Noto Sans JP</option>
            <option value="M PLUS Rounded 1c">M PLUS Rounded 1c</option>
            <option value="Kosugi Maru">Kosugi Maru</option>
            <option value="Arial">Arial</option>
          </select>
        </label>

        <label>
          <span style={{ display: "block", marginBottom: 4, fontSize: 13 }}>
            サイズ
          </span>
          <input
            type="number"
            value={font.size}
            min={12}
            max={120}
            onChange={(e) => update("size", parseInt(e.target.value) || 48)}
          />
        </label>

        <label>
          <span style={{ display: "block", marginBottom: 4, fontSize: 13 }}>
            文字色
          </span>
          <input
            type="color"
            value={font.color}
            onChange={(e) => update("color", e.target.value)}
            style={{ height: 40, padding: 2 }}
          />
        </label>

        <label>
          <span style={{ display: "block", marginBottom: 4, fontSize: 13 }}>
            ハイライト色
          </span>
          <input
            type="color"
            value={font.highlight_color}
            onChange={(e) => update("highlight_color", e.target.value)}
            style={{ height: 40, padding: 2 }}
          />
        </label>

        <label>
          <span style={{ display: "block", marginBottom: 4, fontSize: 13 }}>
            縁取り色
          </span>
          <input
            type="color"
            value={font.stroke_color}
            onChange={(e) => update("stroke_color", e.target.value)}
            style={{ height: 40, padding: 2 }}
          />
        </label>

        <label>
          <span style={{ display: "block", marginBottom: 4, fontSize: 13 }}>
            縁取り幅
          </span>
          <input
            type="number"
            value={font.stroke_width}
            min={0}
            max={10}
            onChange={(e) => update("stroke_width", parseInt(e.target.value) || 2)}
          />
        </label>
      </div>

      {/* Preview */}
      <div
        style={{
          marginTop: 16,
          padding: 20,
          background: "#000",
          borderRadius: 8,
          textAlign: "center",
        }}
      >
        <span
          style={{
            fontFamily: font.family,
            fontSize: Math.min(font.size, 48),
            color: font.highlight_color,
            WebkitTextStroke: `${font.stroke_width}px ${font.stroke_color}`,
            paintOrder: "stroke fill",
          }}
        >
          プレビュー歌詞テキスト
        </span>
      </div>
    </div>
  );
}
