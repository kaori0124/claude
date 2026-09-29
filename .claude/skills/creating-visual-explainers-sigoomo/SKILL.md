---
name: creating-visual-explainers-sigoomo
description: しごおもラボ（シリョサク）のサイトと同じトンマナで図解HTMLを生成し、ローカルにHTMLファイルとして保存する（surge.sh などへのデプロイは行わない）。Triggered by requests like "しごおもトンマナで図解して", "ラボのトンマナで図解して", "しごおもラボの見た目で図解して", or "sigoomoで図解して".
---

# Creating Visual Explainers (しごおもラボ)

任意のトピックについて、しごおもラボのコミュニティサイトと同じトンマナで図解HTMLを生成し、ローカルに保存する。**surge.sh などへの公開・デプロイは行わない**。品質基準は「入社したての新卒社会人が読んでも腹落ちする明快さ」だが、この基準は出力には表示しない。

このスキルは、しごおもラボのサイトの見た目に寄せた非公式のトンマナ版である。コミュニティ公式の配布物ではない。

## 構成

このスキルは2ファイルで動く。どちらも同じフォルダに置く。

    creating-visual-explainers-sigoomo/
    ├── SKILL.md         ← このファイル。末尾に図解テンプレート（額縁）を含む
    └── model-answer.md  ← 模範回答（品質基準・デザインパターンの実例）

- **図解テンプレート** — このファイル末尾の「図解テンプレート」節。Tailwind CSS CDN・Lucide Icons CDN・しごおも配色を含む「額縁」
- **`model-answer.md`** — 模範回答。テンプレートと同一の額縁を含む完全なHTMLファイル。デザインガイドラインの代わりになる

以降、`model-answer.md` はこのスキルフォルダ（冒頭に示される Base directory）からの相対パス、`output/` は作業中のプロジェクトからの相対パスを指す。

## トンマナ（しごおもラボ サイト準拠）

