from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

app = FastAPI(title="Todo API", version="1.0.0")

# Pydanticモデル定義
class TodoBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Todoのタイトル")
    description: Optional[str] = Field(None, max_length=500, description="Todoの詳細説明")
    completed: bool = Field(False, description="完了状態")

class TodoCreate(TodoBase):
    pass

class TodoUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    completed: Optional[bool] = None

class Todo(TodoBase):
    id: int = Field(..., description="TodoのID")
    created_at: datetime = Field(..., description="作成日時")
    updated_at: datetime = Field(..., description="更新日時")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "title": "FastAPIを学ぶ",
                "description": "FastAPIのドキュメントを読む",
                "completed": False,
                "created_at": "2026-01-14T12:00:00",
                "updated_at": "2026-01-14T12:00:00"
            }
        }

# インメモリデータベース（本番環境では実際のDBを使用）
todos_db: List[dict] = []
next_id = 1

@app.get("/", tags=["Root"])
async def root():
    """
    ルートエンドポイント - APIの基本情報を返す
    """
    return {
        "message": "Todo API へようこそ！",
        "docs": "/docs",
        "total_todos": len(todos_db)
    }

@app.post(
    "/todos",
    response_model=Todo,
    status_code=status.HTTP_201_CREATED,
    tags=["Todos"],
    summary="新しいTodoを作成"
)
async def create_todo(todo: TodoCreate):
    """
    新しいTodoを作成します。
    
    - **title**: Todoのタイトル（必須、1-100文字）
    - **description**: Todoの詳細説明（オプション、最大500文字）
    - **completed**: 完了状態（デフォルト: False）
    """
    global next_id
    
    now = datetime.now()
    new_todo = {
        "id": next_id,
        "title": todo.title,
        "description": todo.description,
        "completed": todo.completed,
        "created_at": now,
        "updated_at": now
    }
    
    todos_db.append(new_todo)
    next_id += 1
    
    return new_todo

@app.get(
    "/todos",
    response_model=List[Todo],
    tags=["Todos"],
    summary="全てのTodoを取得"
)
async def get_todos(
    completed: Optional[bool] = None,
    skip: int = 0,
    limit: int = 100
):
    """
    全てのTodoを取得します。
    
    - **completed**: 完了状態でフィルタリング（オプション）
    - **skip**: スキップする件数（デフォルト: 0）
    - **limit**: 取得する最大件数（デフォルト: 100）
    """
    filtered_todos = todos_db
    
    if completed is not None:
        filtered_todos = [todo for todo in filtered_todos if todo["completed"] == completed]
    
    return filtered_todos[skip:skip + limit]

@app.get(
    "/todos/{todo_id}",
    response_model=Todo,
    tags=["Todos"],
    summary="特定のTodoを取得"
)
async def get_todo(todo_id: int):
    """
    IDで特定のTodoを取得します。
    
    - **todo_id**: 取得するTodoのID
    """
    for todo in todos_db:
        if todo["id"] == todo_id:
            return todo
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"ID {todo_id} のTodoが見つかりません"
    )

@app.put(
    "/todos/{todo_id}",
    response_model=Todo,
    tags=["Todos"],
    summary="Todoを更新"
)
async def update_todo(todo_id: int, todo_update: TodoUpdate):
    """
    既存のTodoを更新します。
    
    - **todo_id**: 更新するTodoのID
    - **title**: 新しいタイトル（オプション）
    - **description**: 新しい説明（オプション）
    - **completed**: 新しい完了状態（オプション）
    """
    for i, todo in enumerate(todos_db):
        if todo["id"] == todo_id:
            # 更新されたフィールドのみを適用
            update_data = todo_update.model_dump(exclude_unset=True)
            
            if update_data:
                todos_db[i].update(update_data)
                todos_db[i]["updated_at"] = datetime.now()
            
            return todos_db[i]
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"ID {todo_id} のTodoが見つかりません"
    )

@app.delete(
    "/todos/{todo_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    tags=["Todos"],
    summary="Todoを削除"
)
async def delete_todo(todo_id: int):
    """
    特定のTodoを削除します。
    
    - **todo_id**: 削除するTodoのID
    """
    for i, todo in enumerate(todos_db):
        if todo["id"] == todo_id:
            todos_db.pop(i)
            return
    
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"ID {todo_id} のTodoが見つかりません"
    )

@app.get(
    "/todos/stats/summary",
    tags=["Statistics"],
    summary="Todo統計情報を取得"
)
async def get_todo_stats():
    """
    Todoの統計情報を取得します。
    """
    total = len(todos_db)
    completed = len([todo for todo in todos_db if todo["completed"]])
    pending = total - completed
    
    return {
        "total": total,
        "completed": completed,
        "pending": pending,
        "completion_rate": f"{(completed / total * 100) if total > 0 else 0:.1f}%"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
