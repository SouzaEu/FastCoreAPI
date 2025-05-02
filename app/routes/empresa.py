from app.services.auth_service import get_current_user_by_role

from fastapi import Depends,  APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.tables import ConfigEmpresa
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class EmpresaSchema(BaseModel):
    id_config: Optional[int]
    id_usuario: int
    nome_empresa: str
    setor: str
    tamanho_empresa: str
    notificacoes_sistema: Optional[str]
    atualizacoes_novidades: Optional[str]

    class Config:
        orm_mode = True

@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[EmpresaSchema])
@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(ConfigEmpresa).all()

@router.post("/", response_model=EmpresaSchema)
@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def criar_empresa(empresa: EmpresaSchema, db: Session = Depends(get_db)):
    nova = ConfigEmpresa(**empresa.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
