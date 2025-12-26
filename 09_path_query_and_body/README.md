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
## FastAPI と Pydantic

FastAPI では、リクエストで受け取る値の多くが  
**Pydantic** を使って検証・変換されている。

- Path Parameter
- Query Parameter
- Request Body

これらはすべて、
**関数定義（型ヒント・デフォルト値）をもとに**
FastAPI が自動的に Pydantic の仕組みを使って処理している。

この章では、Pydantic を「書く」ことはしないが、
**Pydantic が動いている結果**を観察する。
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

#### 値が必須か省略可能かは「定義」で決まる

Query Parameter や Body の値が

- 必須か
- 省略可能か

は、**関数の引数定義**によって決まる。

#### 例：省略できない Query Parameter

```python
@app.get("/test/{value}")
def test(value: int, q: int):
...
q にはデフォルト値がない
→ 必須
→ 省略するとエラーになる


#### 例：省略可能な Query Parameter

```python
@app.get("/search")
def search(q: str | None = None):
...
- q に None を許可
- デフォルト値が None
- → 省略可能

FastAPI はこの定義をもとに、
「この値は必要か？」「なくてもよいか？」を判断している。
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

## Request Body と Pydantic Model
Request Body は、Pydantic の Model として定義する。

```python
class Item(BaseModel):
    name: str
    price: int
```
この定義により、
- 必要なキー（name, price）
- 各キーの型
が決まる。

Body に含まれる JSON は、
この Model に 変換・検証されたうえで関数に渡される。

そのため、

- キーが足りない
- 型が違う

といった場合は、
FastAPI が自動的にエラーを返す。

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

## この章の位置づけ

この章では、

- Pydantic の詳細な書き方
- Validation の制御
- エラー内容のカスタマイズ

は扱わない。

目的は、

**「定義によって挙動が決まっている」ことを理解すること**

であり、
詳細な Validation や Error Handling は次章以降で扱う。
