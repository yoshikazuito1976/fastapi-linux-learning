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

## uv について（推奨）

この教材では、Python のパッケージ管理・仮想環境ツールとして  
**uv** の利用を推奨します。

`uv` は Rust 製の高速なツールで、以下の特徴があります。

- `pip` / `venv` と互換性がある
- 依存関係の解決やインストールが高速
- どの Python 環境を使っているかを明確にしやすい

なお、従来どおり `pip` と `venv` を使って進めることも可能です。  
ここでは「なぜ uv を使うのか」を意識しながら導入します。

## uv のインストール（Linux / WSL）

以下のコマンドで `uv` をインストールします。

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```
インストール後、シェルを再読み込みし、
正しくインストールされたか確認してください。

```bash
uv --version
```
## 仮想環境の作成（uv・推奨）

以下のコマンドで仮想環境を作成します。

```bash
uv venv fastapi-env
```

仮想環境を有効化します。
```bash
source fastapi-env/bin/activate
```

## 仮想環境（venv）の作成
このシリーズでは、必ず仮想環境を使用します。現時点では上記のuvを使った環境を推奨しますが、下記の従来型でも問題ありません。
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

