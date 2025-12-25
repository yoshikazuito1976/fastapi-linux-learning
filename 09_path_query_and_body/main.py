# 08_path_query_and_body/main.py
#
# 起動:
# uvicorn main:app --reload --log-config ../util/logging.conf
#
# 動作確認:
# curl -i http://127.0.0.1:8000/items/10
# curl -i "http://127.0.0.1:8000/search?q=fastapi"
# curl -i -X POST http://127.0.0.1:8000/items \
#   -H "Content-Type: application/json" \
#   -d '{"name":"apple","price":100}'
# curl -i "http://127.0.0.1:8000/test/10?q=20"

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="09_path_query_and_body")


class Item(BaseModel):
    name: str
    price: int


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """Path Parameter"""
    return {"item_id": item_id}


@app.get("/search")
def search(q: str | None = None):
    """Query Parameter"""
    return {"query": q}


@app.post("/items")
def create_item(item: Item):
    """Request Body"""
    return item


@app.get("/test/{value}")
def test(value: int, q: int):
    """Path + Query"""
    return {"value": value, "q": q}

