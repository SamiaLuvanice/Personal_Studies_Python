# user = {
#     "nome": "João",
#     "idade": 25,
#     "email": "joao.silva@example.com"
# }

# print(user)

from pydantic import BaseModel, EmailStr, ValidationError, field_validator

class User(BaseModel):
    nome: str
    idade: int
    email: EmailStr

    @field_validator('idade')
    @classmethod
    def validate_idade(cls, value: int) -> int:
        if value < 0:
            raise ValueError('Idade deve ser maior ou igual a 0')
        return value

try:
    user1 = User(nome="João", idade=25, email="joao.silva@example.com")
    print(user1)
except ValidationError as error:
    print(error)