# 07 Request / Response を観察する

この章では、FastAPI が **どのような HTTP Request を受け取り、  
どのような HTTP Response を返しているのか** を観察します。

これまでの章では、
- GET / POST を書く
- curl で API を叩く

といった「使い方」を学んできました。

この章の目的は **APIの正体を理解すること** です。

---

## この章のゴール

- HTTP Request の中身を確認できる
- FastAPI の Request オブジェクトを使える
- Response の status code を意識して返せる
- curl を使って HTTP のやり取りを観察できる

---

## なぜ Request / Response を観察するのか

FastAPI は「魔法のフレームワーク」ではありません。  
HTTP という仕組みの上に成り立っています。

Request / Response を理解すると、次のようなことが
**一本の線でつながる** ようになります。

- エラー（400 / 404 / 500）
- ログ
- セキュリティ
- クラウド（ALB / API Gateway など）

---

## サンプルコード

```python
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/inspect")
async def inspect(request: Request):
    return {
        "method": request.method,
        "url": str(request.url),
        "headers": dict(request.headers),
        "client": request.client.host if request.client else None,
    }

@app.get("/status")
def status_demo():
    return JSONResponse(
        status_code=201,
        content={"message": "created"}
    )
```
---
## 演習1：Request を観察する

以下のコマンドを実行してください。
```
curl -i http://localhost:8000/inspect
```

** 確認するポイント ** ：

- HTTPメソッドは何か
- headers には何が含まれているか
- User-Agent はどこから来ているか

## 演習2：Response の status code を確認する
```
curl -i http://localhost:8000/status
```

** 確認するポイント ** ：
- status code はいくつか
- なぜ 200 ではないのか

## まとめ
- FastAPI は HTTP の上で動いている
- API は「叩ける」だけでなく「理解する」ことが重要

Request / Response を観察できることは、実務で強い武器になる

eated"}
    )
