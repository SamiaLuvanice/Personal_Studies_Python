from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from typing import Any
from jose import JWTError, jwt
from pydantic import ValidationError

from app.core.security import create_access_token, create_refresh_token
from app.core.config import settings
from app.services.user_service import UserService

from app.schemas.auth_schema import RefreshTokenRequest, TokenPayload, TokenSchema

auth_router = APIRouter()

@auth_router.post("/login",
                  summary="Cria Access Token e Rerfesh Token para o usuário",
                  response_model=TokenSchema
                  )
async def login(data: OAuth2PasswordRequestForm = Depends()) -> Any:
    usuario = await UserService.authenticate(
        email=data.username,
        password = data.password
    )

    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas.",
        )

    return {
        "access_token": create_access_token(usuario.email),
        "refresh_token": create_refresh_token(usuario.email),
        "token_type": "bearer",
    }

@auth_router.post("/refresh",
                  summary="Cria um novo Access Token usando o Refresh Token",
                    response_model=TokenSchema
                )
async def refresh_token(data: RefreshTokenRequest) -> Any:
    try:
        payload = jwt.decode(
            data.refresh_token,
            settings.JWT_REFRESH_SECRET_KEY,
            settings.ALGORITHM,
        )
        token_data = TokenPayload(**payload)
        if token_data.sub is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Refresh token inválido.",
            )
    except (JWTError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Refresh token inválido.",
        )

    usuario = await UserService.get_user_by_email(token_data.sub)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuário não encontrado.",
        )

    return {
        "access_token": create_access_token(usuario.email),
        "refresh_token": create_refresh_token(usuario.email),
        "token_type": "bearer",
    }