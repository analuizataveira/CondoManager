from sqlalchemy.orm import Session
from . import models, schemas

# ORDENS DE SERVIÇO - CRUD COMPLETO
def criar_ordem(db: Session, ordem: schemas.OrdemCreate):
    nova_ordem = models.OrdemDeServico(**ordem.dict())
    db.add(nova_ordem)
    db.commit()
    db.refresh(nova_ordem)
    return nova_ordem

def listar_ordens(db: Session):
    return db.query(models.OrdemDeServico).all()

def obter_ordem(db: Session, ordem_id: int):
    return db.query(models.OrdemDeServico).filter(models.OrdemDeServico.id == ordem_id).first()

def atualizar_ordem(db: Session, ordem_id: int, ordem: schemas.OrdemCreate):
    ordem_existente = db.query(models.OrdemDeServico).filter(models.OrdemDeServico.id == ordem_id).first()
    if ordem_existente:
        for campo, valor in ordem.dict().items():
            setattr(ordem_existente, campo, valor)
        db.commit()
        db.refresh(ordem_existente)
        return ordem_existente
    return None

def atualizar_status_ordem(db: Session, ordem_id: int, status: str):
    ordem_existente = db.query(models.OrdemDeServico).filter(models.OrdemDeServico.id == ordem_id).first()
    if ordem_existente:
        ordem_existente.status = status
        db.commit()
        db.refresh(ordem_existente)
        return ordem_existente
    return None

def deletar_ordem(db: Session, ordem_id: int):
    ordem_existente = db.query(models.OrdemDeServico).filter(models.OrdemDeServico.id == ordem_id).first()
    if ordem_existente:
        db.delete(ordem_existente)
        db.commit()
        return True
    return False

# FORNECEDORES - CRUD COMPLETO
def criar_fornecedor(db: Session, fornecedor: schemas.FornecedorCreate):
    novo = models.Fornecedor(**fornecedor.dict())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_fornecedores(db: Session):
    return db.query(models.Fornecedor).all()

def obter_fornecedor(db: Session, fornecedor_id: int):
    return db.query(models.Fornecedor).filter(models.Fornecedor.id == fornecedor_id).first()

def atualizar_fornecedor(db: Session, fornecedor_id: int, fornecedor: schemas.FornecedorCreate):
    fornecedor_existente = db.query(models.Fornecedor).filter(models.Fornecedor.id == fornecedor_id).first()
    if fornecedor_existente:
        for campo, valor in fornecedor.dict().items():
            setattr(fornecedor_existente, campo, valor)
        db.commit()
        db.refresh(fornecedor_existente)
        return fornecedor_existente
    return None

def deletar_fornecedor(db: Session, fornecedor_id: int):
    fornecedor_existente = db.query(models.Fornecedor).filter(models.Fornecedor.id == fornecedor_id).first()
    if fornecedor_existente:
        db.delete(fornecedor_existente)
        db.commit()
        return True
    return False