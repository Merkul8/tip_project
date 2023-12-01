import uuid

from fastapi_users import schemas


class UserRead(schemas.BaseUser[int]):
    id: int
    email: str
    firstname: str
    lastname: str
    room_id: int
    is_active: bool = True
    is_superuser: bool = False
    is_verified: bool = False

    class Config:
        orm_mode = True


class UserCreate(schemas.BaseUserCreate):
    pass