# FastAPI × Linux Learning Log

このリポジトリは、**FastAPI を Linux 環境で学ぶための学習ログ兼、教材化の原型**です。  
フレームワークの使い方だけでなく、**OS・プロセス・ネットワーク視点**から  
「FastAPI がどのように動いているのか」を理解することを目的としています。

---

## このリポジトリの位置づけ

- 個人的な学習ログ（草を生やす 🌱）
- 将来的な教材化・Notion再編集の一次情報
- FastAPI / ASGI / uvicorn の理解を深めるための実験場

> 内容は随時更新・修正されます。  
> 完成されたチュートリアルではありません。

---

## 学習方針

本シリーズでは、以下の方針を重視します。

- **Linux 前提**
  - Manjaro / Debian / VM / コンテナ環境
  - Windows ネイティブ環境は扱わない
- **最小構成から始める**
  - いきなり nginx / systemd / EC2 に行かない
- **OS視点で観察する**
  - プロセス（ps, pstree）
  - ポート（ss）
  - 実行主体は誰か？
- **Why を README に残す**
  - なぜそうなるのか
  - なぜ別の選択肢ではないのか

---

## 学習のゴール

- FastAPI が **単体では動かない**ことを説明できる
- uvicorn が **何者で、何をしているのか**説明できる
- 「EC2 にしたら何が増えるだけなのか」を言語化できる
- Apache / nginx / uvicorn の役割の違いを整理できる

---

## 構成（予定）

```text
.
├── 00_overview/        # 本ページ（全体像・方針）
├── 01_environment/     # Python / venv / Linux 環境確認
├── 02_uvicorn_basics/  # uvicorn の正体と役割
├── 03_fastapi_basics/  # 最小 FastAPI
├── 04_jinja/           # HTML を返す
├── 05_htmx/            # API と HTML の橋渡し
└── notes/              # 思考メモ・雑記

