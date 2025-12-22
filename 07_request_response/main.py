from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Go to /inspect or /status"}

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

