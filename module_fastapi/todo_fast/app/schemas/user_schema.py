from pydantic import BaseModel, EmailStr, Field
from uuid import UUID

class UserAuth(BaseModel):
    email: EmailStr = Field(
        ...,
        description="E-mail do usuário"
    )
    username: str = Field(
        ..., 
        min_length=5,
        max_length=50,
        description="Nome de usuário"
    )
    password: str = Field(
        ...,
        min_length=5,
        max_length=128,
        description="Senha do usuário"
    )
    
class UserDetails(BaseModel):
    user_id: UUID
    username: str
    email: str

