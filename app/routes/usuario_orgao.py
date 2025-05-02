
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.tables import UsuarioOrgao
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class UsuarioOrgaoSchema(BaseModel):
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[UsuarioOrgaoSchema])
def listar(db: Session = Depends(get_db)):
    return db.query(UsuarioOrgao).all()

@router.post("/", response_model=UsuarioOrgaoSchema)
def criar(data: UsuarioOrgaoSchema, db: Session = Depends(get_db)):
    novo = UsuarioOrgao(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.put("/{id_usuario}", response_model=UsuarioOrgaoSchema)
def atualizar(id_usuario: int, dados: UsuarioOrgaoSchema, db: Session = Depends(get_db)):
    registro = db.query(UsuarioOrgao).filter_by(id_usuario=id_usuario).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    return registro

@router.delete("/{id_usuario}")
def deletar(id_usuario: int, db: Session = Depends(get_db)):
    registro = db.query(UsuarioOrgao).filter_by(id_usuario=id_usuario).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    db.delete(registro)
    db.commit()
    return {"detail": "Registro deletado com sucesso"}
