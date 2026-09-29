# 模範回答（しごおもラボ トンマナ）

図解の完成品の実例。品質水準・デザインパターン・情報量をここから読み取る。パーツ一覧やルールではなく、実物として読むこと。`<head>` は SKILL.md 末尾の図解テンプレートと同一に保つ。

```html
<!-- このファイルの<head>はreferences/base.htmlと同一に保つ。base.html変更時は必ずこちらも更新する -->
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="robots" content="noindex, nofollow, noarchive, nosnippet, noimageindex">
  <meta name="googlebot" content="noindex, nofollow">
  <meta property="og:title" content="APIの仕組み">
  <meta property="og:description" content="APIの仕組みを、身近な例とビジュアルでわかりやすく図解します。">
  <meta property="og:type" content="article">
  <title>APIの仕組み</title>
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

<!-- ============================================================ -->
<!--  HERO                                                        -->
<!-- ============================================================ -->
<div class="text-center mb-10 md:mb-14">
  <p class="inline-block text-xs font-bold text-smo-accent bg-smo-band rounded-full px-4 py-1.5 mb-5">テクノロジー</p>
  <h1 class="text-3xl md:text-5xl font-bold text-smo-navy leading-snug mb-5">APIの仕組み</h1>
  <div class="w-20 h-1 rounded-full bg-gradient-to-r from-smo-accent to-smo-teal mx-auto mb-6"></div>
  <p class="text-base text-smo-muted max-w-2xl mx-auto leading-relaxed">
    「APIって何？」と聞かれて、うまく答えられない。<br>
    ひとことで言うと ──
  </p>
</div>


<!-- ============================================================ -->
<!--  ONE-PAGE SUMMARY                                             -->
<!-- ============================================================ -->
<div class="bg-smo-surface border border-smo-border rounded-2xl p-6 md:p-10 mb-6">
  <div class="text-center mb-8 md:mb-10">
    <p class="text-sm font-bold text-smo-muted mb-3">＼ ひとことで言うと ／</p>
    <p class="text-xl md:text-2xl font-bold text-smo-navy mb-2">
      API = ソフトウェアの<span class="text-smo-accent">「注文窓口」</span>
    </p>
    <p class="text-sm text-smo-muted">
      中身を知らなくても、決まった形で頼めば結果が届く
    </p>
  </div>

  <!-- Core flow: App → API → Server -->
  <div class="flex flex-col md:flex-row items-center justify-center gap-2 md:gap-0 mb-8">
    <!-- App -->
    <div class="flex flex-col items-center w-36 p-3">
      <div class="w-14 h-14 rounded-xl bg-smo-accent/10 border border-smo-accent/20 flex items-center justify-center mb-2.5">
        <i data-lucide="smartphone" class="w-7 h-7 text-smo-navy"></i>
      </div>
      <div class="font-bold text-smo-text text-sm">あなたのアプリ</div>
      <div class="text-[11px] text-smo-navy/70 mt-0.5">「天気を教えて」</div>
    </div>

    <!-- Arrow 1: Request -->
    <div class="flex items-center justify-center md:w-16 py-1 md:py-0">
      <div class="flex flex-col items-center gap-0.5">
        <span class="text-[9px] font-medium text-smo-navy tracking-wider">リクエスト</span>
        <i data-lucide="arrow-right" class="w-5 h-5 text-smo-navy hidden md:block"></i>
        <i data-lucide="arrow-down" class="w-5 h-5 text-smo-navy md:hidden"></i>
      </div>
    </div>

    <!-- API (centerpiece — visually prominent) -->
    <div class="flex flex-col items-center w-40 p-4 bg-smo-accent/5 border-2 border-smo-accent/20 rounded-lg">
      <div class="w-16 h-16 rounded-lg bg-smo-accent/15 border-2 border-smo-accent/30 flex items-center justify-center mb-2.5">
        <i data-lucide="arrow-left-right" class="w-8 h-8 text-smo-accent"></i>
      </div>
      <div class="font-bold text-smo-accent text-base">API</div>
      <div class="text-[11px] text-smo-muted mt-0.5 mb-2">注文を届け、結果を返す</div>
      <div class="text-[10px] text-smo-muted bg-white rounded-lg px-2.5 py-1 border border-smo-border/50">レストランのウェイター役</div>
    </div>

    <!-- Arrow 2: Forward to server -->
    <div class="flex items-center justify-center md:w-16 py-1 md:py-0">
      <div class="flex flex-col items-center gap-0.5">
        <span class="text-[9px] font-medium text-smo-navy tracking-wider">依頼</span>
        <i data-lucide="arrow-right" class="w-5 h-5 text-smo-navy hidden md:block"></i>
        <i data-lucide="arrow-down" class="w-5 h-5 text-smo-navy md:hidden"></i>
      </div>
    </div>

    <!-- Server -->
    <div class="flex flex-col items-center w-36 p-3">
      <div class="w-14 h-14 rounded-xl bg-smo-teal/15 border border-smo-teal/30 flex items-center justify-center mb-2.5">
        <i data-lucide="server" class="w-7 h-7 text-smo-positive"></i>
      </div>
      <div class="font-bold text-smo-text text-sm">サービス</div>
      <div class="text-[11px] text-smo-positive/70 mt-0.5">処理して結果を返す</div>
    </div>
  </div>

  <!-- Return flow -->
  <div class="flex justify-center mb-8">
    <div class="flex items-center gap-2 text-xs text-smo-positive bg-smo-teal/10 border border-smo-teal/25 rounded-full px-4 py-1.5">
      <i data-lucide="corner-down-left" class="w-3.5 h-3.5"></i>
      結果（レスポンス）があなたのアプリに届く
    </div>
  </div>

  <!-- スラッシュラベル（しごおもラボ固有の見出し表現） -->
  <p class="text-center text-sm font-bold text-smo-muted mb-5">＼ あなたも毎日使っている ／</p>

  <!-- Everyday examples as pills -->
  <div class="flex flex-wrap justify-center gap-2 mb-8">
    <div class="flex items-center gap-1.5 bg-white border border-smo-border rounded-full px-3.5 py-1.5 text-xs text-smo-text">
      <i data-lucide="cloud" class="w-3.5 h-3.5 text-smo-accent"></i>
      天気予報
    </div>
    <div class="flex items-center gap-1.5 bg-white border border-smo-border rounded-full px-3.5 py-1.5 text-xs text-smo-text">
      <i data-lucide="log-in" class="w-3.5 h-3.5 text-smo-accent"></i>
      Googleログイン
    </div>
    <div class="flex items-center gap-1.5 bg-white border border-smo-border rounded-full px-3.5 py-1.5 text-xs text-smo-text">
      <i data-lucide="credit-card" class="w-3.5 h-3.5 text-smo-teal"></i>
      オンライン決済
    </div>
    <div class="flex items-center gap-1.5 bg-white border border-smo-border rounded-full px-3.5 py-1.5 text-xs text-smo-text">
      <i data-lucide="map-pin" class="w-3.5 h-3.5 text-smo-negative"></i>
      地図・ナビ
    </div>
  </div>

</div>

<p class="text-center text-smo-muted mb-16 md:mb-20">
  ここから先で、この仕組みをひとつずつ丁寧に解説していきます。
</p>


<!-- ============================================================ -->
<!--  SECTION 1: そもそもAPIって何？                                -->
<!-- ============================================================ -->
<section class="mb-16 md:mb-20">
  <div class="text-center mb-10">
    <p class="font-display text-sm font-bold text-smo-accent tracking-[0.25em] mb-2">01</p>
    <h2 class="text-2xl md:text-3xl font-bold text-smo-navy leading-snug mb-4">そもそもAPIって何？</h2>
    <div class="w-16 h-1 rounded-full bg-gradient-to-r from-smo-accent to-smo-teal mx-auto"></div>
  </div>

  <p class="mb-6 leading-relaxed">
    API（エーピーアイ）は <strong class="text-smo-text">Application Programming Interface</strong>（アプリケーション・プログラミング・インターフェース）の略称です。正式名称を聞いても「何のこと？」と思いますよね。
  </p>

  <p class="mb-6 leading-relaxed">
    まずは日常のたとえで考えてみましょう。レストランに行った場面を想像してください。
  </p>

  <p class="mb-8 leading-relaxed">
    あなた（お客さん）は、厨房に直接入って料理を作ることはできません。厨房のルールも、調理器具の使い方も知りません。でも、<strong class="text-smo-text">ウェイターに「パスタをください」と注文すれば、厨房で作られた料理があなたのテーブルに届きます。</strong>厨房の中で何が起きているかを知る必要はありません。
  </p>

  <!-- レストラン比喩フロー図 -->
  <div class="bg-smo-surface border border-smo-border rounded-xl p-6 md:p-8 mb-8">
    <h3 class="text-lg font-bold text-smo-text text-center mb-8">レストランで考えるAPIの役割</h3>

    <div class="flex flex-col md:flex-row items-center justify-center gap-4 md:gap-0">
      <!-- あなた（お客さん） -->
      <div class="w-44 bg-smo-accent/10 border border-smo-accent/20 rounded-xl p-5 text-center">
        <div class="w-12 h-12 rounded-full bg-smo-accent/20 flex items-center justify-center mx-auto mb-3">
          <i data-lucide="user" class="w-6 h-6 text-smo-navy"></i>
        </div>
        <div class="font-bold text-smo-navy mb-1">あなた</div>
        <div class="text-xs text-smo-navy/70">お客さん</div>
        <div class="text-xs text-smo-muted mt-3 bg-smo-bg rounded-lg px-3 py-1.5">「パスタください」</div>
      </div>

      <!-- 矢印 1 -->
      <div class="flex items-center justify-center md:w-16 py-2 md:py-0">
        <div class="flex flex-col items-center gap-1">
          <span class="text-[10px] text-smo-muted">注文</span>
          <i data-lucide="arrow-right" class="w-5 h-5 text-smo-navy hidden md:block"></i>
          <i data-lucide="arrow-down" class="w-5 h-5 text-smo-navy md:hidden"></i>
        </div>
      </div>

      <!-- API（ウェイター） -->
      <div class="w-44 bg-smo-accent/10 border-2 border-smo-accent/30 rounded-xl p-5 text-center">
        <div class="w-12 h-12 rounded-full bg-smo-accent/20 flex items-center justify-center mx-auto mb-3">
          <i data-lucide="message-square" class="w-6 h-6 text-smo-accent"></i>
        </div>
        <div class="font-bold text-smo-accent mb-1">API</div>
        <div class="text-xs text-smo-navy/70">ウェイター</div>
        <div class="text-xs text-smo-muted mt-3 bg-smo-bg rounded-lg px-3 py-1.5">注文を伝え、料理を届ける</div>
      </div>

      <!-- 矢印 2 -->
      <div class="flex items-center justify-center md:w-16 py-2 md:py-0">
        <div class="flex flex-col items-center gap-1">
          <span class="text-[10px] text-smo-muted">依頼</span>
          <i data-lucide="arrow-right" class="w-5 h-5 text-smo-navy hidden md:block"></i>
          <i data-lucide="arrow-down" class="w-5 h-5 text-smo-navy md:hidden"></i>
        </div>
      </div>

      <!-- サーバー（厨房） -->
      <div class="w-44 bg-smo-teal/15 border border-smo-teal/30 rounded-xl p-5 text-center">
        <div class="w-12 h-12 rounded-full bg-smo-teal/20 flex items-center justify-center mx-auto mb-3">
          <i data-lucide="server" class="w-6 h-6 text-smo-positive"></i>
        </div>
        <div class="font-bold text-smo-positive mb-1">サーバー</div>
        <div class="text-xs text-smo-positive/70">厨房</div>
        <div class="text-xs text-smo-muted mt-3 bg-smo-bg rounded-lg px-3 py-1.5">パスタを作って渡す</div>
      </div>
    </div>

    <div class="flex justify-center mt-6">
      <div class="flex items-center gap-2 text-smo-muted text-sm">
        <i data-lucide="corner-down-left" class="w-4 h-4"></i>
        料理（レスポンス）があなたのテーブルに届く
      </div>
    </div>
  </div>

  <p class="mb-6 leading-relaxed">
    この比喩がAPIの本質をほぼ言い当てています。あなた（アプリ）は、厨房（サーバー）の中で何が起きているかを知る必要がありません。ウェイター（API）に決まった形式で注文を伝えれば、結果が返ってくる。これがAPIです。
  </p>

  <!-- ポイントボックス -->
  <div class="bg-smo-accent/5 border border-smo-accent/20 rounded-xl p-5">
    <div class="flex items-start gap-3">
      <div class="flex items-center justify-center w-8 h-8 rounded-lg bg-smo-accent/10 flex-shrink-0 mt-0.5">
        <i data-lucide="lightbulb" class="w-4 h-4 text-smo-accent"></i>
      </div>
      <div>
        <p class="font-bold text-smo-accent mb-1">ここがポイント</p>
        <p class="text-smo-muted leading-relaxed">
          APIは<strong class="text-smo-text">「仲介役」</strong>です。相手の内部構造を知らなくても、<strong class="text-smo-text">決まったルールで話しかければ結果が返ってくる</strong>。これがAPIの本質です。この「決まったルール」のことを、エンジニアは「インターフェース（Interface）」と呼びます。
        </p>
      </div>
    </div>
  </div>
</section>


<!-- ============================================================ -->
<!--  SECTION 2: もう少し正確に言うと                               -->
<!-- ============================================================ -->
<section class="mb-16 md:mb-20">
  <div class="text-center mb-10">
    <p class="font-display text-sm font-bold text-smo-accent tracking-[0.25em] mb-2">02</p>
    <h2 class="text-2xl md:text-3xl font-bold text-smo-navy leading-snug mb-4">もう少し正確に言うと</h2>
    <div class="w-16 h-1 rounded-full bg-gradient-to-r from-smo-accent to-smo-teal mx-auto"></div>
  </div>

  <p class="mb-6 leading-relaxed">
    レストランのたとえで、ざっくりとしたイメージはつかめましたか？ ここからもう少しだけ正確に説明します。
  </p>

  <p class="mb-8 leading-relaxed">
    APIとは、ひとことで言えば<strong class="text-smo-text">「ソフトウェア同士が会話するための窓口」</strong>です。あなたが使っているアプリの裏側で、別のサービスのデータや機能を借りてくるための「取り決め」と考えてください。
  </p>

  <div class="bg-smo-surface border border-smo-border rounded-xl p-6 mb-8 text-center">
    <div class="text-xs text-smo-dim font-medium tracking-widest uppercase mb-3">技術的な定義</div>
    <p class="text-lg md:text-xl font-bold text-smo-text leading-relaxed">
      API = あるソフトウェアの機能を、<br class="hidden md:block">
      別のソフトウェアから使えるようにする仕組み
    </p>
    <p class="text-xs text-smo-dim mt-3">出典: <a href="https://developer.mozilla.org/ja/docs/Learn/JavaScript/Client-side_web_APIs/Introduction" class="underline decoration-smo-dim/30 hover:text-smo-navy transition-colors">MDN Web Docs — Web API の紹介</a></p>
  </div>

  <p class="mb-8 leading-relaxed">
    これだけだとまだ抽象的に感じるかもしれません。では、<strong class="text-smo-text">APIがある世界とない世界</strong>を比べてみましょう。
  </p>

  <!-- Before / After 比較 -->
  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <!-- Before -->
    <div class="bg-smo-negative/10 border border-smo-negative/20 rounded-xl p-6">
      <div class="inline-flex items-center gap-1.5 bg-smo-negative/10 text-smo-negative px-3 py-1 rounded-full text-xs font-bold tracking-wide mb-5">
        <i data-lucide="x-circle" class="w-3.5 h-3.5"></i>
        BEFORE — APIがない世界
      </div>
      <ul class="space-y-3">
        <li class="flex items-start gap-2.5">
          <i data-lucide="x" class="w-4 h-4 text-smo-negative mt-1 flex-shrink-0"></i>
          <span>天気情報が欲しければ、<strong class="text-smo-negative">自分で気象観測の仕組み</strong>を構築する</span>
        </li>
        <li class="flex items-start gap-2.5">
          <i data-lucide="x" class="w-4 h-4 text-smo-negative mt-1 flex-shrink-0"></i>
          <span>決済機能が欲しければ、<strong class="text-smo-negative">クレジットカード処理を自前で開発</strong>する</span>
        </li>
        <li class="flex items-start gap-2.5">
          <i data-lucide="x" class="w-4 h-4 text-smo-negative mt-1 flex-shrink-0"></i>
          <span>地図を表示したければ、<strong class="text-smo-negative">地図データを自分で作成・更新</strong>する</span>
        </li>
        <li class="flex items-start gap-2.5">
          <i data-lucide="x" class="w-4 h-4 text-smo-negative mt-1 flex-shrink-0"></i>
          <span>ユーザー認証は<strong class="text-smo-negative">パスワード管理からセキュリティ対策まで全部自前</strong></span>
        </li>
      </ul>
      <div class="mt-5 pt-4 border-t border-smo-negative/15 text-sm text-smo-negative/80 flex items-center gap-2">
        <i data-lucide="alert-circle" class="w-4 h-4"></i>
        膨大な開発コストと時間。バグのリスクも高い。
      </div>
    </div>

    <!-- After -->
    <div class="bg-smo-teal/10 border border-smo-teal/30 rounded-xl p-6">
      <div class="inline-flex items-center gap-1.5 bg-smo-teal/15 text-smo-positive px-3 py-1 rounded-full text-xs font-bold tracking-wide mb-5">
        <i data-lucide="check-circle" class="w-3.5 h-3.5"></i>
        AFTER — APIがある世界
      </div>
      <ul class="space-y-3">
        <li class="flex items-start gap-2.5">
          <i data-lucide="check" class="w-4 h-4 text-smo-positive mt-1 flex-shrink-0"></i>
          <span>天気情報は<strong class="text-smo-positive">天気予報APIに問い合わせるだけ</strong>で取得できる</span>
        </li>
        <li class="flex items-start gap-2.5">
          <i data-lucide="check" class="w-4 h-4 text-smo-positive mt-1 flex-shrink-0"></i>
          <span>決済は<strong class="text-smo-positive">Stripe APIに任せれば数行のコード</strong>で完成</span>
        </li>
        <li class="flex items-start gap-2.5">
          <i data-lucide="check" class="w-4 h-4 text-smo-positive mt-1 flex-shrink-0"></i>
          <span>地図は<strong class="text-smo-positive">Google Maps APIで高品質な地図を即表示</strong>できる</span>
        </li>
        <li class="flex items-start gap-2.5">
          <i data-lucide="check" class="w-4 h-4 text-smo-positive mt-1 flex-shrink-0"></i>
          <span>ログインは<strong class="text-smo-positive">GoogleやAppleのAPIで安全に認証</strong>できる</span>
        </li>
      </ul>
      <div class="mt-5 pt-4 border-t border-smo-teal/20 text-sm text-smo-positive/80 flex items-center gap-2">
        <i data-lucide="zap" class="w-4 h-4"></i>
        「自分が本当に作るべきもの」に集中できる。
      </div>
    </div>
  </div>
</section>


<!-- ============================================================ -->
<!--  SECTION 3: APIの仕組み                                       -->
<!-- ============================================================ -->
<section class="mb-16 md:mb-20">
  <div class="text-center mb-10">
    <p class="font-display text-sm font-bold text-smo-accent tracking-[0.25em] mb-2">03</p>
    <h2 class="text-2xl md:text-3xl font-bold text-smo-navy leading-snug mb-4">APIの仕組み — リクエストとレスポンス</h2>
    <div class="w-16 h-1 rounded-full bg-gradient-to-r from-smo-accent to-smo-teal mx-auto"></div>
  </div>

  <p class="mb-6 leading-relaxed">
    APIでのやり取りは、実はとてもシンプルです。基本は<strong class="text-smo-text">「聞く（リクエスト）」</strong>と<strong class="text-smo-text">「答える（レスポンス）」</strong>の2つだけ。
  </p>

  <p class="mb-8 leading-relaxed">
    リクエスト（Request）とは、「こういう情報をください」「この処理をしてください」とAPIに送るメッセージのことです。レスポンス（Response）は、APIがその要求に対して返す結果です。この2つのやり取りを分解すると、4つのステップになります。
  </p>

  <!-- 4ステップフロー図 -->
  <div class="bg-smo-surface border border-smo-border rounded-xl p-6 md:p-8 mb-8">
    <h3 class="text-lg font-bold text-smo-text text-center mb-8">APIリクエスト〜レスポンスの流れ</h3>

    <div class="flex flex-col md:flex-row items-stretch justify-center gap-3 md:gap-0">
      <div class="flex-1 bg-smo-accent/10 border border-smo-accent/20 rounded-xl p-4 text-center">
        <div class="w-8 h-8 rounded-full bg-smo-accent text-white text-sm font-bold flex items-center justify-center mx-auto mb-3">1</div>
        <i data-lucide="send" class="w-6 h-6 text-smo-navy mx-auto mb-2"></i>
        <div class="font-bold text-smo-navy text-sm mb-1">リクエスト送信</div>
        <div class="text-xs text-smo-muted leading-relaxed">あなたのアプリが<br>「こういう情報ください」<br>とAPIに送る</div>
      </div>

      <div class="flex items-center justify-center md:w-10 py-1 md:py-0">
        <i data-lucide="chevron-right" class="w-5 h-5 text-smo-dim hidden md:block"></i>
        <i data-lucide="chevron-down" class="w-5 h-5 text-smo-dim md:hidden"></i>
      </div>

      <div class="flex-1 bg-smo-navy/10 border border-smo-navy/20 rounded-xl p-4 text-center">
        <div class="w-8 h-8 rounded-full bg-smo-navy text-white text-sm font-bold flex items-center justify-center mx-auto mb-3">2</div>
        <i data-lucide="shield" class="w-6 h-6 text-smo-navy mx-auto mb-2"></i>
        <div class="font-bold text-smo-navy text-sm mb-1">APIが受け取る</div>
        <div class="text-xs text-smo-muted leading-relaxed">リクエストの内容を<br>チェック・認証する<br>（門番の役割）</div>
      </div>

      <div class="flex items-center justify-center md:w-10 py-1 md:py-0">
        <i data-lucide="chevron-right" class="w-5 h-5 text-smo-dim hidden md:block"></i>
        <i data-lucide="chevron-down" class="w-5 h-5 text-smo-dim md:hidden"></i>
      </div>

      <div class="flex-1 bg-smo-teal/15 border border-smo-teal/30 rounded-xl p-4 text-center">
        <div class="w-8 h-8 rounded-full bg-smo-positive text-white text-sm font-bold flex items-center justify-center mx-auto mb-3">3</div>
        <i data-lucide="database" class="w-6 h-6 text-smo-positive mx-auto mb-2"></i>
        <div class="font-bold text-smo-positive text-sm mb-1">サーバーが処理</div>
        <div class="text-xs text-smo-muted leading-relaxed">データベース検索や<br>計算など、実際の<br>処理を実行する</div>
      </div>

      <div class="flex items-center justify-center md:w-10 py-1 md:py-0">
        <i data-lucide="chevron-right" class="w-5 h-5 text-smo-dim hidden md:block"></i>
        <i data-lucide="chevron-down" class="w-5 h-5 text-smo-dim md:hidden"></i>
      </div>

      <div class="flex-1 bg-smo-warning/10 border border-smo-warning/20 rounded-xl p-4 text-center">
        <div class="w-8 h-8 rounded-full bg-smo-warning text-white text-sm font-bold flex items-center justify-center mx-auto mb-3">4</div>
        <i data-lucide="reply" class="w-6 h-6 text-smo-warning mx-auto mb-2"></i>
        <div class="font-bold text-smo-warning text-sm mb-1">レスポンス返却</div>
        <div class="text-xs text-smo-muted leading-relaxed">処理結果をあなたの<br>アプリに返す<br>（料理が届く瞬間）</div>
      </div>
    </div>
  </div>

  <p class="mb-6 leading-relaxed">
    言葉だけだとまだピンとこないかもしれません。では、実際のコードで見てみましょう。たとえば、天気予報APIから東京の天気を取得するコードは、たったこれだけです。
  </p>

  <!-- コード例: JavaScript -->
  <div class="mb-6">
    <div class="flex items-center gap-2 bg-slate-800 border border-slate-700/50 rounded-t-xl px-4 py-2.5 text-xs text-smo-muted">
      <i data-lucide="code" class="w-3.5 h-3.5"></i>
      JavaScript — 天気予報APIの呼び出し例
    </div>
    <pre class="bg-slate-950 border border-slate-700/50 border-t-0 rounded-b-xl p-5 overflow-x-auto text-sm leading-loose"><code><span class="text-slate-500">// 1. APIにリクエストを送る（「東京の天気を教えて」と聞く）</span>
<span class="text-purple-400">const</span> response <span class="text-slate-400">=</span> <span class="text-purple-400">await</span> <span class="text-blue-400">fetch</span>(<span class="text-emerald-400">"https://api.weather.example.com/current?city=tokyo"</span>);

<span class="text-slate-500">// 2. レスポンスをJSON形式（データの構造）に変換する</span>
<span class="text-purple-400">const</span> data <span class="text-slate-400">=</span> <span class="text-purple-400">await</span> response.<span class="text-blue-400">json</span>();

<span class="text-slate-500">// 3. 必要なデータを取り出して使う</span>
console.<span class="text-blue-400">log</span>(data.temperature); <span class="text-slate-500">// → "22°C"</span>
console.<span class="text-blue-400">log</span>(data.condition);   <span class="text-slate-500">// → "晴れ"</span>
console.<span class="text-blue-400">log</span>(data.humidity);    <span class="text-slate-500">// → "65%"</span></code></pre>
  </div>

  <!-- コード解説 -->
  <div class="bg-smo-surface border border-smo-border rounded-xl p-5 mb-8">
    <h4 class="text-sm font-bold text-smo-text mb-4 flex items-center gap-2">
      <i data-lucide="file-text" class="w-4 h-4 text-smo-navy"></i>
      コードの解説（1行ずつ読み解く）
    </h4>
    <div class="space-y-4 text-sm">
      <div class="flex items-start gap-3">
        <span class="text-xs font-mono bg-smo-accent/10 text-smo-navy px-2 py-0.5 rounded flex-shrink-0 mt-0.5">1</span>
        <span class="leading-relaxed"><code class="text-smo-positive text-xs bg-smo-bg px-1.5 py-0.5 rounded">fetch()</code> は「指定したURLに問い合わせる」命令。URLの末尾にある <code class="text-smo-positive text-xs bg-smo-bg px-1.5 py-0.5 rounded">?city=tokyo</code> が「東京の情報が欲しい」というリクエストの中身です。レストランのたとえで言えば「パスタください」にあたる部分。</span>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-xs font-mono bg-smo-navy/10 text-smo-navy px-2 py-0.5 rounded flex-shrink-0 mt-0.5">2</span>
        <span class="leading-relaxed">返ってきたデータは機械向けの生データなので、<code class="text-smo-positive text-xs bg-smo-bg px-1.5 py-0.5 rounded">.json()</code> で人間が読みやすい形（JSON = JavaScript Object Notation）に変換します。JSONは「名前: 値」の組み合わせでデータを表現する書式で、Web業界で最も広く使われています。</span>
      </div>
      <div class="flex items-start gap-3">
        <span class="text-xs font-mono bg-smo-teal/15 text-smo-positive px-2 py-0.5 rounded flex-shrink-0 mt-0.5">3</span>
        <span class="leading-relaxed">変換したデータから <code class="text-smo-positive text-xs bg-smo-bg px-1.5 py-0.5 rounded">data.temperature</code> のように、ドット（.）で区切って欲しい情報を名前で取り出します。辞書で単語を引くのに似ています。</span>
      </div>
    </div>
  </div>

  <p class="mb-4 leading-relaxed">
    ターミナル（コマンドを入力する黒い画面）からもAPIを試せます。<code class="text-smo-positive text-xs bg-smo-bg px-1.5 py-0.5 rounded">curl</code>（カール）というコマンドを使うと、たった1行でAPIにリクエストを送れます。
  </p>

  <!-- ターミナルUIモックアップ: curl -->
  <div class="mb-8 rounded-xl overflow-hidden border border-slate-700/50">
    <div class="flex items-center gap-3 bg-slate-800 px-4 py-2.5">
      <div class="flex gap-1.5">
        <div class="w-3 h-3 rounded-full bg-red-500/80"></div>
        <div class="w-3 h-3 rounded-full bg-yellow-500/80"></div>
        <div class="w-3 h-3 rounded-full bg-green-500/80"></div>
      </div>
      <div class="flex items-center gap-1.5 text-xs text-slate-400">
        <i data-lucide="terminal" class="w-3.5 h-3.5"></i>
        ターミナル — curlコマンドでAPIを叩く
      </div>
    </div>
    <pre class="bg-slate-950 p-5 overflow-x-auto text-sm leading-loose"><code><span class="text-emerald-400">$</span> curl https://api.weather.example.com/current?city=tokyo

<span class="text-slate-500"># 返ってくるレスポンス（JSON形式）</span>
{
  <span class="text-blue-400">"city"</span>: <span class="text-emerald-400">"東京"</span>,
  <span class="text-blue-400">"temperature"</span>: <span class="text-amber-400">"22°C"</span>,
  <span class="text-blue-400">"condition"</span>: <span class="text-emerald-400">"晴れ"</span>,
  <span class="text-blue-400">"humidity"</span>: <span class="text-amber-400">"65%"</span>
}</code></pre>
  </div>

  <div class="bg-smo-warning/5 border border-smo-warning/20 rounded-xl p-5">
    <div class="flex items-start gap-3">
      <div class="flex items-center justify-center w-8 h-8 rounded-lg bg-smo-warning/10 flex-shrink-0 mt-0.5">
        <i data-lucide="info" class="w-4 h-4 text-smo-warning"></i>
      </div>
      <div>
        <p class="font-bold text-smo-warning mb-1">ちょっと補足: URLの構造</p>
        <p class="text-smo-muted leading-relaxed text-sm">
          <code class="text-smo-positive text-xs bg-smo-bg px-1.5 py-0.5 rounded">https://api.weather.example.com/current?city=tokyo</code> のURLは、大きく3つの部分に分かれます。<strong class="text-smo-text">api.weather.example.com</strong> がAPIの住所（ベースURL）、<strong class="text-smo-text">/current</strong> が「何を」（現在の天気）、<strong class="text-smo-text">?city=tokyo</strong> が「どこの」（東京）というパラメータです。レストランで例えると「〇〇レストランの（住所）、メインメニューから（何を）、パスタを（詳細）」に対応します。
        </p>
      </div>
    </div>
  </div>

  <p class="mt-8 mb-6 leading-relaxed">
    では、このAPIのレスポンスが実際のアプリではどう表示されるのでしょうか？ あなたが見ている天気アプリの画面を覗いてみましょう。
  </p>

  <!-- ブラウザUIモックアップ -->
  <div class="rounded-xl overflow-hidden border border-slate-700/50 mb-8">
    <div class="flex items-center gap-3 bg-slate-800 px-4 py-2.5">
      <div class="flex gap-1.5">
        <div class="w-3 h-3 rounded-full bg-red-500/80"></div>
        <div class="w-3 h-3 rounded-full bg-yellow-500/80"></div>
        <div class="w-3 h-3 rounded-full bg-green-500/80"></div>
      </div>
      <div class="flex-1 bg-slate-700/50 rounded-lg px-3 py-1 text-xs text-slate-400 flex items-center gap-1.5">
        <i data-lucide="lock" class="w-3 h-3 text-emerald-400"></i>
        weather-app.example.com
      </div>
    </div>
    <div class="bg-gradient-to-b from-sky-100 to-sky-50 p-6 md:p-8">
      <div class="text-center">
        <div class="text-xs text-sky-600/70 font-medium mb-1">現在地: 東京</div>
        <div class="flex items-center justify-center gap-2 mb-2">
          <i data-lucide="sun" class="w-10 h-10 text-smo-warning"></i>
          <span class="text-4xl font-bold text-sky-900">22°C</span>
        </div>
        <div class="text-sm text-sky-700 font-medium mb-4">晴れ</div>
        <div class="flex justify-center gap-6 text-xs text-sky-600/80">
          <div class="flex items-center gap-1"><i data-lucide="droplets" class="w-3.5 h-3.5"></i> 65%</div>
          <div class="flex items-center gap-1"><i data-lucide="wind" class="w-3.5 h-3.5"></i> 3m/s</div>
        </div>
      </div>
    </div>
  </div>

  <div class="bg-smo-accent/5 border border-smo-accent/20 rounded-xl p-5">
    <div class="flex items-start gap-3">
      <div class="flex items-center justify-center w-8 h-8 rounded-lg bg-smo-accent/10 flex-shrink-0 mt-0.5">
        <i data-lucide="lightbulb" class="w-4 h-4 text-smo-accent"></i>
      </div>
      <div>
        <p class="font-bold text-smo-accent mb-1">APIの結果 → アプリの画面</p>
        <p class="text-smo-muted leading-relaxed">
          上の天気アプリは、裏側で <code class="text-smo-positive text-xs bg-smo-bg px-1.5 py-0.5 rounded">temperature: "22°C"</code> や <code class="text-smo-positive text-xs bg-smo-bg px-1.5 py-0.5 rounded">condition: "晴れ"</code> というAPIレスポンスを受け取り、見やすいデザインに変換して表示しています。<strong class="text-smo-text">あなたが普段見ているきれいな画面の裏側では、こうしたAPIのやり取りが行われている</strong>のです。
        </p>
      </div>
    </div>
  </div>
</section>


<!-- ============================================================ -->
<!--  SECTION 4: 身近なAPIの例                                     -->
<!-- ============================================================ -->
<section class="mb-16 md:mb-20">
  <div class="text-center mb-10">
    <p class="font-display text-sm font-bold text-smo-accent tracking-[0.25em] mb-2">04</p>
    <h2 class="text-2xl md:text-3xl font-bold text-smo-navy leading-snug mb-4">身近なAPIの例 — 実はあなたも毎日使っている</h2>
    <div class="w-16 h-1 rounded-full bg-gradient-to-r from-smo-accent to-smo-teal mx-auto"></div>
  </div>

  <p class="mb-8 leading-relaxed">
    「API」と聞くとプログラマーの専門用語に聞こえるかもしれません。しかし、あなたがスマホで何気なくやっている日常の操作の裏側では、たくさんのAPIが動いています。<strong class="text-smo-text">「あなたが見ている画面」の裏側で、APIが何をしているのか</strong>を図解します。
  </p>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <!-- 天気予報アプリ -->
    <div class="bg-smo-surface border border-smo-border rounded-xl overflow-hidden">
      <div class="bg-gradient-to-b from-sky-100 to-sky-50 p-5">
        <div class="text-center">
          <div class="text-[10px] text-sky-600/60 font-medium mb-0.5">東京</div>
          <div class="flex items-center justify-center gap-1.5 mb-1">
            <i data-lucide="sun" class="w-7 h-7 text-smo-warning"></i>
            <span class="text-2xl font-bold text-sky-900">22°C</span>
          </div>
          <div class="text-xs text-sky-700 font-medium mb-2">晴れ</div>
          <div class="flex justify-center gap-4 text-[10px] text-sky-600/70">
            <div class="flex items-center gap-0.5"><i data-lucide="droplets" class="w-3 h-3"></i> 65%</div>
            <div class="flex items-center gap-0.5"><i data-lucide="wind" class="w-3 h-3"></i> 3m/s</div>
          </div>
        </div>
      </div>
      <div class="p-5 pt-4">
        <h3 class="font-bold text-smo-text text-sm mb-2 flex items-center gap-2">
          <i data-lucide="cloud" class="w-4 h-4 text-smo-accent"></i> 天気予報アプリ
        </h3>
        <div class="text-xs text-smo-accent font-medium mb-1">裏側でAPIがやっていること</div>
        <p class="text-sm text-smo-muted leading-relaxed">気象庁のサーバーに「東京の最新天気データをください」とリクエストを送り、気温・天候・湿度・風速などのデータをJSON形式で受け取っている</p>
      </div>
    </div>

    <!-- Googleログイン -->
    <div class="bg-smo-surface border border-smo-border rounded-xl overflow-hidden">
      <div class="bg-white p-5 flex flex-col items-center justify-center">
        <div class="text-xs text-smo-muted mb-3">アカウントにログイン</div>
        <div class="flex items-center gap-2.5 border border-smo-border rounded-lg px-5 py-2.5 bg-white hover:bg-smo-band transition-colors">
          <div class="w-5 h-5 rounded-full bg-gradient-to-br from-blue-500 via-red-500 to-yellow-500 flex items-center justify-center">
            <span class="text-[8px] font-bold text-white">G</span>
          </div>
          <span class="text-sm font-medium text-smo-text">Google でログイン</span>
        </div>
        <div class="flex items-center gap-3 mt-3">
          <div class="flex-1 border-t border-smo-border/50"></div>
          <span class="text-[10px] text-smo-dim">または</span>
          <div class="flex-1 border-t border-smo-border/50"></div>
        </div>
        <div class="w-full mt-2 bg-smo-surface border border-smo-border/50 rounded-lg px-3 py-1.5 text-xs text-smo-dim">メールアドレスで登録</div>
      </div>
      <div class="p-5 pt-4">
        <h3 class="font-bold text-smo-text text-sm mb-2 flex items-center gap-2">
          <i data-lucide="log-in" class="w-4 h-4 text-smo-navy"></i> 「Googleでログイン」ボタン
        </h3>
        <div class="text-xs text-smo-navy font-medium mb-1">裏側でAPIがやっていること</div>
        <p class="text-sm text-smo-muted leading-relaxed">GoogleのOAuth API（オーオース = 認可の仕組み）に「このユーザーの身元を確認してください」と問い合わせ、認証トークン（本人確認済みの証）を受け取っている</p>
      </div>
    </div>

    <!-- オンライン決済 -->
    <div class="bg-smo-surface border border-smo-border rounded-xl overflow-hidden">
      <div class="bg-gradient-to-b from-emerald-50 to-white p-5 text-center">
        <div class="w-10 h-10 rounded-full bg-smo-teal/15 flex items-center justify-center mx-auto mb-2">
          <i data-lucide="check" class="w-6 h-6 text-smo-positive"></i>
        </div>
        <div class="text-sm font-bold text-smo-positive mb-1">お支払い完了</div>
        <div class="text-xl font-bold text-smo-text mb-1">&#165;1,980</div>
        <div class="text-[10px] text-smo-dim">VISA **** 4242</div>
      </div>
      <div class="p-5 pt-4">
        <h3 class="font-bold text-smo-text text-sm mb-2 flex items-center gap-2">
          <i data-lucide="credit-card" class="w-4 h-4 text-smo-positive"></i> オンライン決済
        </h3>
        <div class="text-xs text-smo-positive font-medium mb-1">裏側でAPIがやっていること</div>
        <p class="text-sm text-smo-muted leading-relaxed">Stripe等の決済APIが、クレジットカード会社のサーバーと暗号化通信を行い、与信確認（この人は支払える？）→ 決済処理 → 結果通知を実行している</p>
        <p class="text-[10px] text-smo-dim mt-2">出典: <a href="https://docs.stripe.com/api" class="underline decoration-smo-dim/30 hover:text-smo-navy transition-colors">Stripe API 公式ドキュメント</a></p>
      </div>
    </div>

    <!-- 地図・ナビ -->
    <div class="bg-smo-surface border border-smo-border rounded-xl overflow-hidden">
      <div class="bg-emerald-50/50 p-5">
        <div class="relative bg-emerald-100/80 rounded-lg p-4 h-28 flex flex-col justify-between">
          <div class="flex items-center gap-1.5">
            <div class="w-4 h-4 rounded-full bg-smo-accent border-2 border-white flex items-center justify-center">
              <div class="w-1.5 h-1.5 bg-white rounded-full"></div>
            </div>
            <span class="text-[10px] text-smo-navy font-medium">現在地</span>
          </div>
          <div class="border-l-2 border-dashed border-smo-accent/60 ml-2 h-6"></div>
          <div class="flex items-center justify-between">
            <div class="flex items-center gap-1.5">
              <i data-lucide="map-pin" class="w-4 h-4 text-smo-negative"></i>
              <span class="text-[10px] text-smo-negative font-medium">東京駅</span>
            </div>
            <div class="bg-white rounded-full px-2 py-0.5 text-[10px] font-bold text-smo-navy border border-smo-border">12分</div>
          </div>
        </div>
      </div>
      <div class="p-5 pt-4">
        <h3 class="font-bold text-smo-text text-sm mb-2 flex items-center gap-2">
          <i data-lucide="map-pin" class="w-4 h-4 text-smo-negative"></i> 地図・ナビアプリ
        </h3>
        <div class="text-xs text-smo-negative font-medium mb-1">裏側でAPIがやっていること</div>
        <p class="text-sm text-smo-muted leading-relaxed">Google Maps APIが地図画像の取得、現在の交通情報の取得、経路計算をそれぞれ別のAPIに問い合わせ、統合して表示している</p>
      </div>
    </div>
  </div>

  <div class="mt-8 bg-smo-accent/5 border border-smo-accent/20 rounded-xl p-5">
    <div class="flex items-start gap-3">
      <div class="flex items-center justify-center w-8 h-8 rounded-lg bg-smo-accent/10 flex-shrink-0 mt-0.5">
        <i data-lucide="lightbulb" class="w-4 h-4 text-smo-accent"></i>
      </div>
      <div>
        <p class="font-bold text-smo-accent mb-1">気づきましたか？</p>
        <p class="text-smo-muted leading-relaxed text-sm">
          上の4つの例に共通しているのは、<strong class="text-smo-text">あなたがAPIの存在を意識していない</strong>ということです。天気を確認するとき「今からAPIを呼ぶぞ」とは思いませんよね。優れたAPIは、ユーザーにその存在を感じさせません。まるで空気のように、裏側で静かに仕事をしているのです。
        </p>
      </div>
    </div>
  </div>
</section>


<!-- ============================================================ -->
<!--  SECTION 5: APIを使うとどう嬉しいか                            -->
<!-- ============================================================ -->
<section class="mb-16 md:mb-20">
  <div class="text-center mb-10">
    <p class="font-display text-sm font-bold text-smo-accent tracking-[0.25em] mb-2">05</p>
    <h2 class="text-2xl md:text-3xl font-bold text-smo-navy leading-snug mb-4">APIを使うとどう嬉しいか</h2>
    <div class="w-16 h-1 rounded-full bg-gradient-to-r from-smo-accent to-smo-teal mx-auto"></div>
  </div>

  <p class="mb-8 leading-relaxed">
    ここまで読んで「APIは便利そうだ」と感じてもらえたと思います。では、開発者の視点から見たとき、APIを使うことで<strong class="text-smo-text">具体的にどのくらいの効果</strong>があるのか。数字と一緒に見てみましょう。
  </p>

  <!-- 円形スタットバッジ（しごおもラボ固有。数字を主役にする） -->
  <div class="flex flex-wrap justify-center gap-5 md:gap-8 mb-6">
    <div class="w-36 h-36 rounded-full bg-white border-2 border-smo-accent flex flex-col items-center justify-center text-center px-3">
      <span class="text-[11px] text-smo-muted leading-tight mb-1">あなたが1日に<br>使っている回数</span>
      <span class="text-3xl font-bold text-smo-accent leading-none">50<span class="text-base">回</span></span>
      <span class="text-[11px] text-smo-muted mt-1">以上</span>
    </div>
    <div class="w-36 h-36 rounded-full bg-white border-2 border-smo-teal flex flex-col items-center justify-center text-center px-3">
      <span class="text-[11px] text-smo-muted leading-tight mb-1">世界で公開されて<br>いるAPIの数</span>
      <span class="text-3xl font-bold text-smo-teal leading-none">24,000</span>
      <span class="text-[11px] text-smo-muted mt-1">以上</span>
    </div>
    <div class="w-36 h-36 rounded-full bg-white border-2 border-smo-navy flex flex-col items-center justify-center text-center px-3">
      <span class="text-[11px] text-smo-muted leading-tight mb-1">多くのAPIの<br>平均応答時間</span>
      <span class="text-3xl font-bold text-smo-navy leading-none">0.2<span class="text-base">秒</span></span>
    </div>
  </div>
  <p class="text-[10px] text-smo-dim text-center mb-10">出典: <a href="https://www.programmableweb.com/" class="underline decoration-smo-dim/30 hover:text-smo-accent transition-colors">ProgrammableWeb</a></p>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
    <div class="flex gap-4 bg-smo-surface border border-smo-border rounded-xl p-5">
      <div class="w-10 h-10 rounded-lg bg-smo-warning/10 flex items-center justify-center flex-shrink-0">
        <i data-lucide="zap" class="w-5 h-5 text-smo-warning"></i>
      </div>
      <div>
        <h3 class="font-bold text-smo-text mb-2">開発スピードが上がる</h3>
        <p class="text-sm text-smo-muted leading-relaxed">決済、認証、地図、翻訳...。これらをゼロから作ると何ヶ月もかかりますが、APIを使えば数日〜数時間で実装できます。車を作りたいとき、エンジンから設計する必要はないのです。</p>
      </div>
    </div>

    <div class="flex gap-4 bg-smo-surface border border-smo-border rounded-xl p-5">
      <div class="w-10 h-10 rounded-lg bg-smo-accent/10 flex items-center justify-center flex-shrink-0">
        <i data-lucide="shield" class="w-5 h-5 text-smo-navy"></i>
      </div>
      <div>
        <h3 class="font-bold text-smo-text mb-2">品質が担保される</h3>
        <p class="text-sm text-smo-muted leading-relaxed">Google Maps、Stripe、AWSなど、各分野の専門企業が何千人体制で開発・運用しているAPIの品質は、個人や小さなチームで再現できるレベルではありません。その品質を「借りる」ことができます。</p>
      </div>
    </div>

    <div class="flex gap-4 bg-smo-surface border border-smo-border rounded-xl p-5">
      <div class="w-10 h-10 rounded-lg bg-smo-navy/10 flex items-center justify-center flex-shrink-0">
        <i data-lucide="refresh-cw" class="w-5 h-5 text-smo-navy"></i>
      </div>
      <div>
        <h3 class="font-bold text-smo-text mb-2">保守の手間が減る</h3>
        <p class="text-sm text-smo-muted leading-relaxed">API提供元がバグ修正・機能改善・セキュリティ更新を継続的に行ってくれます。あなたはAPIを「使うだけ」。自分でゼロから作った機能は、自分でずっと面倒を見続ける必要があります。</p>
      </div>
    </div>

    <div class="flex gap-4 bg-smo-surface border border-smo-border rounded-xl p-5">
      <div class="w-10 h-10 rounded-lg bg-smo-teal/15 flex items-center justify-center flex-shrink-0">
        <i data-lucide="layers" class="w-5 h-5 text-smo-positive"></i>
      </div>
      <div>
        <h3 class="font-bold text-smo-text mb-2">レゴのように拡張できる</h3>
        <p class="text-sm text-smo-muted leading-relaxed">APIはレゴブロックのように組み合わせられます。たとえば「翻訳API + 音声合成API」を組み合わせれば、多言語音声読み上げ機能が作れます。1つのAPIだけでは実現できない価値が、組み合わせで生まれるのです。</p>
      </div>
    </div>
  </div>
</section>


<!-- ============================================================ -->
<!--  SECTION 6: よくある誤解                                      -->
<!-- ============================================================ -->
<section class="mb-16 md:mb-20">
  <div class="text-center mb-10">
    <p class="font-display text-sm font-bold text-smo-accent tracking-[0.25em] mb-2">06</p>
    <h2 class="text-2xl md:text-3xl font-bold text-smo-navy leading-snug mb-4">よくある誤解</h2>
    <div class="w-16 h-1 rounded-full bg-gradient-to-r from-smo-accent to-smo-teal mx-auto"></div>
  </div>

  <p class="mb-8 leading-relaxed">
    APIについて学び始めると、多くの人が同じところでつまずきます。ここでは、初学者が陥りがちな3つの誤解を取り上げて、正しい理解に修正します。
  </p>

  <div class="space-y-4">
    <div class="bg-smo-surface border border-smo-border rounded-xl overflow-hidden">
      <div class="flex items-center gap-3 px-6 py-4 bg-smo-negative/10 border-b border-smo-border/50">
        <div class="w-6 h-6 rounded-full bg-smo-negative/10 flex items-center justify-center flex-shrink-0">
          <i data-lucide="x" class="w-3.5 h-3.5 text-smo-negative"></i>
        </div>
        <h3 class="font-bold text-smo-negative text-sm">誤解: 「APIはプログラマーだけが使うもの」</h3>
      </div>
      <div class="px-6 py-5">
        <div class="flex items-start gap-3">
          <div class="w-6 h-6 rounded-full bg-smo-teal/15 flex items-center justify-center flex-shrink-0 mt-0.5">
            <i data-lucide="check" class="w-3.5 h-3.5 text-smo-positive"></i>
          </div>
          <div>
            <p class="text-sm font-bold text-smo-positive mb-2">実際は:</p>
            <p class="text-sm text-smo-muted leading-relaxed">
              あなたも毎日APIを使っています。朝、天気アプリを開く。SNSにログインする。電子マネーで買い物する。これらの操作はすべて、裏側でAPIが動いています。プログラマーが「APIを使う」のは、この仕組みのコードを書いている側にいるだけの話。<strong class="text-smo-text">気づかないうちにAPIの恩恵を毎日受けている</strong>のです。
            </p>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-smo-surface border border-smo-border rounded-xl overflow-hidden">
      <div class="flex items-center gap-3 px-6 py-4 bg-smo-negative/10 border-b border-smo-border/50">
        <div class="w-6 h-6 rounded-full bg-smo-negative/10 flex items-center justify-center flex-shrink-0">
          <i data-lucide="x" class="w-3.5 h-3.5 text-smo-negative"></i>
        </div>
        <h3 class="font-bold text-smo-negative text-sm">誤解: 「APIって難しい技術でしょ？」</h3>
      </div>
      <div class="px-6 py-5">
        <div class="flex items-start gap-3">
          <div class="w-6 h-6 rounded-full bg-smo-teal/15 flex items-center justify-center flex-shrink-0 mt-0.5">
            <i data-lucide="check" class="w-3.5 h-3.5 text-smo-positive"></i>
          </div>
          <div>
            <p class="text-sm font-bold text-smo-positive mb-2">実際は:</p>
            <p class="text-sm text-smo-muted leading-relaxed">
              APIの概念自体は「注文して結果を受け取る」というシンプルな仕組みです。レストランで注文できるなら、APIの概念は理解できます。先ほどのコード例のように、実際のプログラムも数行で書けることがほとんどです。難しいのはAPIそのものではなく、<strong class="text-smo-text">「APIで何を作るか」を考える部分</strong>。道具はシンプル、使いこなすセンスが問われるということです。
            </p>
          </div>
        </div>
      </div>
    </div>

    <div class="bg-smo-surface border border-smo-border rounded-xl overflow-hidden">
      <div class="flex items-center gap-3 px-6 py-4 bg-smo-negative/10 border-b border-smo-border/50">
        <div class="w-6 h-6 rounded-full bg-smo-negative/10 flex items-center justify-center flex-shrink-0">
          <i data-lucide="x" class="w-3.5 h-3.5 text-smo-negative"></i>
        </div>
        <h3 class="font-bold text-smo-negative text-sm">誤解: 「APIを使うと個人情報が漏れそうで怖い」</h3>
      </div>
      <div class="px-6 py-5">
        <div class="flex items-start gap-3">
          <div class="w-6 h-6 rounded-full bg-smo-teal/15 flex items-center justify-center flex-shrink-0 mt-0.5">
            <i data-lucide="check" class="w-3.5 h-3.5 text-smo-positive"></i>
          </div>
          <div>
            <p class="text-sm font-bold text-smo-positive mb-2">実際は:</p>
            <p class="text-sm text-smo-muted leading-relaxed">
              適切に設計されたAPIは、<strong class="text-smo-text">必要最小限の情報だけ</strong>をやり取りします。たとえば銀行のAPIが口座残高を返す際、パスワードや暗証番号は一切含まれません。APIはデータの「窓口」であり、<strong class="text-smo-text">「何の情報を公開し、何を隠すか」を厳密に制御</strong>できます。むしろ、データベースに直接触るよりもAPIを介した方が安全なのです。レストランのたとえで言えば、お客さんが直接厨房に入るより、ウェイターを通した方が厨房の秩序が保たれるのと同じです。
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>


<!-- ============================================================ -->
<!--  SECTION 7: まとめ                                            -->
<!-- ============================================================ -->
<section>
  <div class="text-center mb-10">
    <p class="font-display text-sm font-bold text-smo-accent tracking-[0.25em] mb-2">07</p>
    <h2 class="text-2xl md:text-3xl font-bold text-smo-navy leading-snug mb-4">まとめ — 覚えておきたい3つのこと</h2>
    <div class="w-16 h-1 rounded-full bg-gradient-to-r from-smo-accent to-smo-teal mx-auto"></div>
  </div>

  <p class="mb-8 leading-relaxed">
    長い図解を読んでいただきありがとうございます。最後に、この記事で伝えたかったことを3つに絞ってまとめます。
  </p>

  <div class="space-y-4 mb-10">
    <div class="bg-smo-surface border border-smo-border rounded-xl p-6 border-l-4 border-l-smo-accent">
      <div class="flex items-start gap-4">
        <div class="font-display text-3xl font-bold text-smo-accent leading-none flex-shrink-0 mt-1">01</div>
        <div>
          <h3 class="font-bold text-smo-text mb-2">APIは「ソフトウェアの窓口」</h3>
          <p class="text-sm text-smo-muted leading-relaxed">
            レストランのウェイターのように、あなた（アプリ）とサーバーの間を取り持つ仲介役。相手の内部構造を知らなくても、決まったルール（インターフェース）で話しかければ結果が返ってきます。
          </p>
        </div>
      </div>
    </div>

    <div class="bg-smo-surface border border-smo-border rounded-xl p-6 border-l-4 border-l-smo-teal">
      <div class="flex items-start gap-4">
        <div class="font-display text-3xl font-bold text-smo-teal leading-none flex-shrink-0 mt-1">02</div>
        <div>
          <h3 class="font-bold text-smo-text mb-2">あなたはすでにAPIユーザー</h3>
          <p class="text-sm text-smo-muted leading-relaxed">
            天気予報、SNSログイン、地図検索、オンライン決済。気づかないうちに、あなたの日常はAPIに支えられています。APIは特別な人だけのものではなく、全員の生活を支える仕組みです。
          </p>
        </div>
      </div>
    </div>

    <div class="bg-smo-surface border border-smo-border rounded-xl p-6 border-l-4 border-l-smo-warning">
      <div class="flex items-start gap-4">
        <div class="font-display text-3xl font-bold text-smo-warning leading-none flex-shrink-0 mt-1">03</div>
        <div>
          <h3 class="font-bold text-smo-text mb-2">APIで「車輪の再発明」がなくなる</h3>
          <p class="text-sm text-smo-muted leading-relaxed">
            すでにある優れた機能をAPIで借りることで、自分は「自分にしか作れない部分」に集中できます。開発スピードが上がり、品質も上がり、保守の手間も減る。これがAPIの最大の恩恵です。
          </p>
        </div>
      </div>
    </div>
  </div>

  <div class="text-center bg-gradient-to-b from-smo-accent/5 to-transparent border border-smo-accent/10 rounded-xl p-8 md:p-10">
    <i data-lucide="globe" class="w-8 h-8 text-smo-navy mx-auto mb-4"></i>
    <p class="text-lg font-bold text-smo-text mb-3">APIは「知っている」だけで世界が広がる概念です。</p>
    <p class="text-smo-muted max-w-lg mx-auto leading-relaxed">
      次にアプリを使うとき、「この裏側でどんなAPIが動いているんだろう？」と想像してみてください。天気予報の数字も、ログインボタンも、決済完了の画面も、すべてAPIが繋いでいます。テクノロジーの見え方が、少しだけ変わるはずです。
    </p>
  </div>
</section>

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
