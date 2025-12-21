# 06 POST を呼び出す：Swagger / curl / HTTPリクエストの作り方

この章では、FastAPI の `POST` エンドポイントを **「どう呼び出すか」** に焦点を当てます。  
`@app.post()` を書けても、実際にクライアントから呼び出して動かせないと理解が定着しません。

`05_endpoint_Basics` では、`GET` と `POST` が同じパス（例：`/items`）でも別物であることを体験しました。  
この章では、`POST /items` を **Swagger UI（/docs）** と **curl** の両方で呼び出して、HTTPリクエストの基本形を身につけます。

---

## この章のゴール

- `POST` は「ブラウザでURLを開くだけ」では呼べないことを理解します
- Swagger UI（/docs）で `POST` を実行できることを確認します
- `curl` で `POST` を作れるようになります（最低限の型を覚えます）
- `curl` と `wget` の役割の違いを、API学習の観点で整理します

---

## 前提

- FastAPI アプリは `uvicorn main:app --reload` で起動できる状態にします
- 例として `/items` に `GET` と `POST` がある状態を想定します

例：

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return {"method": "GET"}

@app.post("/items")
def create_item():
    return {"method": "POST"}
```

1. GET はブラウザで呼べますが、POST は基本的に呼べません

ブラウザで http://127.0.0.1:8000/items を開くと GET /items が呼ばれます。
しかし、同じURLを開いても POST /items は呼ばれません。

これは、ブラウザの「URLバーからのアクセス」が基本的に GET だからです。
（フォーム送信などは例外ですが、学習の最初は「URLバー = GET」1. GET はブラウザで呼べますが、POST は基本的に呼べません



2. Swagger UI（/docs）で POST を呼び出します

FastAPI は OpenAPI に対応しており、/docs に Swagger UI が表示されます。

Swagger UI: http://127.0.0.1:8000/docs

OpenAPI定義: http://127.0.0.1:8000/openapi.json

## 手順（Swagger UI）

- /docs を開きます
- POST /items を探します
- Try it out を押します
- Execute を押します
- Response の内容と Status code を確認します

## 確認ポイント

- 「POST をどう送るか」が視覚的に理解できます
- curl のサンプルが自動表示されます（ここが非常に強力です）

3. curl で POST /items を呼び出します（ボディなし）

まずは「ボディ無し」の最小形から始めます。
```
curl -X POST http://127.0.0.1:8000/items
```

## 確認ポイント：

- -X POST で HTTPメソッドを指定しています
- URL は同じでも、GET と POST は別の操作です

4. curl で JSON を送る（ボディあり）

次に、POST らしい「データ送信」を行います。
FastAPI 側のコードは、次のように JSON を受け取る形にします。

```
#main.py

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str

@app.post("/items")
def create_item(item: Item):
    return {"received": item}
```
```
uvicorn app:app
```

このとき、curl は次のようになります。
```
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"apple"}'
```

## 確認ポイント：

- -H "Content-Type: application/json" は「これはJSONです」という宣言です
- -d は送信データ（リクエストボディ）です
- JSON の引用符（"）に注意します（最初はここで詰まりやすいです）

### JSON が壊れている場合のエラー例

POST リクエストで送信する JSON の形式が正しくない場合、
FastAPI はエラーを返します。

以下は、文字列のクォートが閉じられていない例です。

```bash
-d '{
  "name": "apple
}'
```

5. curl と wget の違い（API学習の観点）

どちらもHTTP通信を行えますが、得意分野が違います。

- wget は「ファイルを取ってくる（ダウンロード）」が得意です
- curl は「HTTPリクエストを自由に組み立てる」のが得意です

API学習では、

- メソッド（GET/POST/PUT/DELETE）
- ヘッダ（Content-Type, Authorization など）
- ボディ（JSON など）

を扱いたいので、基本は curl を使うのが適しています。と覚えておけば十分です。

