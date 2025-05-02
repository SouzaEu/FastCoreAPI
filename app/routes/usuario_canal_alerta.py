
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.tables import UsuarioCanalAlerta
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class UsuarioCanalAlertaSchema(BaseModel):
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[UsuarioCanalAlertaSchema])
def listar(db: Session = Depends(get_db)):
    return db.query(UsuarioCanalAlerta).all()

@router.post("/", response_model=UsuarioCanalAlertaSchema)
def criar(data: UsuarioCanalAlertaSchema, db: Session = Depends(get_db)):
    novo = UsuarioCanalAlerta(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.put("/{id_usuario}", response_model=UsuarioCanalAlertaSchema)
def atualizar(id_usuario: int, dados: UsuarioCanalAlertaSchema, db: Session = Depends(get_db)):
    registro = db.query(UsuarioCanalAlerta).filter_by(id_usuario=id_usuario).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    return registro

@router.delete("/{id_usuario}")
def deletar(id_usuario: int, db: Session = Depends(get_db)):
    registro = db.query(UsuarioCanalAlerta).filter_by(id_usuario=id_usuario).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    db.delete(registro)
    db.commit()
    return {"detail": "Registro deletado com sucesso"}
