
from fastapi import APIRouter, Depends, HTTPException
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

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[EmpresaSchema])
def listar_empresas(db: Session = Depends(get_db)):
    return db.query(ConfigEmpresa).all()

@router.post("/", response_model=EmpresaSchema)
def criar_empresa(empresa: EmpresaSchema, db: Session = Depends(get_db)):
    nova = ConfigEmpresa(**empresa.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
