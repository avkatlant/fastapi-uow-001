from datetime import datetime

from sqlalchemy import TIMESTAMP, Boolean, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.models.src.models import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)

    username: Mapped[str] = mapped_column(String, unique=True)
    email: Mapped[str] = mapped_column(String, nullable=True)
    phone: Mapped[str] = mapped_column(String, nullable=True)
    password: Mapped[str] = mapped_column(String, nullable=True)
    name: Mapped[str] = mapped_column(String, nullable=True)
    middle_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=False),
        nullable=False,
        default=datetime.utcnow,
    )
    updated_at: Mapped[datetime | None] = mapped_column(
        TIMESTAMP(timezone=False),
        nullable=True,
        onupdate=datetime.utcnow,
    )
    deleted_at: Mapped[datetime | None] = mapped_column(TIMESTAMP(timezone=False), nullable=True)

    def __repr__(self) -> str:
        return f"<User id={self.id}>"
