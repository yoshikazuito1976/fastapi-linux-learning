# 09 Path / Query / Body を観察する

この章では、FastAPI が **どこから値を受け取っているのか**を整理します。

HTTP リクエストの主な入力元は次の 3 つです。

- Path Parameter
- Query Parameter
- Request Body

---

## この章のゴール

- Path / Query / Body の違いを説明できる
- 値が「どこから来ているか」を意識してコードを書ける
- 次章（Validation）の理解につなげる

---

## Path Parameter

```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```
```
curl http://127.0.0.1:8000/items/10
```
### 観察
- 値は URL の一部
- 型ヒントで自動変換される
---
## Query Parameter
```python
@app.get("/search")
def search(q: str | None = None):
    return {"query": q}
```
```
curl "http://127.0.0.1:8000/search?q=fastapi"
```

### 観察
- ?key=value 形式
- 省略可能かどうかは定義で決まる
---
## Request Body
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: int

@app.post("/items")
def create_item(item: Item):
    return item
```
```
curl -X POST http://127.0.0.1:8000/items \
  -H "Content-Type: application/json" \
  -d '{"name":"apple","price":100}'
```
### 観察
- Body は URL に見えない
- JSON → Python オブジェクトに変換される
---
## Path / Query を同時に使う
```python
@app.get("/test/{value}")
def test(value: int, q: int):
    return {"value": value, "q": q}
```
```
curl "http://127.0.0.1:8000/test/10?q=20"
```

### 観察
- 同じ型でも取得元で区別される

## まとめ

- 入力元は Path / Query / Body に分かれる
- FastAPI は定義から自動で判別している
- 入力を理解すると、次章のエラーが自然に分かる
