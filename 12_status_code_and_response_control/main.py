from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse

app = FastAPI()


# -------------------------
# 1. FastAPI に任せる Response
# -------------------------
@app.get("/auto")
def auto_response():
    """
    dict を返すだけ。
    Status Code や Header は FastAPI が自動生成する。
    """
    return {"message": "handled by FastAPI"}


# -------------------------
# 2. status_code を明示的に指定
# -------------------------
@app.post("/create", status_code=201)
def create_item():
    """
    status_code を指定すると、
    FastAPI がその値を使って Response を生成する。
    """
    return {"message": "resource created"}


# -------------------------
# 3. Response を自分で返す
# -------------------------
@app.get("/custom-response")
def custom_response():
    """
    JSONResponse を直接返す。
    Response の生成をユーザーが制御する。
    """
    return JSONResponse(
        status_code=202,
        content={"message": "accepted and processing"}
    )


# -------------------------
# 4. HTTPException によるエラー
# -------------------------
@app.get("/bad-request")
def bad_request():
    """
    HTTPException を raise すると、
    FastAPI がエラー用の Response を返す。
    """
    raise HTTPException(
        status_code=400,
        detail="bad request example"
    )


# -------------------------
# 5. 入力エラー（FastAPI が自動処理）
# -------------------------
@app.get("/items")
def get_item(limit: int):
    """
    limit が int でない場合、
    FastAPI が自動で 422 Response を返す。
    """
    return {"limit": limit}
