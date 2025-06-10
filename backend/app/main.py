from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"mensagem": "API de Gestão Predial"}

# ORDENS
@app.post("/ordens", response_model=schemas.Ordem)
def criar(ordem: schemas.OrdemCreate, db: Session = Depends(get_db)):
    return crud.criar_ordem(db, ordem)

@app.get("/ordens", response_model=list[schemas.Ordem])
def listar(db: Session = Depends(get_db)):
    return crud.listar_ordens(db)

# FORNECEDORES
@app.post("/fornecedores", response_model=schemas.Fornecedor)
def criar(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    return crud.criar_fornecedor(db, fornecedor)

@app.get("/fornecedores", response_model=list[schemas.Fornecedor])
def listar(db: Session = Depends(get_db)):
    return crud.listar_fornecedores(db)
