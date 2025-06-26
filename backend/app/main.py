from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import Base, engine, SessionLocal

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CondoManager API", 
    description="API para gerenciamento de condomínios com sistema de ordens de serviço e fornecedores",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", tags=["Home"])
def home():
    """Endpoint raiz da API - Informações básicas do sistema"""
    return {"mensagem": "API de Gestão Predial - CondoManager", "versao": "1.0.0"}

# ORDENS DE SERVIÇO - CRUD COMPLETO
@app.post("/ordens", response_model=schemas.Ordem, tags=["Ordens de Serviço"])
def criar_ordem(ordem: schemas.OrdemCreate, db: Session = Depends(get_db)):
    """
    Criar uma nova ordem de serviço
    
    - **tipo**: Tipo do serviço (Elétrica, Hidráulica, etc.)
    - **descricao**: Descrição detalhada do serviço
    - **status**: Status atual da ordem
    - **data_agendada**: Data para execução do serviço
    - **fornecedor_id**: ID do fornecedor (opcional)
    """
    return crud.criar_ordem(db, ordem)

@app.get("/ordens", response_model=list[schemas.Ordem], tags=["Ordens de Serviço"])
def listar_ordens(db: Session = Depends(get_db)):
    """
    Listar todas as ordens de serviço
    
    Retorna todas as ordens com informações do fornecedor associado (se houver)
    """
    return crud.listar_ordens(db)

@app.get("/ordens/{ordem_id}", response_model=schemas.Ordem, tags=["Ordens de Serviço"])
def obter_ordem(ordem_id: int, db: Session = Depends(get_db)):
    """
    Obter uma ordem de serviço específica
    
    Retorna os detalhes completos da ordem incluindo informações do fornecedor associado
    """
    ordem = crud.obter_ordem(db, ordem_id)
    if ordem is None:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return ordem

@app.put("/ordens/{ordem_id}", response_model=schemas.Ordem, tags=["Ordens de Serviço"])
def atualizar_ordem(ordem_id: int, ordem: schemas.OrdemCreate, db: Session = Depends(get_db)):
    """
    Atualizar uma ordem de serviço completamente
    
    Permite alterar todos os campos da ordem, incluindo associar/desassociar fornecedor
    """
    ordem_atualizada = crud.atualizar_ordem(db, ordem_id, ordem)
    if ordem_atualizada is None:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return ordem_atualizada

@app.patch("/ordens/{ordem_id}/status", response_model=schemas.Ordem, tags=["Ordens de Serviço"])
def atualizar_status_ordem(ordem_id: int, status: str, db: Session = Depends(get_db)):
    """
    Atualizar apenas o status de uma ordem de serviço
    
    - **status**: Novo status (Pendente, Em Andamento, Concluído, Cancelado)
    """
    ordem_atualizada = crud.atualizar_status_ordem(db, ordem_id, status)
    if ordem_atualizada is None:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return ordem_atualizada

@app.delete("/ordens/{ordem_id}", tags=["Ordens de Serviço"])
def deletar_ordem(ordem_id: int, db: Session = Depends(get_db)):
    """
    Deletar uma ordem de serviço
    
    Remove permanentemente a ordem do sistema
    """
    ordem_deletada = crud.deletar_ordem(db, ordem_id)
    if not ordem_deletada:
        raise HTTPException(status_code=404, detail="Ordem não encontrada")
    return {"mensagem": "Ordem deletada com sucesso"}

# FORNECEDORES - CRUD COMPLETO
@app.post("/fornecedores", response_model=schemas.Fornecedor, tags=["Fornecedores"])
def criar_fornecedor(fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    """
    Cadastrar um novo fornecedor
    
    - **nome**: Nome ou razão social do fornecedor
    - **especialidade**: Área de atuação (Elétrica, Hidráulica, etc.)
    - **contato**: Telefone ou email para contato
    """
    return crud.criar_fornecedor(db, fornecedor)

@app.get("/fornecedores", response_model=list[schemas.Fornecedor], tags=["Fornecedores"])
def listar_fornecedores(db: Session = Depends(get_db)):
    """
    Listar todos os fornecedores cadastrados
    
    Retorna a lista completa de fornecedores disponíveis no sistema
    """
    return crud.listar_fornecedores(db)

@app.get("/fornecedores/{fornecedor_id}", response_model=schemas.Fornecedor, tags=["Fornecedores"])
def obter_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    """
    Obter um fornecedor específico
    
    Retorna os dados completos de um fornecedor pelo ID
    """
    fornecedor = crud.obter_fornecedor(db, fornecedor_id)
    if fornecedor is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor

@app.put("/fornecedores/{fornecedor_id}", response_model=schemas.Fornecedor, tags=["Fornecedores"])
def atualizar_fornecedor(fornecedor_id: int, fornecedor: schemas.FornecedorCreate, db: Session = Depends(get_db)):
    """
    Atualizar um fornecedor existente
    
    Permite alterar nome, especialidade e contato do fornecedor
    """
    fornecedor_atualizado = crud.atualizar_fornecedor(db, fornecedor_id, fornecedor)
    if fornecedor_atualizado is None:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return fornecedor_atualizado

@app.delete("/fornecedores/{fornecedor_id}", tags=["Fornecedores"])
def deletar_fornecedor(fornecedor_id: int, db: Session = Depends(get_db)):
    """
    Deletar um fornecedor
    
    Remove permanentemente o fornecedor do sistema.
    ATENÇÃO: Ordens associadas a este fornecedor terão o campo fornecedor_id definido como NULL.
    """
    fornecedor_deletado = crud.deletar_fornecedor(db, fornecedor_id)
    if not fornecedor_deletado:
        raise HTTPException(status_code=404, detail="Fornecedor não encontrado")
    return {"mensagem": "Fornecedor deletado com sucesso"}
