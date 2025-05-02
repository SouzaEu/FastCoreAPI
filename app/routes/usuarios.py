from app.services.auth_service import get_current_user_by_role

from fastapi import Depends,  APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.tables import Usuario
from app.models.schemas import UsuarioSchema

router = APIRouter()

@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UsuarioSchema])
@router.get("/check-admin", dependencies=[Depends(get_current_user_by_role("ADMIN"))])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()
