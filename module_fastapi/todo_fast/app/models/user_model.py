from beanie import Document, Indexed
from uuid import uuid4, UUID
from pydantic import EmailStr, Field
from datetime import datetime
from typing import Annotated, Optional


class User(Document):
    user_id: UUID = Field(default_factory=uuid4)
    username: Annotated[str, Indexed(unique=True)]
    email: Annotated[EmailStr, Indexed(unique=True)]
    hashed_password: str
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    disabled: bool = False

    class Settings:
        name = "users"

    def __repr__(self) -> str:
        return f"<User {self.email}>"

    def __str__(self) -> str:
        return str(self.email)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, User):
            return self.email == other.email
        return False

    @property
    def created_at(self) -> datetime:
        return self.id.generation_time

    @classmethod
    async def by_email(cls, email: str) -> Optional["User"]:
        return await cls.find_one(cls.email == email)
    
    