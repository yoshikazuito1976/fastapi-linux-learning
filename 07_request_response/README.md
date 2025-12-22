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
