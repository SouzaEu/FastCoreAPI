from app.services.auth_service import get_current_user_by_role

from fastapi import Depends,  APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.tables import TipoOrgao
from pydantic import BaseModel
from typing import List, Optional

router = APIRouter()

class TipoOrgaoSchema(BaseModel):
    class Config:
        orm_mode = True

@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TipoOrgaoSchema])
@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def listar(db: Session = Depends(get_db)):
    return db.query(TipoOrgao).all()

@router.post("/", response_model=TipoOrgaoSchema)
@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def criar(data: TipoOrgaoSchema, db: Session = Depends(get_db)):
    novo = TipoOrgao(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

@router.put("/{id_tipo}", response_model=TipoOrgaoSchema)
@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def atualizar(id_tipo: int, dados: TipoOrgaoSchema, db: Session = Depends(get_db)):
    registro = db.query(TipoOrgao).filter_by(id_tipo=id_tipo).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    for k, v in dados.dict().items():
        setattr(registro, k, v)
    db.commit()
    return registro

@router.delete("/{id_tipo}")
@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def deletar(id_tipo: int, db: Session = Depends(get_db)):
    registro = db.query(TipoOrgao).filter_by(id_tipo=id_tipo).first()
    if not registro:
        raise HTTPException(status_code=404, detail="Registro não encontrado")
    db.delete(registro)
    db.commit()
    return {"detail": "Registro deletado com sucesso"}
