from pydantic import parse_obj_as
from sqlalchemy.ext.asyncio import AsyncSession

from src.core.utils import get_password_hash, get_phone_from_string

from .dals import user_dal
from .schemas import (
    UserCreateSchema,
    UserSchema,
    UsersListSchema,
    UsersPaginationSchema,
    UsersSearchSchema,
    UserUpdateSchema,
)


class UserAction:
    @staticmethod
    async def get_all(
        db: AsyncSession,
        pagi: UsersPaginationSchema | None = None,
        search_data: UsersSearchSchema | None = None,
        order_by_value: str | list[str | list[str]] | None = None,
    ) -> UsersListSchema:
        pagi_dict = pagi.dict(exclude_unset=True) if pagi is not None else None
        search_data_dict = search_data.dict(exclude_unset=True) if search_data is not None else None

        items = await user_dal.get_multi(
            db,
            pagi=pagi_dict,
            search_data=search_data_dict,
            order_by_value=order_by_value,
        )

        total = await user_dal.get_count_multi(db, search_data=search_data_dict)
        return UsersListSchema(items=parse_obj_as(list[UserSchema], items), total=total)

    @staticmethod
    async def create(db: AsyncSession, data: UserCreateSchema) -> UserSchema:
        current_data = data.dict()
        if "password" in current_data and current_data["password"]:
            current_data["password"] = get_password_hash(current_data["password"])

        if not current_data["username"]:
            current_data["username"] = current_data["phone"]

        if current_data["phone"] is not None:
            current_data["phone"] = get_phone_from_string(current_data["phone"])

        user = await user_dal.create(db, current_data)
        return UserSchema.from_orm(user)

    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: int) -> UserSchema | None:
        user = await user_dal.get(db, user_id)
        if user is not None:
            return UserSchema.from_orm(user)
        return None

    @staticmethod
    async def update(
        db: AsyncSession,
        user_id: int,
        data: UserUpdateSchema,
    ) -> UserSchema:
        updated_data = data.dict(exclude_unset=True)

        if "password" in updated_data:
            if updated_data["password"]:
                updated_data["password"] = get_password_hash(updated_data["password"])
            else:
                del updated_data["password"]

        if "phone" in updated_data and updated_data["phone"]:
            updated_data["phone"] = get_phone_from_string(updated_data["phone"])

        user = await user_dal.update(db, user_id, updated_data)
        return UserSchema.from_orm(user)
