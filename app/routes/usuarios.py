
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models.tables import Usuario
from app.models.schemas import UsuarioSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[UsuarioSchema])
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()
