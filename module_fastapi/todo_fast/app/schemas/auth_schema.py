from pydantic import BaseModel

class TokenSchema(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str
    
class TokenPayload(BaseModel):
    sub: str | None = None
    exp: int | None = None