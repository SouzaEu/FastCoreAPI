
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.tables import CanalAlerta
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class CanalAlertaSchema(BaseModel):
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[CanalAlertaSchema])
def listar(db: Session = Depends(get_db)):
    return db.query(CanalAlerta).all()

@router.post("/", response_model=CanalAlertaSchema)
def criar(data: CanalAlertaSchema, db: Session = Depends(get_db)):
    novo = CanalAlerta(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.put("/{id_canal}", response_model=CanalAlertaSchema)
def atualizar(id_canal: int, dados: CanalAlertaSchema, db: Session = Depends(get_db)):
    registro = db.query(CanalAlerta).filter_by(id_canal=id_canal).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    return registro

@router.delete("/{id_canal}")
def deletar(id_canal: int, db: Session = Depends(get_db)):
    registro = db.query(CanalAlerta).filter_by(id_canal=id_canal).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    db.delete(registro)
    db.commit()
    return {"detail": "Registro deletado com sucesso"}
