# 10 Validation and Error Handling を観察する

この章では、FastAPI が **入力値をどう検証しているか** と、  
検証エラーが起きたときに **どんなHTTPレスポンスが返るか** を観察します。

FastAPI の「便利さ」の中核はここです。

---

## この章のゴール

- Path / Query / Body それぞれの検証ポイントを説明できる
- 422 Unprocessable Entity の意味を言語化できる
- `RequestValidationError` を捕まえてレスポンス形式を整えられる
- 「エラーの設計はAPIの設計である」という感覚を持つ

---

## なぜ Validation を観察するのか

API は「正しい入力」だけが来る前提では作れません。

- 不正な型（数字のはずが文字列）
- 範囲外（負の数、長すぎる文字列）
- 必須欠落（required）
- 期待しない形式（メールっぽくない）

これらを **アプリが壊れる前に止める仕組み**が Validation です。

---

## ここで観察すること（視点）

- **どの層が検証している？**
  - FastAPI ？ -> 実際は Pydantic が中心
- **どの入力がどこで検証される？**
  - Path / Query / Body
- **失敗すると何が返る？**
  - status code / body
- **エラーを整形できる？**
  - `@app.exception_handler(RequestValidationError)`

---

## 動かし方

```bash
cd 10_validation_and_error_handling
uvicorn main:app --reload --port 8010
```

## エンドポイント一覧

- GET /items/{item_id}  
Path / Query のバリデーション観察

- POST /users  
Body のバリデーション観察（Field制約 / 独自ルール）

- POST /orders  
ネストしたモデルのバリデーション観察

- GET /errors/demo  
HTTPException と予期しない例外の違い

## 演習アイデア（軽め）

/items/{item_id} に item_id=-1 を渡して、どこで弾かれているか説明してみる

/users に password="123" を入れて、独自バリデーションのエラーを観察する

バリデーションエラーのレスポンスを「自分のAPI標準形式」に整形してみる

