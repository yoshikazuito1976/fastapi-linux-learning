# requests.md
# 09_path_query_and_body – Error Observation Requests

このファイルでは、**意図的にエラーを発生させるリクエスト**をまとめる。

目的は、  
**Path / Query / Body の違いによって、FastAPI の壊れ方がどう変わるかを観察すること**。

---

## 前提

アプリは以下で起動していること。

```bash
uvicorn main:app --reload --log-config ../util/logging.conf
```
## 1. Path Parameter の型エラー
```bash
curl -i http://127.0.0.1:8000/items/abc
```

### 観察ポイント

Status Code

loc: ["path", "item_id"]

## 2. Query Parameter の型エラー
```bash
curl -i "http://127.0.0.1:8000/test/10?q=abc"
```

### 観察ポイント

loc: ["query", "q"]

-Path は正しいが Query で失敗している

## 3. Query Parameter 不足
```bash
curl -i http://127.0.0.1:8000/test/10
```

### 観察ポイント

Query が存在しないこともエラーになる

loc: ["query", "q"]

## 4. Request Body のキー不足
```bash
curl -i -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"apple"}'
```

### 観察ポイント

loc: ["body", "price"]

## 5. Request Body の型エラー
```bash
curl -i -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"apple","price":"cheap"}'
```

### 観察ポイント

JSON としては正しいが、型が違う

## 6. Content-Type 不一致
```bash
curl -i -X POST http://127.0.0.1:8000/items \
  -d '{"name":"apple","price":100}'
```

### 観察ポイント

Header がない場合の挙動

環境によって 422 / 415 の違い

## メモ

この章では HTTPException は使わない

FastAPI が「何も書かなくても返すエラー」を観察する

エラーの制御・設計は次章で扱う
