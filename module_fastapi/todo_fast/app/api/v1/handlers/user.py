from fastapi import APIRouter, HTTPException, status
from app.schemas.user_schema import UserAuth, UserPublic
from app.services.user_service import UserService
import pymongo

user_router = APIRouter()

@user_router.post("/adiciona", summary="Adiciona um novo usuario", response_model=UserPublic)
async def adiciona_usuario(data: UserAuth):
    try:
        return await UserService.create_user(data)
    except pymongo.errors.DuplicateKeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuário já existe."
        )
        