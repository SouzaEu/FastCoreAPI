
from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioSchema(BaseModel):
    id_usuario: Optional[int]
    nome: str
    email: EmailStr
    email_verificado: Optional[str]
    perfil: Optional[str]

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str
