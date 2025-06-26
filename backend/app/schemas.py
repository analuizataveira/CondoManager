from pydantic import BaseModel
from datetime import date
from typing import Optional

class OrdemBase(BaseModel):
    tipo: str
    descricao: str
    status: str
    data_agendada: date
    fornecedor_id: Optional[int] = None

class OrdemCreate(OrdemBase):
    pass

class FornecedorSimples(BaseModel):
    id: int
    nome: str
    especialidade: str
    
    class Config:
        orm_mode = True

class Ordem(OrdemBase):
    id: int
    fornecedor: Optional[FornecedorSimples] = None
    
    class Config:
        orm_mode = True

class FornecedorBase(BaseModel):
    nome: str
    especialidade: str
    contato: str

class FornecedorCreate(FornecedorBase):
    pass

class Fornecedor(FornecedorBase):
    id: int
    
    class Config:
        orm_mode = True