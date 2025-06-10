from pydantic import BaseModel
from datetime import date

class OrdemBase(BaseModel):
    tipo: str
    descricao: str
    status: str
    data_agendada: date

class OrdemCreate(OrdemBase):
    pass

class Ordem(OrdemBase):
    id: int
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
