# 02 uvicorn Basics

この章では、FastAPI を書く前に  
**uvicorn（ASGI サーバ）そのもの**を主役として扱います。

## ASGIサーバとは？

ASGI（Asynchronous Server Gateway Interface）は、  
**Python アプリケーションと Web サーバをつなぐための仕様**です。

従来の Python Web では、**WSGI（Web Server Gateway Interface）** という仕様が主に使われてきました。  
ASGI はその **後継・拡張** にあたります。

---

## WSGI と ASGI の違い（概要）

| 項目 | WSGI | ASGI |
|---|---|---|
| 同期処理 | ○ | ○ |
| 非同期処理 | ✕ | ○ |
| WebSocket | ✕ | ○ |
| HTTP/2 | ✕ | ○ |
| 主な用途 | 従来型Web | モダンWeb / API |

ASGI は **非同期処理を前提**として設計されており、

- 同時接続が多い API
- WebSocket
- リアルタイム通信

といった用途に向いています。

## ASGIサーバの役割

ASGIサーバ（uvicorn など）は、次の役割を担います。

- HTTPリクエストを受信する
- WebSocket接続を管理する
- 非同期イベントループを管理する
- ASGIアプリケーションを呼び出す

重要なのは次の点です。

> **ASGIサーバは「実行環境」であり、  
> アプリケーションそのものではない**

## FastAPI と ASGI の関係

FastAPI は **ASGIアプリケーション**です。

- FastAPI = ASGI仕様に従ったアプリ
- uvicorn = ASGIサーバ（実行主体）

この2つを組み合わせることで、

```text
[Client]
   ↓
[uvicorn (ASGI server)]
   ↓
[FastAPI (ASGI app)]
```
FastAPI は「アプリ」であり、  
**実際にプロセスとして起動し、ポートを開いているのは uvicorn** です。

---

## なぜ uvicorn から始めるのか

FastAPI 学習で混乱が起きやすい理由の一つは、

- FastAPI が何をしているのか
- uvicorn が何をしているのか
- Web サーバ（nginx / Apache）と何が違うのか

が **混ざったまま進んでしまう**ことにあります。

この章では、

- FastAPI = アプリ
- uvicorn = 実行主体（ASGI サーバ）

という役割分担を、  
**Linux のプロセス・ポート視点で確認**します。

---

## uvicorn とは何か

- **ASGI サーバ**
- Python で書かれた Web サーバ
- ASGI アプリ（FastAPI など）を実行する役割

重要なのは次の一点です。

> **FastAPI は uvicorn によって起動されている**

---

## uvicorn のインストール

まずは仮想環境が有効になっていることを確認します。

```bash
which python
```
次に uvicorn をインストールします。

```bash
pip install uvicorn
```
確認：
```bash
which uvicorn
```
確認ポイント
- uvicorn はどこにインストールされたか
- system Python ではなく、仮想環境配下になっているか

## 最小の ASGI アプリを用意する

FastAPI は まだ使いません。
ASGI アプリとして最小のものを用意します。
```
# app.py
async def app(scope, receive, send):
    assert scope["type"] == "http"

    await send({
        "type": "http.response.start",
        "status": 200,
        "headers": [(b"content-type", b"text/plain")],
    })
    await send({
        "type": "http.response.body",
        "body": b"Hello from ASGI",
    })
```

uvicorn で起動する
```
uvicorn app:app
```

ブラウザで以下にアクセスします。

http://127.0.0.1:8000

## ここで起きていること

この時点で起きているのは：
- uvicorn プロセスが起動している
- ポート 8000 を LISTEN している
- HTTP リクエストを受け取っている
- ASGI アプリ（app）を呼び出している

## プロセスの確認

```
ps aux | grep uvicorn
```

または：

```
pstree -p | grep uvicorn
```

観察ポイント
- uvicorn が Linux プロセスとして存在している
- FastAPI（まだ使っていない）はプロセスではない

ポートの確認
```
ss -ltnp | grep 8000
```
観察ポイント
- ポート 8000 を LISTEN しているのは誰か
- uvicorn が Web サーバとして振る舞っていること

uvicorn と Web サーバの違い（整理）
|項目|	uvicorn|nginx / Apache|
|HTTP受信|○|○|
|Python実行|○|✕|
|ASGI対応|○|✕|
|FastAPI実行|○|✕|

※ nginx / Apache は 別の役割
（リバースプロキシ・静的配信など）

## この章で理解しておきたいこと
- FastAPI は 単体では動かない
- uvicorn が 実行主体
- uvicorn は Python製 Web サーバ
- Linux 的には「1つのプロセス」として扱える
