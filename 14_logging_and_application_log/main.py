import logging
from fastapi import FastAPI, Request

# 章では「まず動く」こと優先（本格運用の設定は後の章へ）
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)

logger = logging.getLogger(__name__)

app = FastAPI(title="14 Logging and Application Log")


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info("request start method=%s path=%s", request.method, request.url.path)
    response = await call_next(request)
    logger.info("request end   status_code=%s", response.status_code)
    return response


@app.get("/")
def root():
    logger.info("root called")
    return {"message": "Hello logging"}


@app.get("/warn")
def warn():
    logger.warning("this is a warning sample")
    return {"message": "warning logged"}


@app.get("/error")
def error():
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("division by zero occurred")
    return {"message": "exception logged"}
