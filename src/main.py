from fastapi import FastAPI
from auth.schemas import UserRead, UserCreate
from auth.base_config import current_user, fastapi_users, auth_backend

app = FastAPI()

fastapi_users = fastapi_users

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = current_user
# @app.get("/protected-route")
# def protected_route(user: User = Depends(current_user)):
#     return f"Hello, {user.email}"

# @app.get("/unprotected-route")
# def protected_route():
#     return f"Hello, user"