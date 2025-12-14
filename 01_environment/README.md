# Environment Setup

Linux 環境で FastAPI を学ぶための前提整理。
# 01 Environment Setup

この章では、FastAPI を学ぶ前提として  
**Linux 環境と Python 実行環境を「観察しながら」整理**します。

いきなり FastAPI を書かず、  
「どこで」「どの Python が」「どのように」動くのかを明確にすることが目的です。

---

## 前提環境

- OS：Linux
  - Manjaro / Debian
  - 必要に応じて VM / コンテナ
- Windows 環境は直接使用しない  
  （Windows の場合は Linux VM を使用する）

---

## なぜ環境確認から始めるのか

FastAPI 学習でつまずきやすい原因の多くは、  
**フレームワークではなく「環境の曖昧さ」**にあります。

- Python がどこに入っているかわからない
- system Python と user Python の区別がない
- どの Python で uvicorn が起動しているかわからない

これらを先に整理しておくことで、  
後続の ASGI / uvicorn / FastAPI の理解が一気に楽になるらしい。

---

## Python の確認

まずは、現在の環境をそのまま観察します。

  ```bash
  python3 --version
  which python3
  ```

確認ポイント
- Python のバージョンはいくつか
- Python の実体はどこにあるか
- system 管理か、ユーザー管理か


## pip の確認
  ```bash
  pip --version
  which pip
  ```
確認ポイント
- pip はどの Python に紐づいているか
- system pip か user pip か

## 仮想環境（venv）の作成
このシリーズでは、必ず仮想環境を使用します。
理由：
- system Python を汚さない
- uvicorn / fastapi の実体を明確にする
- EC2 やコンテナ環境と考え方を揃える

  ```bssh
  python3 -m venv fastapi-env
  ```

## 仮想環境を有効化：
  ```bash
  source fastapi-env/bin/activate
  ```

仮想環境有効化後の確認
  ```bash
  which python
  python --version
  ```

**観察ポイント**
Python のパスが fastapi-env 配下に変わっているか

以降、この環境でインストールしたものは
このディレクトリ内に閉じる

この時点で理解しておきたいこと
Python は「1つ」ではない

**uvicorn / fastapi は どの Python に入れたか がすべて**

仮想環境は「面倒な作業」ではなく 状況を単純化するための道具

次のステップ
次の章では、FastAPI ではなく
uvicorn（ASGI サーバ）そのものを先に扱います。

- uvicorn は何者か
- 何を起動しているのか
- どのポートを開いているのか

