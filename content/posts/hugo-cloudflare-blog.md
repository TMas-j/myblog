---
title: "Hugo + Cloudflare Pagesでブログを公開するまでの記録"
date: 2026-02-26
draft: false
tags: ["hugo", "cloudflare", "wsl", "blog", "github"]
categories: ["技術"]
---

## はじめに

静的サイトでブログを作ってみたいと思い、Hugoを使って構築し、最終的にCloudflare Pagesで公開するまでをやってみた。

そのセットアップの記録。

---

## やりたかったこと

- シンプルなデザイン
- Markdownで記事を書きたい
- GitHubと連携したい
- 無料で公開したい
- Cloudflareを使ってみたい

---

## 開発環境

- WSL (Ubuntu)
- Hugo（extended版）
- テーマ：PaperMod
- GitHub
- Cloudflare Pages

---

## ① Hugoのセットアップ

まずはHugoをインストール。

https://github.com/gohugoio/hugo/releases/を参考に最新版(v0.157.0)を使用。

```bash
wget https://github.com/gohugoio/hugo/releases/download/v0.157.0/hugo_extended_0.157.0_linux-amd64.deb
dpkg -i hugo_extended_0.157.0_linux-amd64.deb
```

version確認

```bash
$ hugo version
hugo v0.157.0-7747abbb316b03c8f353fd3be62d5011fa883ee6+extended linux/amd64 BuildDate=2026-02-25T16:38:33Z VendorInfo=gohugoio
```

新規サイト作成

```bash
hugo new site myblog
cd myblog
```

---
### ※ 注意

最初、aptでインストールしたが、Hugo(v0.123.7)がインストールされてしまい、
後述のPaperModの要求バージョン(v0.146.0以上)を満たさなかったので注意。

```bash
$ sudo apt install hugo
$ hugo version
hugo v0.123.7+extended linux/amd64 BuildDate=2025-07-18T03:41:49Z VendorInfo=ubuntu:0.123.7-1ubuntu0.3
$ hugo server -D
WARN Module "PaperMod" is not compatible with this Hugo version: Min 0.146.0;
```

---

## ②テーマ導入（PaperMod）

hugo公式ではテーマがたくさん紹介されている。

https://themes.gohugo.io/

今回はシンプルなページを目指したので、PaperModのテーマを使用した。

```bash
git submodule add https://github.com/adityatelange/hugo-PaperMod themes/PaperMod
```

ローカルで動作確認。

```bash
hugo server -D
```

http://localhost:1313 での表示確認できた。


---

## ③ デザイン調整

hugo.tomlを編集して、
- タグ管理を有効化
- ダークモード対応
- シンプルなレイアウトに調整

---

## ④ GitHubへアップロード

GitHubでリポジトリ作成して、pushする。

```bash
git add .
git commit -m "initial commit"
git branch -M main
git remote add origin https://github.com/username/myblog.git
git push -u origin main
```

## ⑤ Cloudflare Pagesで公開

Cloudflare Pagesで公開するために、以下の順で設定する。

- Cloudflareのアカウントを作成して、Consoleにアクセスする
- 左メニューの 「ビルド→Workers & Pages」 を選ぶ
- 右上の 「+ 追加」 から 「Pages」 を選ぶ
- 「既存の Git リポジトリをインポートする」を選ぶ
- (GitHubの連携をしたあと、) 先ほどのGitHubリポジトリを選択する
- アプリケーションビルドとデプロイのセットアップ
  - プロダクションブランチ: main
  - フレームワーク プリセット: Hugo
  - ビルとコマンド: hugo
  - ビルド出力ディレクトリ: public

デプロイすると、URLが発行されてアクセスできるようになる。

hugo.toml の baseUrl を本番URLに変更して再push。

## 感想

ローカルで動いたときも嬉しかったけど、本番URLが発行された瞬間はやっぱりテンションが上がった。

「自分のサイトがインターネット上にある」という感覚は特別。

思っていたより構築はシンプルで、

- Markdownで書ける
- Git pushで自動公開
- 無料で運用できる

というのはかなり便利。

## 今後やりたいこと

- favicon追加
- OGP設定
- 記事をどんどん書く

とりあえず今日はここまで。

まずは公開できたことに満足。

ありがとうございました。