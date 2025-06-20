from app.services.auth_service import get_current_user_by_role
from fastapi import Depends,  APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from app.models.database import SessionLocal
from app.models.tables import Assinatura, MetodoPagamento, Fatura

router = APIRouter()

# ====== Schemas ======

class AssinaturaSchema(BaseModel):
    id_assinatura: Optional[int]
    id_usuario: int
    plano: str
    valor: float

    class Config:
        orm_mode = True

class MetodoPagamentoSchema(BaseModel):
    id_pagamento: Optional[int]
    id_usuario: int
    tipo_cartao: str
    validade: str

    class Config:
        orm_mode = True

class FaturaSchema(BaseModel):
    id_fatura: Optional[int]
    id_usuario: int
    mes_referencia: str
    valor: float
    status: str

    class Config:
        orm_mode = True

# ====== Dependência ======
@router.get("/check-padrao", dependencies=[Depends(get_current_user_by_role("PADRAO"))])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ====== ASSINATURA ======
@router.get("/assinaturas", response_model=List[AssinaturaSchema])
@router.get("/check-padrao", dependencies=[Depends(get_current_user_by_role("PADRAO"))])
def listar_assinaturas(db: Session = Depends(get_db)):
    return db.query(Assinatura).all()

@router.post("/assinaturas", response_model=AssinaturaSchema)
@router.get("/check-padrao", dependencies=[Depends(get_current_user_by_role("PADRAO"))])
def criar_assinatura(data: AssinaturaSchema, db: Session = Depends(get_db)):
    nova = Assinatura(**data.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova

# ====== MÉTODO DE PAGAMENTO ======
@router.get("/metodos", response_model=List[MetodoPagamentoSchema])
@router.get("/check-padrao", dependencies=[Depends(get_current_user_by_role("PADRAO"))])
def listar_metodos(db: Session = Depends(get_db)):
    return db.query(MetodoPagamento).all()

@router.post("/metodos", response_model=MetodoPagamentoSchema)
@router.get("/check-padrao", dependencies=[Depends(get_current_user_by_role("PADRAO"))])
def criar_metodo(data: MetodoPagamentoSchema, db: Session = Depends(get_db)):
    novo = MetodoPagamento(**data.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

# ====== FATURAS ======
@router.get("/faturas", response_model=List[FaturaSchema])
@router.get("/check-padrao", dependencies=[Depends(get_current_user_by_role("PADRAO"))])
def listar_faturas(db: Session = Depends(get_db)):
    return db.query(Fatura).all()

@router.post("/faturas", response_model=FaturaSchema)
@router.get("/check-padrao", dependencies=[Depends(get_current_user_by_role("PADRAO"))])
def criar_fatura(data: FaturaSchema, db: Session = Depends(get_db)):
    nova = Fatura(**data.dict())
    db.add(nova)
    db.commit()
    db.refresh(nova)
    return nova
