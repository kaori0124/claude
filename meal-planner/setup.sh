#!/bin/bash
set -e

echo "🍽 献立プランナー セットアップ"
echo "================================"

cd "$(dirname "$0")"

if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 がインストールされていません"
    exit 1
fi

echo "📦 依存パッケージをインストール中..."
pip install -r requirements.txt

echo ""
echo "✅ セットアップ完了！"
echo ""
echo "使い方:"
echo "  cd meal-planner"
echo ""
echo "  # 1週間の献立を生成"
echo "  python -m meal_planner generate"
echo ""
echo "  # 買い物リスト付き"
echo "  python -m meal_planner generate --shopping-list"
echo ""
echo "  # Googleカレンダーに登録（ドライラン）"
echo "  python -m meal_planner calendar --dry-run"
echo ""
echo "  # Googleカレンダーに登録"
echo "  python -m meal_planner calendar --clear"
echo ""
echo "⚠️  Googleカレンダー連携には credentials.json が必要です。"
echo "   https://console.cloud.google.com でOAuth2クライアントIDを作成してください。"