参照: [しごおもラボ](https://shiryosaku.co.jp/shiryosaku_labo)

コミュニティサイトの明るく親しみのある見た目に寄せる。硬いB2Bコーポレートの顔にはしない。色・フォント・見出しの型はテンプレートの `smo-*` トークンと模範回答から読み取る。

- **ページ地**: `#F8F8F9`（`bg-smo-bg`）。カードは白（`bg-smo-surface`）＋薄いグレー罫線（`border-smo-border`）
- **セクション帯**: `#EBF1F8`（`bg-smo-band`）。話題の切り替わりに薄い青グレーの帯を敷く
- **本文色**: `#333333`（`text-smo-text`）。補足は `#555555`（`text-smo-muted`）、出典は `text-smo-dim`
- **ブランド色は2色のグラデーション**: 青 `#2BA0E2`（`smo-accent`）→ ティール `#37AABA`（`smo-teal`）。`bg-gradient-to-r from-smo-accent to-smo-teal` が全体を貫く一番の特徴
- **見出しの色**: 濃紺 `#00314E`（`text-smo-navy`）。青 `#2BA0E2` は小さい文字に使うと薄いので、塗り・アイコン・ラベルに使う
- **区別に使う3色**: 青 `smo-accent` / ティール `smo-teal` / 濃紺 `smo-navy`。ステップや分類はこの3色で回す
- **日本語本文**: Noto Sans JP。英語の小ラベル（01・POINT など）だけ Raleway（`font-display`）
- **字間**: 本文は標準。`tracking-wide` は使わない。小さい英字ラベルだけ `tracking-[0.25em]`
- **見出しの型**: **中央揃え**。小さい番号（`font-display` の `01`）→ 日本語の見出し（`text-2xl`〜`text-3xl font-bold text-smo-navy`）→ グラデーションの短い下線（`w-16 h-1 rounded-full bg-gradient-to-r`）
- **スラッシュラベル**: サイト固有の表現。小見出しを `＼ 例えば… ／` のように全角スラッシュで挟んで中央に置く。罫線で挟むデザインより優先する
- **数字は主役にする**: 統計や件数は円形バッジ（`w-36 h-36 rounded-full` ＋ 2pxのブランド色ボーダー）に入れ、数字を `text-3xl font-bold` で見せる。単位と「以上」は小さく添える
- **角丸は大きめ**: カードは `rounded-xl`（12px）、大きなカードは `rounded-2xl`（16px）。ピルは `rounded-full`。角ばった見た目にしない
- **禁止する見た目**: グラデーション文字（`bg-clip-text`）、ネオン感のあるダークUI、絵文字、左揃えの巨大英字見出し

## ワークフロー

### Step 0: 前提確認

このスキルフォルダに `model-answer.md` が存在するか確認する。

存在しない場合、以下を伝えて終了:

> 模範回答ファイル（model-answer.md）が見つかりません。SKILL.md と同じフォルダに model-answer.md を置いてください。

### Step 1: 模範回答の読み込み

`model-answer.md` を読み、以下を把握する:

- 完成品の品質水準
- デザインパターン（色使い・余白・カード・フロー図などの視覚表現）
- Tailwind CSSクラスの使い方
- Lucide Iconsの使い方
- コンテンツの構成・情報量・説明の深さ

模範回答がデザインガイドラインの代わりになる。パーツ一覧やルールではなく、実物から読み取る。

### Step 2: テンプレートの確認

このファイル末尾の「図解テンプレート」節を読み、額縁の構造を把握する:

- `<!-- CONTENT_START -->` 〜 `<!-- CONTENT_END -->` のプレースホルダー位置
- `<!-- TITLE -->`, `<!-- DESCRIPTION -->` のプレースホルダー
- しごおも配色（`smo-*`）と `font-display`（Raleway）のTailwind設定
- 読み込み済みのCDN（Tailwind CSS・Lucide Icons・Google Fonts）

### Step 3: ウェブで情報収集

トピックについてウェブ検索を行い、正確かつ最新の情報を収集する。

検索は **2〜3回** に絞る。以下の観点でクエリを組み立てる:

1. **正確な定義**: トピックの公式な定義、公式ドキュメントの説明
2. **最新動向**: 直近の変更点、アップデート、現在のベストプラクティス
3. **具体例**: 実際の使われ方、初心者に伝わるたとえに使える事例

検索結果から以下を整理し、Step 4 の参考情報とする:

- トピックの正確な定義（検索結果を優先。AIの学習データだけに頼らない）
- 最近変わった点があれば、それを明記する
- たとえ話に使えそうな事例や数字
- **出典URL**: 図解に採用した情報のソースURLを控えておく（Step 4 でインライン出典に使う）

ユーザーが元ネタ（記事・動画のまとめなど）を渡してきた場合は、その内容を最優先で使う。検索は、固有名詞や出典の裏取りに絞ってよい。

### Step 4: コンテンツ生成

Step 3 で収集した情報をもとに、図解HTMLを生成する。検索結果で得た定義・事実・具体例を優先的に採用する。

模範回答のデザインを参考にしつつ、Tailwindの語彙で自由にレイアウトを組む。模範回答のパターンに合うものはそのまま使い、合わないものはTailwindクラスでその場で作る。テンプレートの定義済みパーツに縛られない。

### Step 5: ファイル作成

1. 作業中のプロジェクト直下に `output/` ディレクトリがなければ作成する
2. トピックに関連する短い英単語のスラッグを決める（例: `api-basics`, `git-rebase`）
3. 末尾の「図解テンプレート」節のHTMLをそのまま `output/{スラッグ}.html` として書き出す
4. 書き出したファイル内のプレースホルダーをすべて置換する:
   - `<!-- TITLE -->` → 図解のタイトル
   - `<!-- DESCRIPTION -->` → 内容を要約した1文
   - `<!-- CONTENT_START -->` 〜 `<!-- CONTENT_END -->` → Step 4で生成したコンテンツ
5. ファイルを保存する

### Step 6: 完了報告

生成したHTMLはローカルファイルとして保存するだけで終わりにする。Node.js の確認、`npx`、surge へのログインやデプロイは**一切実行しない**。

```
完成: 【図解のタイトル】

（図解の内容を1〜2文で要約）

ファイルの保存先:
output/{スラッグ}.html（ブラウザにドラッグ＆ドロップすると表示できます）

図解の主なポイント:
- （主要トピックを3〜5個）

PDFにしたいとき:
ブラウザで開き、右上の「PDF」ボタン（または Ctrl+P）から印刷・保存できます。
```

ユーザーから「公開して」「URLで共有したい」と依頼された場合は、このスキルは対応していないことを伝える。公開は各自のホスティング手段で行ってもらう。

## 守ること（禁止事項）

- **デプロイしない** — surge.sh を含め、生成物を外部に送信・公開しない。このスキルの成果物はローカルのHTMLファイルまで
- **React・shadcn/ui を使わない** — 静的な図解にJSフレームワークは不要。AIの出力を制限し、モデルによる品質差も限定的にしてしまう
- **絵文字を使わない** — OS依存で表示が変わる。アイコンはLucide Iconsを使う
- **インタラクティブ要素を入れない** — トグル、フェードイン、アニメーション、フォーム、クリックで開閉する要素は一切禁止
- **`<style>` タグを追加しない** — スタイリングはTailwind CSSクラスで行う。インラインの `style` 属性も避ける
- **`<script>` を追加しない** — テンプレートに含まれるもの以外のJavaScriptは禁止
- **外部リソースを追加しない** — テンプレートに含まれるCDN以外の外部読み込み（画像URL・フォント・追加CDN）は禁止
- **テンプレートの額縁構造を変更しない** — `<head>`・CDN読み込み・meta タグはそのまま維持する
- **グラデーションは「塗り」だけに使う** — `bg-gradient-to-r from-smo-accent to-smo-teal` は帯・ボタン・下線などの背景に使う。`bg-clip-text text-transparent` によるグラデーション文字はPDF出力で消えるので使わない
- **Tailwind標準の青・シアンでブランドを出さない** — `text-blue-500` や `from-cyan-600` ではなく、`smo-accent` / `smo-teal` / `smo-navy` を使う。ただしコードのシンタックスハイライトや、アプリ画面のモックアップなど「描写」に使う色はこの限りではない
- **しごおもラボのロゴ・写真・固有の文言を複製しない** — 色とレイアウトの雰囲気に寄せるだけにとどめ、公式の配布物に見える作りにはしない

## コンテンツ生成の指針

- **概論 → 各論** — いきなり詳細に入らない。全体像を見せてから個別の話に入る
- **専門用語は初出で必ず解説** — 「API（Application Programming Interface＝ソフトウェア同士がやり取りするための窓口）」のように、括弧書きで平易に説明する
- **たとえ話で身近な体験に結びつける** — レストランの注文、郵便配達、信号機など、技術を知らない人でもイメージできる例を使う
- **簡潔にまとめすぎない** — 理解に必要な情報量は削らない。腹落ちするまで丁寧に説明する
- **図を早く見せる** — 見出しから最初のビジュアルまでに、テキストは最大2段落（各2〜3行）。それ以上の説明が必要な場合は、図を先に見せてから図の後にテキストで補足する（図→説明の順）。テキストで述べたたとえ話も、テキストだけで済まさずミニビジュアル化を検討する
- **「見たことがあるもの」は説明するのではなく見せる** — 図解の中で読者がすでに体験しているもの（アプリの画面、ツールのUI、Webサイト）に言及するとき、テキストで「〜という画面が表示されます」と書く代わりに、その画面自体をTailwind CSSで再現して配置する
- **ビジュアルには2つの役割がある** — 「構造を示す図」と「体験を再現する図」の2種類。どちらか一方ではなく、両方を組み合わせて使う:
  - **構造パターン（仕組みを頭で理解する図）** — 知識の種類に応じて選ぶ:
    - **「Xとは何か」(定義)** → アナロジー図: 身近なたとえの登場人物を配置し、矢印で関係を示す。主役を中央に大きく
    - **「Xはどう動くか」(プロセス)** → ステップフロー: 番号つき横並び（モバイルは縦）。各ステップにアイコン＋一言。色は `smo-accent` / `smo-teal` / `smo-navy` で変える
    - **「XとYの違い」(比較)** → 左右対比: 2カラムで並べ、同じ観点を同じ行に揃える。✗/✓ や `smo-negative` / `smo-positive` で差を一目で伝える
    - **「Xの具体例」(事例)** → カードグリッド: 2列のカードにアイコン＋タイトル＋説明。カード内で「表の顔」と「裏の仕組み」を分けると深みが出る
    - **「Xのすごさ」(数値)** → **円形バッジ**: `w-36 h-36 rounded-full` にブランド色の2pxボーダー。数字を `text-3xl font-bold`、単位と「以上」を小さく添える。角カードより円を優先する
    - **「Xの構造・中身」(階層)** → 入れ子ブロック: 外側の大きなブロック内に構成要素を配置。ボーダーや背景色の濃淡で階層を表現
    - **「Xの誤解」(訂正)** → 誤解→正解カード: `smo-negative` のヘッダーに誤解、本文に `smo-positive` で正解
    - **「Xの変遷」(時系列)** → タイムライン: 左にボーダーライン、各時点に年号・ラベル・要約
  - **体験再現パターン（読者の「見たことある」記憶と結びつける図）** — 読者が実際に触れたことのある画面をTailwind CSSで再現する:
    - **チャットUI** — 吹き出し形式の対話画面。ユーザー吹き出し（右寄せ）＋相手の吹き出し（左寄せ）
    - **エディタUI / ターミナルUI / ブラウザUI** — タイトルバー（赤黄緑ボタン）＋中身
    - **アプリ画面** — 角丸カード内にアイコン＋数値＋ラベルでミニ画面を再現
    - 共通ルール: 中身はリアルすぎず要点が伝わるミニマルな内容にする。特定ブランドのロゴや名称は使わず汎用的な表現にする
- **冒頭にヒーロー＋一枚絵サマリー** — タイトルで「何の図解か」を伝えたあと、そのままトピックの核心を1枚の図で見せる。ヒーロー → 一言の答え → 図 → 各論が一本の流れになること:
  - **ヒーロー**: **中央揃え**。カテゴリを薄い青地のピル（`bg-smo-band rounded-full`）で小さく → 日本語タイトル（`text-3xl md:text-5xl font-bold text-smo-navy`）→ グラデーションの短い下線 → リード文。左揃えの巨大英字は使わない
  - **一言の答え**: 白い大きなカード（`rounded-2xl`）の冒頭に `＼ ひとことで言うと ／` を中央に置き、続けて核心の1文を `text-xl md:text-2xl font-bold text-smo-navy` で
  - **コア図解**: 一言の答えを図にしたもの。アイコン＋矢印＋ラベルで表現
  - **身近な接点**: 読者がすでに体験している具体例を、白地のピル（`rounded-full`）で2〜4個並べる
- **読者のレベルに言及しない** — 「初心者向け」「入門」「未経験者でもわかる」のように読者を特定のレベルにラベリングする表現をタイトル・見出し・本文に入れない
- **セクション見出しは中央揃えの3点セット** — 番号（`font-display` の `01`）→ 日本語見出し → グラデーションの短い下線。話題の切り替えを示したいときは `＼ ラベル ／` のスラッシュ見出しを併用する
- **インライン出典** — 検索結果から採用した事実・定義・数字のすぐ近くに、出典リンクをさりげなく添える。`text-xs text-smo-dim` で小さく薄く表示し、リンクテキストはURLそのままではなく「出典: ○○公式ドキュメント」のようにページ内容がわかる名前にする
- **日本語で** — 英語メインのトピックでも、図解は日本語で書く

## 図解テンプレート

Step 5 でこのHTMLをコピーし、`<!-- TITLE -->`・`<!-- DESCRIPTION -->`・`<!-- CONTENT_START -->` 〜 `<!-- CONTENT_END -->` を置換して `output/{スラッグ}.html` として保存する。`<head>` とCDN読み込みは変更しない。

```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
  <meta name="googlebot" content="noindex, nofollow">
  <meta property="og:title" content="<!-- TITLE -->">
  <meta property="og:description" content="<!-- DESCRIPTION -->">
  <meta property="og:type" content="article">
  <title><!-- TITLE --></title>
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='%232BA0E2'/><stop offset='1' stop-color='%2337AABA'/></linearGradient></defs><rect width='100' height='100' rx='22' fill='url(%23g)'/><rect x='24' y='30' width='52' height='34' rx='5' fill='%23FFFFFF'/><rect x='32' y='39' width='26' height='4' rx='2' fill='%232BA0E2'/><rect x='32' y='48' width='36' height='4' rx='2' fill='%2337AABA'/><rect x='42' y='68' width='16' height='4' rx='2' fill='%23FFFFFF'/></svg>">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&family=Raleway:wght@600;700&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      theme: {
        extend: {
          colors: {
            smo: {
              bg: '#F8F8F9',
              surface: '#FFFFFF',
              band: '#EBF1F8',
              soft: '#E2EBEF',
              border: '#E6E6E6',
              accent: '#2BA0E2',
              teal: '#37AABA',
              navy: '#00314E',
              text: '#333333',
              muted: '#555555',
              dim: '#767F88',
              positive: '#2E9E79',
              negative: '#E2685E',
              warning: '#E8A33D',
            }
          },
          fontFamily: {
            sans: ['"Noto Sans JP"', '"Hiragino Sans"', '"Hiragino Kaku Gothic ProN"', '"Yu Gothic UI"', '"Meiryo"', 'sans-serif'],
            display: ['"Raleway"', '"Noto Sans JP"', 'sans-serif'],
          }
        }
      }
    }
  </script>
  <style>
    @media print {
      .no-print { display: none !important; }
      body { border-top: none !important; }
      .rounded-xl { break-inside: avoid; }
      .md\:flex-row { flex-direction: row !important; }
      .md\:hidden { display: none !important; }
      .hidden.md\:block { display: block !important; }
      .md\:grid-cols-2 { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; }
      .sm\:grid-cols-3 { grid-template-columns: repeat(3, minmax(0, 1fr)) !important; }
      .md\:mb-20 { margin-bottom: 5rem !important; }
      .md\:py-16 { padding-top: 4rem !important; padding-bottom: 4rem !important; }
      .bg-clip-text.text-transparent {
        -webkit-background-clip: initial !important;
        background-clip: initial !important;
        color: #2BA0E2 !important;
        -webkit-text-fill-color: #2BA0E2 !important;
      }
    }
  </style>
</head>
<body class="bg-smo-bg text-smo-text antialiased leading-relaxed">
  <header class="bg-white border-b border-smo-border">
    <div class="no-print max-w-6xl mx-auto px-5 h-14 flex items-center justify-end">
      <button onclick="window.print()" class="flex items-center gap-1.5 text-xs text-smo-muted hover:text-smo-accent transition-colors cursor-pointer">
        <i data-lucide="download" class="w-3.5 h-3.5"></i>
        PDF
      </button>
    </div>
  </header>
  <div class="h-1.5 bg-gradient-to-r from-smo-accent to-smo-teal"></div>
  <main class="max-w-6xl mx-auto px-5 py-12 md:py-16">
<!-- CONTENT_START -->

<!-- CONTENT_END -->
  </main>
  <footer class="bg-gradient-to-r from-smo-accent to-smo-teal">
    <div class="max-w-6xl mx-auto px-5 py-10">
      <p class="text-xs text-white/70 text-center">図解ツールで作成</p>
    </div>
  </footer>
  <script src="https://unpkg.com/lucide@latest"></script>
  <script>lucide.createIcons();</script>
</body>
</html>
```
