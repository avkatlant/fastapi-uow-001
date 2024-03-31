from datetime import datetime

from pydantic import EmailStr, validator

from src.core.schemas import BaseSchema, PaginationSchema


class UserSchema(BaseSchema):
    id: int
    phone: str
    name: str | None
    username: str | None
    middle_name: str | None
    last_name: str | None
    email: EmailStr | None
    is_active: bool

    created_at: datetime
    updated_at: datetime | None
    deleted_at: datetime | None

    @validator("created_at", "updated_at", "deleted_at")
    def convert_datetime_to_str(cls, v: datetime | None) -> str | None:
        if v is not None:
            return v.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        return v


class UserCreateSchema(BaseSchema):
    phone: str
    password: str
    name: str | None
    username: str | None
    middle_name: str | None
    last_name: str | None
    email: EmailStr | None
    is_active: bool


class UserUpdateSchema(BaseSchema):
    phone: str | None
    password: str | None
    name: str | None
    username: str | None
    middle_name: str | None
    last_name: str | None
    email: EmailStr | None
    is_active: bool | None


class UsersListSchema(BaseSchema):
    total: int
    items: list[UserSchema]


class UsersPaginationSchema(PaginationSchema):
    pass


class UsersSearchSchema(BaseSchema):
    query_row: str | None
    is_active: int | None
