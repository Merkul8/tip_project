from sqlalchemy import Integer, String, MetaData, Table, Column, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base


metadata = MetaData()
Base: DeclarativeMeta = declarative_base()

user = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('firstname', String, nullable=False),
    Column('lastname', String, nullable=False),
    # Column('room_id', Integer, ForeignKey(room.c.id)),
    Column('email', String(length=320), unique=True, index=True, nullable=False),
    Column('hashed_password', String(length=1024), nullable=False),
    Column('is_active', Boolean, default=True, nullable=False),
    Column('is_superuser', Boolean, default=False, nullable=False),
    Column('is_verified', Boolean, default=False, nullable=False),
)

class User(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(
        Integer, primary_key=True
        )
    firstname: Mapped[str] = mapped_column(
        String, nullable=False
        )
    lastname: Mapped[str] = mapped_column(
        String, nullable=False
        )
    # room_id: Mapped[int] = mapped_column(
    #     Integer, ForeignKey(room.c.id)
    #     )
    email: Mapped[str] = mapped_column(
            String(length=320), unique=True, index=True, nullable=False
        )
    hashed_password: Mapped[str] = mapped_column(
            String(length=1024), nullable=False
        )
    is_active: Mapped[bool] = mapped_column(
        Boolean, default=True, nullable=False
        )
    is_superuser: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )
    is_verified: Mapped[bool] = mapped_column(
            Boolean, default=False, nullable=False
        )