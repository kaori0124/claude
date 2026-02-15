import React from "react";

interface Props {
  value: number;
  onChange: (value: number) => void;
}

export default function BrightnessControl({ value, onChange }: Props) {
  return (
    <div className="card">
      <h2>5. 背景の明るさ</h2>
      <div style={{ display: "flex", alignItems: "center", gap: 16 }}>
        <span style={{ fontSize: 13, minWidth: 24 }}>暗</span>
        <input
          type="range"
          min={0}
          max={1}
          step={0.05}
          value={value}
          onChange={(e) => onChange(parseFloat(e.target.value))}
          style={{ flex: 1, accentColor: "#6366f1" }}
        />
        <span style={{ fontSize: 13, minWidth: 24 }}>明</span>
        <span style={{ fontSize: 13, color: "#888", minWidth: 40 }}>
          {Math.round(value * 100)}%
        </span>
      </div>
    </div>
  );
}
