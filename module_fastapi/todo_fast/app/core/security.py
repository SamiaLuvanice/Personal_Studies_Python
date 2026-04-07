import hashlib
import bcrypt
from typing import Any, Optional, Union
from datetime import datetime, timedelta
from jose import jwt

from app.core.config import settings

def _prehash_password(password: str) -> bytes:
    # Normaliza o tamanho da entrada para evitar limite de 72 bytes do bcrypt.
    return hashlib.sha256(password.encode("utf-8")).hexdigest().encode("utf-8")


# Criptografia da senha
def get_password(password: str) -> str:
    hashed = bcrypt.hashpw(_prehash_password(password), bcrypt.gensalt())
    return hashed.decode("utf-8")


# Descriptografia da senha
def verify_password(password: str, hashed_password: str) -> bool:
    hashed_password_bytes = hashed_password.encode("utf-8")

    # Primeiro tenta o formato novo com pre-hash.
    if bcrypt.checkpw(_prehash_password(password), hashed_password_bytes):
        return True

    # Compatibilidade com hashes antigos gravados sem pre-hash.
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed_password_bytes)
    except ValueError:
        return False
    
def create_access_token(
    subject: Union[str, Any],
    expires_delta: Optional[timedelta] = None,
) -> str:
    if expires_delta is not None:
        expire_at = datetime.utcnow() + expires_delta
    else:
        expire_at = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
        
    info_jwt = {
        "exp": expire_at,
        "sub": str(subject)
    }
    
    jwt_encoded = jwt.encode(
        info_jwt, 
        settings.JWT_SECRET_KEY,
        settings.ALGORITHM
    )
    
    return jwt_encoded

def create_refresh_token(
    subject: Union[str, Any],
    expires_delta: Optional[timedelta] = None,
) -> str:
    if expires_delta is not None:
        expire_at = datetime.utcnow() + expires_delta
    else:
        expire_at = datetime.utcnow() + timedelta(
            minutes=settings.REFRESH_TOKEN_EXPIRE_MINUTES
        )
        
    info_jwt = {
        "exp": expire_at,
        "sub": str(subject)
    }
    
    jwt_encoded = jwt.encode(
        info_jwt, 
        settings.JWT_REFRESH_SECRET_KEY,
        settings.ALGORITHM
    )
    
    return jwt_encoded