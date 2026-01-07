from __future__ import annotations

from fastapi import Cookie, FastAPI, Response
from fastapi.responses import JSONResponse

app = FastAPI(title="13 Response Header and Cookie")


@app.get("/")
def root() -> dict:
    return {"message": "Hello. Go to /headers or /cookies"}


# ----------------------------
# Response Header
# ----------------------------
@app.get("/headers")
def add_custom_header(response: Response) -> dict:
    """
    Response Header を付与する最小例。
    curl -i で確認すると、X-Example-Header が返る。
    """
    response.headers["X-Example-Header"] = "hello-from-fastapi"
    response.headers["X-Chapter"] = "13_response_header_and_cookie"
    return {"message": "Check response headers with curl -i"}


# ----------------------------
# Cookie (Set-Cookie)
# ----------------------------
@app.get("/cookies/set")
def set_cookie(response: Response) -> dict:
    """
    Cookie をセットする最小例。
    Set-Cookie は「レスポンスヘッダー」として返る。
    """
    response.set_cookie(
        key="session_id",
        value="abc123",
        httponly=True,   # JS から読めない（安全寄り）
        max_age=60 * 10, # 10分（秒）
        samesite="lax",
    )
    return {"message": "Cookie 'session_id' was set (check Set-Cookie header)"}


@app.get("/cookies/get")
def get_cookie(session_id: str | None = Cookie(default=None)) -> dict:
    """
    Cookie を受け取る最小例。
    Cookie はリクエストヘッダーに乗って送られてくる。
    """
    return {
        "message": "Cookie received (or not).",
        "session_id": session_id,
        "hint": "Try: curl -i http://127.0.0.1:8000/cookies/set then curl -i --cookie 'session_id=abc123' http://127.0.0.1:8000/cookies/get",
    }


@app.get("/cookies/clear")
def clear_cookie() -> JSONResponse:
    """
    Cookie を削除する例（レスポンス側で削除指示を返す）。
    """
    res = JSONResponse({"message": "Cookie cleared (delete_cookie sent)."})
    res.delete_cookie("session_id")
    return res
