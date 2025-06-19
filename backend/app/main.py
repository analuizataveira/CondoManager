from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(title="CondoManager API", description="API para gerenciamento de condominios")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"mensagem": "API de Gestão Predial - CondoManager"}

# ORDENS DE SERVIÇO - CRUD COMPLETO
@app.post("/ordens", response_model=schemas.Ordem)
def criar_ordem(ordem: schemas.OrdemCreate, db: Session = Depends(get_db)):
    return crud.criar_ordem(db, ordem)

@app.get("/ordens", response_model=list[schemas.Ordem])
def listar_ordens(db: Session = Depends(get_db)):
    return crud.listar_ordens(db)

@app.get("/ordens/{ordem_id}", response_model=schemas.Ordem)
def obter_ordem(ordem_id: int, db: Session = Depends(get_db)):
    ordem = crud.obter_ordem(db, ordem_id)
    if ordem is None:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return ordem

@app.put("/ordens/{ordem_id}", response_model=schemas.Ordem)
def atualizar_ordem(ordem_id: int, ordem: schemas.OrdemCreate, db: Session = Depends(get_db)):
    ordem_atualizada = crud.atualizar_ordem(db, ordem_id, ordem)
    if ordem_atualizada is None:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return ordem_atualizada

@app.patch("/ordens/{ordem_id}/status", response_model=schemas.Ordem)
def atualizar_status_ordem(ordem_id: int, status: str, db: Session = Depends(get_db)):
    ordem_atualizada = crud.atualizar_status_ordem(db, ordem_id, status)
    if ordem_atualizada is None:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return ordem_atualizada

@app.delete("/ordens/{ordem_id}")
def deletar_ordem(ordem_id: int, db: Session = Depends(get_db)):
    ordem_deletada = crud.deletar_ordem(db, ordem_id)
    if not ordem_deletada:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return {"mensagem": "Ordem deletada com sucesso"}

# FORNECEDORES - CRUD COMPLETO
@app.post("/fornecedores", response_model=schemas.Fornecedor)
def criar_fornecedor(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    return crud.criar_fornecedor(db, fornecedor)

@app.get("/fornecedores", response_model=list[schemas.Fornecedor])
def listar_fornecedores(db: Session = Depends(get_db)):
    return crud.listar_fornecedores(db)

@app.get("/fornecedores/{fornecedor_id}", response_model=schemas.Fornecedor)
def obter_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    fornecedor = crud.obter_fornecedor(db, fornecedor_id)
    if fornecedor is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

@app.put("/fornecedores/{fornecedor_id}", response_model=schemas.Fornecedor)
def atualizar_fornecedor(fornecedor_id: int, fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    fornecedor_atualizado = crud.atualizar_fornecedor(db, fornecedor_id, fornecedor)
    if fornecedor_atualizado is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor_atualizado

@app.delete("/fornecedores/{fornecedor_id}")
def deletar_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    fornecedor_deletado = crud.deletar_fornecedor(db, fornecedor_id)
    if not fornecedor_deletado:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return {"mensagem": "Fornecedor deletado com sucesso"}
