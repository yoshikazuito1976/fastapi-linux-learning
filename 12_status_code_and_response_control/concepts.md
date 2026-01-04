# Status Code と Response の考え方

この章では、FastAPI が返している **HTTP Response の意味**を整理します。

FastAPI は多くの処理を自動で行ってくれますが、  
その裏側では **HTTP Response** が必ず返されています。

このファイルでは、

- Status Code とは何か
- FastAPI でどう扱われているか
- なぜ制御する必要があるのか

を順に整理します。

---

## 1. HTTP Response とは何か

HTTP Response は、主に次の情報を持っています。

- Status Code（状態）
- Header（付加情報）
- Body（中身のデータ）

これまでの章では、  
主に **Body（JSONの中身）** に注目してきました。

この章では、特に **Status Code** に注目します。

---

## 2. HTTP Status Code の役割

HTTP Status Code は、

> 「このリクエストは、どういう結果だったのか」

を **機械的に伝えるための情報**です。

人間向けのメッセージではなく、  
**クライアント（プログラム）が判断するための情報**です。

---

## 3. Status Code の基本的な分類

すべてを覚える必要はありません。  
まずは次の分類を押さえます。

| クラス | 意味 | 例 |
|------|------|----|
| 2xx | 成功 | 200 OK, 201 Created |
| 4xx | クライアント側の問題 | 400, 404, 422 |
| 5xx | サーバー側の問題 | 500 |

この教材では、主に **2xx と 4xx** を扱います。

---

## 4. よく使う Status Code

### 200 OK
- 正常に処理が完了した
- FastAPI のデフォルト

```python
@app.get("/ok")
def ok():
    return {"message": "success"}
```
---
### 201 Created

新しいリソースが作成された
```python
@app.post("/items", status_code=201)
def create_item():
    return {"message": "created"}
```
---
### 400 Bad Request

リクエストの内容が不正
```python
from fastapi import HTTPException

raise HTTPException(
    status_code=400,
    detail="bad request"
)
```
---
### 404 Not Found

指定されたリソースが存在しない
```python
from fastapi.responses import JSONResponse

return JSONResponse(
    status_code=404,
    content={"error": "not found"}
)
```
---
## 5. FastAPI が自動でやっていること

FastAPI は、次のような処理を 自動で行っています。

- dict を返す → JSON Response を作成
- バリデーションエラー → 422 を返す
- 型に合わない入力 → エラー Response を返す

つまり、

「Response を書いていない」

のではなく、

「FastAPI に任せている」
状態です。

---
## 6. Response を自分で返すということ
dict を返す場合
```python
return {"message": "ok"}
```

- FastAPI が Response を作る
- Status Code は基本的に 200

Response を返す場合
```python
from fastapi.responses import JSONResponse

return JSONResponse(
    status_code=404,
    content={"message": "not found"}
)
```

- Status Code を自分で指定できる
- Header なども制御できる

7. 「返り値」と「Response」は別物

ここが重要なポイントです。

書き方	意味
dict を返す	FastAPI に Response を作らせる
Response を返す	開発者が Response を制御する

この違いを理解しておくと、
次の章（Header / Cookie / Logging）が一気につながります。

8. エラーは「例外」で表現する

FastAPI では、エラーを 例外（Exception） として表現します。

raise HTTPException(
    status_code=404,
    detail="item not found"
)


処理を途中で止める

明確な Status Code を返す

エラーの意味をはっきりさせる

9. なぜこの章が重要なのか

Status Code を意識できるようになると、

API の設計が変わる

エラーの扱いが整理される

ログやデバッグがしやすくなる

FastAPI を
「便利な道具」から「制御できるフレームワーク」
として使えるようになります。
