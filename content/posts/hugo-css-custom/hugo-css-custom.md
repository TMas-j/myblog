---
title: "Hugoブログの見た目をカスタマイズする（PaperMod）"
date: 2026-03-06T10:36:42+09:00
draft: false
slug: hugo-css-custom
tags: ["Hugo"]
categories: ["技術"]
description: "Hugoブログの見た目をカスタマイズする方法"
---

## はじめに

Hugoブログの見た目を少しよくするカスタマイズをしました。

## カスタムCSSの設置場所

Hugoの場合は、カスタムCSSは以下の場所に設置すればOKです。

```
assets/css/extended/custom.css
```

## フォント設定

Mac / Windows / 日本語環境で自然に表示されるフォントスタックに対応しました。

- apple-system → Mac / iOS
- Segoe UI → Windows
- Hiragino Sans → macOS日本語
- Noto Sans JP → Googleフォント
- Yu Gothic UI → Windows日本語

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
               "Hiragino Sans", "Noto Sans JP",
               "Yu Gothic UI", sans-serif;
}
```

記事本文の行間を少し広くする。

デフォルトより少し余裕を持たせることで
長い記事でも読みやすくなります。

```css
.post-content {
  line-height: 1.8;
}
```

## 記事カードのデザイン（トップページ）

記事一覧のカードの角を丸くする。

```css
.post-entry {
  border-radius: 10px;

  /*
  hover時のアニメーション
  */
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}
```

マウスを乗せたときに少し浮き上がるようなエフェクトを追加する。

```css
.post-entry:hover {
  transform: translateY(-3px);

  /*
  影をつけてカード感を出す
  */
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}
```

## 見出しの装飾

### H2見出し

左側にラインを付けて、
技術ブログっぽいデザインにする。

```css
.post-content h2 {
  border-left: 6px solid #6366f1;
  padding-left: 12px;
  margin-top: 2em;
}
```

### H3見出し

下線を追加して、
階層が分かりやすくなるようにする。

```css
.post-content h3 {
  border-bottom: 2px solid #eee;
  padding-bottom: 4px;
  margin-top: 1.5em;
}
```

### H4見出し

少し色を薄くする。

```css
.post-content h4 {
  color: #666;
}
```

## 画像の中央寄せとズーム

記事内画像を中央寄せにする。

```css
.post-content img {
  display: block;
  margin: 1.5em auto;
  border-radius: 6px;

  /*
  クリック可能なことを示すカーソル
  */
  cursor: zoom-in;

  /*
  hoverアニメーション
  */
  transition: transform 0.2s ease;
}
```

マウスを乗せたときに少しだけ拡大する。

```css
.post-content img:hover {
  transform: scale(1.02);
}
```

## コードブロックの見た目

コードブロックの角丸を丸くする。

```css
.post-content pre {
  border-radius: 8px;
  padding: 14px;

  /*
  長いコードは横スクロール
  */
  overflow-x: auto;

  /*
  少しコンパクトに
  */
  font-size: 0.9em;
}
```

コードの行間を調整する。

```css
.post-content pre code {
  line-height: 1.5;
}
```

## 表と引用のデザイン

スマホでも崩れないよう横スクロールに対応する。

```css
.post-content table {
  display: block;
  overflow-x: auto;
  border-collapse: collapse;
}
```

表のセルを調整する。

```css
.post-content th,
.post-content td {
  border: 1px solid #ddd;
  padding: 6px 10px;
}
```

blockquoteを装飾して、
技術ブログでよくある「左ライン + 薄い背景」にする。

```css
.post-content blockquote {
  border-left: 4px solid #6366f1;
  background: #f8fafc;
  padding: 10px 14px;
  border-radius: 4px;
}
```

## まとめ

ブログの見た目を調整すると、見やすくなるのでいいかと思います。

満足感もアップします。

最後に、全体のCSSを置いておきます。

```css
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI",
               "Hiragino Sans", "Noto Sans JP",
               "Yu Gothic UI", sans-serif;
}

.post-content {
  line-height: 1.8;
}

/* =========================
   記事カード
========================= */

.post-entry {
  border-radius: 10px;
  transition: transform 0.15s ease, box-shadow 0.15s ease;
}

.post-entry:hover {
  transform: translateY(-3px);
  box-shadow: 0 6px 20px rgba(0,0,0,0.08);
}


/* =========================
   見出し
========================= */

.post-content h2 {
  border-left: 6px solid #6366f1;
  padding-left: 12px;
  margin-top: 2em;
}

.post-content h3 {
  border-bottom: 2px solid #eee;
  padding-bottom: 4px;
  margin-top: 1.5em;
}

.post-content h4 {
  color: #666;
}


/* =========================
   画像（ズーム対応）
========================= */

.post-content img {
  display: block;
  margin: 1.5em auto;
  border-radius: 6px;

  cursor: zoom-in;
  transition: transform 0.2s ease;
}

.post-content img:hover {
  transform: scale(1.02);
}


/* =========================
   コードブロック
========================= */

.post-content pre {
  border-radius: 8px;
  padding: 14px;
  overflow-x: auto;
  font-size: 0.9em;
}

.post-content pre code {
  line-height: 1.5;
}


/* =========================
   インラインコード
========================= */

.post-content code {
  background: #f3f4f6;
  padding: 3px 6px;
  border-radius: 4px;
}

/* ダークモード */
@media (prefers-color-scheme: dark) {
  .post-content code {
    background: #1f2937;
    color: #e5e7eb;
  }
}


/* =========================
   表
========================= */

.post-content table {
  display: block;
  overflow-x: auto;
  border-collapse: collapse;
}

.post-content th,
.post-content td {
  border: 1px solid #ddd;
  padding: 6px 10px;
}


/* =========================
   引用
========================= */

.post-content blockquote {
  border-left: 4px solid #6366f1;
  background: #f8fafc;
  padding: 10px 14px;
  border-radius: 4px;
}
```

ありがとうございました。