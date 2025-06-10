from sqlalchemy.orm import Session
from . import models, schemas

# Ordens
def criar_ordem(db: Session, ordem: schemas.OrdemCreate):
    nova_ordem = models.OrdemDeServico(**ordem.dict())
    db.add(nova_ordem)
    db.commit()
    db.refresh(nova_ordem)
    return nova_ordem

def listar_ordens(db: Session):
    return db.query(models.OrdemDeServico).all()

# Fornecedores
def criar_fornecedor(db: Session, fornecedor: schemas.FornecedorCreate):
    novo = models.Fornecedor(**fornecedor.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_fornecedores(db: Session):
    return db.query(models.Fornecedor).all()
