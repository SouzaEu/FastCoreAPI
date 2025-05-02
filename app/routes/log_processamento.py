
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.tables import LogProcessamento
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class LogProcessamentoSchema(BaseModel):
    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[LogProcessamentoSchema])
def listar(db: Session = Depends(get_db)):
    return db.query(LogProcessamento).all()

@router.post("/", response_model=LogProcessamentoSchema)
def criar(data: LogProcessamentoSchema, db: Session = Depends(get_db)):
    novo = LogProcessamento(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.put("/{id_log}", response_model=LogProcessamentoSchema)
def atualizar(id_log: int, dados: LogProcessamentoSchema, db: Session = Depends(get_db)):
    registro = db.query(LogProcessamento).filter_by(id_log=id_log).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    return registro

@router.delete("/{id_log}")
def deletar(id_log: int, db: Session = Depends(get_db)):
    registro = db.query(LogProcessamento).filter_by(id_log=id_log).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    db.delete(registro)
    db.commit()
    return {"detail": "Registro deletado com sucesso"}
