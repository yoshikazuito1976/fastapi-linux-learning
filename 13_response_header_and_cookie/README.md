# 13 Response Header and Cookie

この章では、FastAPI における **レスポンスの制御** をテーマに、  
**Response Header** と **Cookie** を通して HTTP の振る舞いを観察します。

これまでの章では「リクエストを受け取り、レスポンスボディを返す」ことに注目してきましたが、  
Web アプリケーションにおいては **ボディ以外の情報** も非常に重要です。

本章では、  
「FastAPI は *何を返しているのか*」  
「その情報は *どこを通って* クライアントに届いているのか」  
を意識しながら学習を進めます。

---

## この章でわかること

- レスポンスは **Body だけで構成されているわけではない** こと
- Response Header によって、サーバーは追加情報を返せること
- Cookie は **レスポンスヘッダーとして送信される** こと
- Cookie は「サーバーが覚える仕組み」ではないこと
- HTTP が **ステートレス** と呼ばれる理由の入り口

---

## 主なトピック

### Response Header
- `Response` オブジェクトを使ったヘッダー操作
- カスタムヘッダーの付与
- curl を使ったレスポンスヘッダーの確認

### Cookie（Set-Cookie）
- `response.set_cookie()` による Cookie の送信
- Cookie がレスポンスヘッダーに含まれることの確認
- ブラウザ（クライアント）側で保持される仕組み

### Cookie の受け取り
- `Cookie()` 依存関係を使った値の取得
- 未設定時の挙動
- リクエストヘッダーとの関係

---

## 学習のポイント

この章の目的は、  
**Cookie の使い方を暗記することではありません。**

重要なのは、

- HTTP では  
  - リクエストにもヘッダーがあり  
  - レスポンスにもヘッダーがある
- Cookie はその **ヘッダーを通して往復している**
- FastAPI は「Web の仕組みを操作するための道具」である

という視点を持つことです。

---

## 構成

```text
13_response_header_and_cookie/
├── main.py        # サンプルコード
├── concepts.md    # この章の概念整理
└── README.md
```
---
### 起動
```bash
uvicorn main:app --reload
```

### 1) ヘッダー付与の確認
```bash
curl -i http://127.0.0.1:8000/headers
```
### 2) Cookie をセット（Set-Cookie がレスポンスヘッダーに出る）
```bash
curl -i http://127.0.0.1:8000/cookies/set
```

### 3) Cookie を送って取得（リクエストヘッダーとして送る）
```bash
curl -i --cookie "session_id=abc123" http://127.0.0.1:8000/cookies/get
```

### 4) Cookie 削除
```bash
curl -i http://127.0.0.1:8000/cookies/clear
```