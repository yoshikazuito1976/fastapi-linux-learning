# 03 FastAPI Basics

この章では、いよいよ **FastAPI** を扱います。

ただし、この章の目的は  
「FastAPIを使えるようになること」そのものではありません。

FastAPIを、

- 何のために使うのか
- どの立ち位置の技術なのか
- どこまで理解すれば十分なのか

を整理しながら、  
**目的達成のための手段として位置づける**ことを目指します。

---

## なぜ FastAPI を学ぶのか

FastAPI は、Python で API を作成するためのフレームワークです。

しかし、実務やプロジェクトにおいて重要なのは、

- FastAPI が書けること  
ではなく、
- FastAPI を使って **何を実現するか**

です。

この章では、FastAPI を  
「ゴール」ではなく  
**「道具」**として扱います。

---

## FastAPI の立ち位置

前の章で確認した通り、

- uvicorn は ASGI サーバ
- FastAPI は ASGI アプリケーション

という関係にあります。

構造としては、次のようになります。

```text
[Client]
   ↓
[uvicorn (ASGIサーバ)]
   ↓
[FastAPI (ASGIアプリ)]
```

FastAPI 自体が通信を受け取っているわけではなく、
uvicorn によって呼び出されているアプリケーションであることを意識してください。

最小の FastAPI アプリを作成する
まずは、最小構成の FastAPI アプリを作成します。

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}
```

このコードでは、次のことだけを行っています。

- FastAPI アプリケーションを作成する
- ルート (/) に対する GET リクエストを定義する
- JSON を返す

## uvicorn で FastAPI を起動する
FastAPI は単体では動作しません。
前章と同様に、uvicorn を使って起動します。

```bash
uvicorn main:app
```
ここで重要なのは、
起動しているのは uvicorn であるという点です。
**FastAPI は、uvicorn の中で呼び出されているにすぎません。**

## FastAPI が提供している価値
FastAPI の本当の価値は、次の点にあります。
- ASGI アプリを 簡潔に書ける
- ルーティングが明確
- 自動で OpenAPI / Swagger UI を生成する
- 型ヒントを活用できる

これらはすべて、
**「APIを安全に、迷いにくく作るための支援」** です。

## この章で押さえておきたいこと
この時点では、次の理解で十分です。
- FastAPI は ASGI アプリケーションである
- uvicorn が実行主体である
- FastAPI は API を書きやすくするための道具である
- FastAPI を使うこと自体が目的ではない
