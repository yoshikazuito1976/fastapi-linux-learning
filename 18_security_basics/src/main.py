from fastapi import FastAPI, Depends, Header, HTTPException
from typing import Annotated

app = FastAPI(title="18_security_basics", version="0.1.0")


def verify_token(x_token: Annotated[str, Header(alias="X-Token")]) -> str:
    """
    学習用の超シンプル認証。
    リクエストヘッダ `X-Token: secret-token` が無い / 間違っていると 401 を返す。
    """
    if x_token != "secret-token":
        raise HTTPException(status_code=401, detail="Invalid token")
    return x_token


@app.get("/")
def health():
    return {"status": "ok", "message": "Try GET /secure with header X-Token: secret-token"}


@app.get("/secure")
def secure_endpoint(token: str = Depends(verify_token)):
    # token には verify_token が返した値が入る
    return {"message": "You are authenticated", "token": token}


# ローカル実行用（python main.py でも起動できる）
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
