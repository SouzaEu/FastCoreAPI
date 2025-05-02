
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.tables import ResumoDou
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class ResumoDouSchema(BaseModel):
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[ResumoDouSchema])
def listar(db: Session = Depends(get_db)):
    return db.query(ResumoDou).all()

@router.post("/", response_model=ResumoDouSchema)
def criar(data: ResumoDouSchema, db: Session = Depends(get_db)):
    novo = ResumoDou(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.put("/{id_resumo}", response_model=ResumoDouSchema)
def atualizar(id_resumo: int, dados: ResumoDouSchema, db: Session = Depends(get_db)):
    registro = db.query(ResumoDou).filter_by(id_resumo=id_resumo).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    return registro

@router.delete("/{id_resumo}")
def deletar(id_resumo: int, db: Session = Depends(get_db)):
    registro = db.query(ResumoDou).filter_by(id_resumo=id_resumo).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    db.delete(registro)
    db.commit()
    return {"detail": "Registro deletado com sucesso"}
