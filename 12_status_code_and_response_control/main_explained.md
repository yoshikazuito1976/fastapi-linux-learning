# main.py の読み解き

このファイルでは、`main.py` に書かれているコードを通して、

- FastAPI が自動で行っていること
- ユーザーが明示的に制御していること

を整理します。

---

## 全体の構成

`main.py` には、次の5つのエンドポイントがあります。

| エンドポイント | 目的 |
|---------------|------|
| `/auto` | FastAPI に Response を任せる例 |
| `/create` | status_code だけを指定する例 |
| `/custom-response` | Response を自分で返す例 |
| `/bad-request` | HTTPException によるエラー |
| `/items` | バリデーションエラー（422）の確認 |

---

## 1. FastAPI に Response を任せる例

```python
@app.get("/auto")
def auto_response():
    return {"message": "handled by FastAPI"}
```
### 何が起きているか

- ユーザーは dict を返しているだけ

- Status Code は指定していない

- Header も指定していない

### 実際の Response

- Status Code：200 OK

- Content-Type：application/json

- Body：JSON に変換された dict

**👉 Response の生成を FastAPI に任せている状態**
---
## 2. status_code を明示的に指定する例
```python
@app.post("/create", status_code=201)
def create_item():
    return {"message": "resource created"}
```

### ポイント

- Response は FastAPI が生成

- ただし Status Code だけはユーザーが指定

👉
**「全部任せる」から「一部だけ制御する」** への第一歩。
---
## 3. Response を自分で返す例
```python
@app.get("/custom-response")
def custom_response():
    return JSONResponse(
        status_code=202,
        content={"message": "accepted"}
    )
```

### ポイント

- JSONResponse を直接返している

- Status Code も Body もユーザーが制御

** Response の責務が FastAPI からユーザー側に移っている ** 

この感覚は、次の章（Header / Cookie）につながります。
---
## 4. HTTPException によるエラー表現
```python
@app.get("/bad-request")
def bad_request():
    raise HTTPException(
        status_code=400,
        detail="bad request example"
    )
```
### ポイント

- エラーは「返す」のではなく「例外として投げる」

- FastAPI がエラー用 Response を生成する

👉
正常系と異常系を明確に分離できる 
---
## 5. FastAPI が自動で返す 422 エラー
```python
@app.get("/items")
def get_item(limit: int):
    return {"limit": limit}
```
```bash
curl "http://localhost:8000/items?limit=abc"
```

### 起きていること

- limit は int と宣言されている

- "abc" は int に変換できない

FastAPI が自動で 422 Response を返す

👉
型ヒントがルールとして機能している例
---
## まとめ：この main.py で伝えたいこと

- ユーザーは「返り値」を書く

- FastAPI は「Response」を組み立てる

- 制御したくなったら、明示的に書く

この境界線を意識できると、
FastAPI の理解が一段深くなります。
