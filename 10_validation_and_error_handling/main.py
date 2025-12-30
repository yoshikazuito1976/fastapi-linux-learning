from __future__ import annotations

from typing import Annotated, Optional

from fastapi import Body, FastAPI, HTTPException, Path, Query, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, field_validator

app = FastAPI(title="10_validation_and_error_handling")

# -----------------------------
# Validation Error Handler
# -----------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError,):
    """
    FastAPI標準の422レスポンスは情報量が多い。
    ここでは「APIのエラー形式を整える」例として整形する。
    """
    return JSONResponse(
        status_code=422,
        content={
            "message": "validation error",
            "errors": exc.errors(),  # どのフィールドで何が起きたか
            "path": str(request.url.path),
        },)

# -----------------------------
# Models (Pydantic)
# -----------------------------
class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=20, examples=["yito"])
    email: str = Field(
        pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$",
        examples=["foo@example.com"],)
    password: str = Field(min_length=8, examples=["verysecret1"])

    @field_validator("password")
    @classmethod
    def password_must_have_number(cls, v: str) -> str:
        if not any(ch.isdigit() for ch in v):
            raise ValueError("password must include at least one number")
        return v


class UserOut(BaseModel):
    user_id: int
    username: str
    email: str


class OrderItem(BaseModel):
    sku: str = Field(min_length=3, max_length=20)
    qty: int = Field(ge=1, le=99)


class OrderCreate(BaseModel):
    user_id: int = Field(ge=1)
    items: list[OrderItem] = Field(min_length=1)

# -----------------------------
# Endpoints
# -----------------------------
@app.get("/items/{item_id}")
def get_item(
    item_id: Annotated[int, Path(ge=1, le=9999, description="item_id must be 1..9999")],
    q: Annotated[Optional[str], Query(min_length=2, max_length=20)] = None,
    limit: Annotated[int, Query(ge=1, le=50)] = 10,):
    """
    Path / Query の validation を観察する。
    """
    return {"item_id": item_id, "q": q, "limit": limit}


@app.post("/users", response_model=UserOut, status_code=201)
def create_user(user: Annotated[UserCreate, Body()]):
    """
    Body (JSON) の validation を観察する。
    """
    return UserOut(user_id=100, username=user.username, email=user.email)


@app.post("/orders", status_code=201)
def create_order(order: OrderCreate):
    """
    ネストしたモデルの validation を観察する。
    """
    total_qty = sum(i.qty for i in order.items)
    return {
        "user_id": order.user_id,
        "items": len(order.items),
        "total_qty": total_qty,
    }


@app.get("/errors/demo")
def error_demo(
    kind: Annotated[str, Query(pattern="^(http|crash)$")] = "http",):
    """
    HTTPException（想定エラー）と、想定外例外（500）を比較する。
    """
    if kind == "http":
        raise HTTPException(
            status_code=404,
            detail="this is an intentional HTTP error",
        )

    # 想定外例外（500）をわざと起こす
    1 / 0

