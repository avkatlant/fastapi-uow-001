from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from src.models.src.database import get_db

from .actions import UserAction
from .schemas import (
    UserCreateSchema,
    UserSchema,
    UsersListSchema,
    UsersPaginationSchema,
    UsersSearchSchema,
    UserUpdateSchema,
)

users_router = APIRouter()


@users_router.post("/all/", summary="Get all or search users")
async def get_users(
    pagi: UsersPaginationSchema | None = None,
    search_data: UsersSearchSchema | None = None,
    order_by_value: str | list[str | list[str]] | None = None,
    db: AsyncSession = Depends(get_db),
) -> UsersListSchema:
    return await UserAction.get_all(db, pagi, search_data, order_by_value)


@users_router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(
    data: UserCreateSchema,
    db: AsyncSession = Depends(get_db),
) -> UserSchema:
    return await UserAction.create(db, data)


@users_router.get("/{user_id}/")
async def get_user_by_id(
    user_id: int,
    db: AsyncSession = Depends(get_db),
) -> UserSchema:
    item = await UserAction.get_by_id(db, user_id)
    if item is not None:
        return item
    raise HTTPException(status_code=404, detail="User not found")


@users_router.patch("/{user_id}/")
async def update_user(
    user_id: int,
    data: UserUpdateSchema,
    db: AsyncSession = Depends(get_db),
) -> UserSchema:
    return await UserAction.update(db, user_id, data)
