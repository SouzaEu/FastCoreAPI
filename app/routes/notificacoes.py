from app.services.auth_service import get_current_user_by_role
from fastapi import Depends,  APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from app.models.database import SessionLocal
from app.models.tables import ConfigEmpresa  # supondo que preferências estão nessa tabela

router = APIRouter()

class PreferenciaNotificacaoSchema(BaseModel):
    id_usuario: int
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

@router.get("/", response_model=List[PreferenciaNotificacaoSchema])
@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def listar_preferencias(db: Session = Depends(get_db)):
    return db.query(ConfigEmpresa).all()

@router.put("/{id_usuario}")
@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def atualizar_preferencias(id_usuario: int, preferencias: PreferenciaNotificacaoSchema, db: Session = Depends(get_db)):
    config = db.query(ConfigEmpresa).filter_by(id_usuario=id_usuario).first()
    if not config:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    config.notificacoes_sistema = preferencias.notificacoes_sistema
    config.atualizacoes_novidades = preferencias.atualizacoes_novidades
    db.commit()
    return {"detail": "Preferências atualizadas com sucesso"}
