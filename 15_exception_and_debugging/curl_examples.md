# curl Examples – Exception and Debugging

## 目的

- curl を「叩くコマンド」ではなく
- 挙動を観察するための道具として使わせる

このドキュメントでは、[main.py](main.py) に定義された各エンドポイントを curl を使って段階的に観察します。

curl は単なるテストツールではありません。HTTP通信を可視化するための観測装置です。

## 0. 事前準備

FastAPI アプリケーションを起動します。

```bash
uvicorn main:app --reload
```

以降の curl コマンドは、**別ターミナル**から実行してください。

## 1. 何も考えずに `/` を叩く

```bash
curl http://127.0.0.1:8000/
```

### レスポンス

```json
{"message":"Exception and Debugging chapter"}
```

### 観察ポイント

- HTTP ステータスコードは `200 OK`
- JSON がそのまま返ってくる
- ターミナルには INFO ログが出ている: `INFO __main__ : root endpoint called`

## 2. HTTP レスポンスの詳細を見る（`-i`）

```bash
curl -i http://127.0.0.1:8000/
```

### ここで注目する点

- `HTTP/1.1 200 OK`
- `content-type: application/json`

### Body と Header の違い

👉 HTTP は「ヘッダ＋ボディ」で構成されている

## 3. 正常系 `/add`

```bash
curl "http://127.0.0.1:8000/add?a=3&b=5"
```

### レスポンス

```json
{"result":8}
```

### ログ

```
INFO __main__ : add called: a=3, b=5
```

### ポイント

- クエリパラメータが URL に含まれている
- FastAPI が `int` に変換している
- 例外は発生していない

## 4. パラメータ型エラーを起こす

```bash
curl "http://127.0.0.1:8000/add?a=abc&b=5"
```

### レスポンス

```json
{
  "detail": [
    {
      "loc": ["query", "a"],
      "msg": "value is not a valid integer",
      "type": "type_error.integer"
    }
  ]
}
```

### 観察ポイント

- 自分で例外を書いていない
- FastAPI が入力チェックを行っている
- ステータスコードは `422`

👉 バリデーションエラーも例外の一種

## 5. `/divide` 正常系

```bash
curl "http://127.0.0.1:8000/divide?a=10&b=2"
```

### レスポンス

```json
{"result":5.0}
```

### ログ

```
INFO __main__ : divide called: a=10, b=2
```

## 6. 設計された例外 `/divide?a=10&b=0`

```bash
curl "http://127.0.0.1:8000/divide?a=10&b=0"
```

### レスポンス

```json
{"detail":"division by zero is not allowed"}
```

### HTTP ステータスを確認

```bash
curl -i "http://127.0.0.1:8000/divide?a=10&b=0"
```

```
HTTP/1.1 400 Bad Request
```

### ログ

```
ERROR __main__ : division by zero attempted
```

### 重要な点

- 意図したエラー
- レスポンスは JSON
- ログは ERROR
- スタックトレースは出ない

## 7. curl でステータスコードだけ見る

```bash
curl -o /dev/null -w "%{http_code}\n" \
"http://127.0.0.1:8000/divide?a=10&b=0"
```

```
400
```

👉 スクリプトや監視でよく使う形式

## 8. 想定外の例外 `/crash`

```bash
curl http://127.0.0.1:8000/crash
```

### レスポンス

```json
{"detail":"Internal Server Error"}
```

### HTTP ヘッダ

```bash
curl -i http://127.0.0.1:8000/crash
```

```
HTTP/1.1 500 Internal Server Error
```

## 9. ターミナル側の観察（最重要）

ターミナルには**スタックトレース**が表示されます。

```
ZeroDivisionError: division by zero
```

### 読み方のコツ

- 一番下を見る
- `return {"result": 1 / 0}` を探す
- どの関数かを確認する

👉 curl だけでは原因はわからない

## 10. curl とログの役割分担

| 観測対象   | 手段              |
|-----------|-------------------|
| HTTP結果  | curl              |
| ステータス | curl -i           |
| 内部挙動  | logging           |
| 原因特定  | スタックトレース   |

## 11. わざと壊して観察する（推奨）

次を自分で試してみてください。

- `/add?a=1`
- `/divide?b=2`
- `/divide?a=1&b=abc`
- `/crash` を連続で叩く

👉 壊していい環境で壊す

## 12. curl を使う本当の理由

- ブラウザは「優しい」
- curl は「正直」
- HTTP をそのまま見せてくれる

### デバッグとは

見えないものを、見える形にすること

## まとめ

- curl は HTTP 観測ツール
- エラーは挙動の一部
- ログとセットで理解する
- 「慣れる」ことが最大の目的