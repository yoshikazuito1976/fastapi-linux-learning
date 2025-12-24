## 08_http_methods_overview  
### HTTPメソッドは「操作」ではなく「意思表示」

この章では、HTTPメソッドを

- 「GETは取得、POSTは送信」
といった**操作手順**としてではなく、
- **クライアントがサーバーに伝える“意思表示”**

として理解することを目的とします。

FastAPIは「魔法のフレームワーク」ではなく、  
HTTPという仕組みの上に成り立っています。  
そのため、HTTPメソッドの意味を理解することは  
API全体を理解するための重要な基礎になります。

---

### この章でできるようになること

- HTTPメソッドの役割を自分の言葉で説明できる
- 同じURLでも、メソッドが違えば意味が変わることを理解できる
- curlでメソッドを切り替えたときの挙動の違いを観察できる
- 「この処理はGETでよいのか？」とAPI設計を考えられる

---

### HTTPメソッドとは何か

HTTPメソッドは、  
**サーバーに対して「何をしたいか」を伝える手段**です。

- URL：対象（何に対して）
- メソッド：意図（どうしたいか）

URLだけでは意味は決まりません。  
**URLとHTTPメソッドの組み合わせ**によって、  
APIの意味が決まります。

---

### 代表的なHTTPメソッド（最小限）

この教材では、以下の4つに絞って扱います。

| Method | 意味 | ポイント |
|------|----|----|
| GET | 情報を取得したい | 副作用がない |
| POST | 新しく作りたい／送信したい | 副作用がある |
| PUT | 上書きしたい | 何度実行しても同じ結果 |
| DELETE | 削除したい | 何度実行しても同じ結果 |

※ PATCH や OPTIONS などは扱いません  
※ 用語（safe / 冪等）は深入りせず、挙動の理解を重視します

---
---

### サンプルアプリ（app.py）

この章では、HTTPメソッドの違いを観察するために  
**最小構成の FastAPI アプリ**を使用します。

以下の `app.py` を作成してください。

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return {"method": "GET", "message": "get items"}

@app.post("/items")
def post_items():
    return {"method": "POST", "message": "create item"}

@app.put("/items/{item_id}")
def put_item(item_id: int):
    return {
        "method": "PUT",
        "item_id": item_id,
        "message": "update item"
    }

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {
        "method": "DELETE",
        "item_id": item_id,
        "message": "delete item"
    }
```
### アプリの起動

以下のコマンドでアプリを起動します。
```
uvicorn app:app --reload
```

起動後、http://localhost:8000 でアクセスできます。

### Swagger UI について

FastAPI は、自動的に **Swagger UI** を提供します。

アプリを起動した状態で、以下のURLにアクセスしてください。
```
http://localhost:8000/docs
```
---
### 同じURLでも意味は変わる

例：`/items`

- `GET /items`  
  → 一覧を取得したい
- `POST /items`  
  → 新しいデータを追加したい
- `PUT /items/1`  
  → ID=1 のデータを上書きしたい
- `DELETE /items/1`  
  → ID=1 のデータを削除したい

**URL × HTTPメソッド = APIの意味**  
という考え方が重要です。

---

### 観察してみよう（curl）

#### GETの場合

```bash
curl -v http://localhost:8000/items
```
- status code はいくつか
- response body はどうなっているか
- サーバーログには何が出ているか

#### POSTの場合
```bash
curl -v -X POST http://localhost:8000/items
```
- GETとの違いは何か
- status code は変わったか
- ログの出方はどう違うか

**コードを書く前に、通信の挙動** を観察することを重視します。

### FastAPIとの対応関係

FastAPIでは、HTTPメソッドごとに処理を分けて定義します。
```
@app.get("/items")
def read_items():
    ...

@app.post("/items")
def create_item():
    ...

```
- URLは同じ
- HTTPメソッドが違う
- 実行される関数が違う

FastAPIは、HTTPの仕組みをそのままコードとして書けるだけのフレームワークです。

### なぜHTTPメソッドを意識するのか
HTTPメソッドを意識できるようになると：
- status code の意味が分かる
- エラーの理由を説明できる
- API設計が「雰囲気」ではなくなる
- 他人のAPI仕様が読みやすくなる

### この章のまとめ
- HTTPメソッドは「操作」ではなく意思表示
- URLだけではAPIの意味は決まらない
- URL × HTTPメソッドで意味が決まる
- FastAPIはHTTPの考え方をそのまま書いている

