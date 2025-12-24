from fastapi import FastAPI

app = FastAPI()

@app.get("/items")
def get_items():
    return {"method": "GET", "message": "get items"}

@app.post("/items")
def post_items():
    return {"method": "POST", "message": "create item"}

@app.put("/items/{item_id}")
def put_item(item_id: int):
    return {
        "method": "PUT",
        "item_id": item_id,
        "message": "update item"
    }

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {
        "method": "DELETE",
        "item_id": item_id,
        "message": "delete item"
    }
