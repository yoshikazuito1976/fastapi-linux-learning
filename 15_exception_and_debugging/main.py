from fastapi import FastAPI, HTTPException
import logging

# --------------------------------------------------
# Logging 設定
# --------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s : %(message)s"
)

logger = logging.getLogger(__name__)

# --------------------------------------------------
# FastAPI アプリケーション
# --------------------------------------------------
app = FastAPI()

# --------------------------------------------------
# ルートエンドポイント
# --------------------------------------------------
@app.get("/")
def root():
    logger.info("root endpoint called")
    return {"message": "Exception and Debugging chapter"}

# --------------------------------------------------
# 正常系の例
# --------------------------------------------------
@app.get("/add")
def add(a: int, b: int):
    logger.info("add called: a=%s, b=%s", a, b)
    return {"result": a + b}

# --------------------------------------------------
# 例外を明示的に発生させる例
# --------------------------------------------------
@app.get("/divide")
def divide(a: int, b: int):
    logger.info("divide called: a=%s, b=%s", a, b)

    if b == 0:
        logger.error("division by zero attempted")
        raise HTTPException(
            status_code=400,
            detail="division by zero is not allowed"
        )

    return {"result": a / b}

# --------------------------------------------------
# 想定外の例外が発生する例
# --------------------------------------------------
@app.get("/crash")
def crash():
    logger.info("crash endpoint called")
    # ZeroDivisionError を意図的に発生させる
    return {"result": 1 / 0}
