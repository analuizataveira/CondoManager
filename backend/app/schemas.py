from pydantic import BaseModel, Field
from datetime import date
from typing import Optional

class OrdemBase(BaseModel):
    tipo: str = Field(..., description="Tipo do serviço", example="Elétrica")
    descricao: str = Field(..., description="Descrição detalhada do serviço", example="Troca de lâmpadas do hall de entrada")
    status: str = Field(..., description="Status atual da ordem", example="Pendente")
    data_agendada: date = Field(..., description="Data agendada para execução", example="2025-06-30")
    fornecedor_id: Optional[int] = Field(None, description="ID do fornecedor responsável (opcional)", example=1)

class OrdemCreate(OrdemBase):
    """Schema para criar uma nova ordem de serviço"""
    pass

class FornecedorSimples(BaseModel):
    """Informações básicas do fornecedor para exibição em ordens"""
    id: int = Field(..., description="ID único do fornecedor", example=1)
    nome: str = Field(..., description="Nome do fornecedor", example="ElétricaTech Ltda")
    especialidade: str = Field(..., description="Especialidade do fornecedor", example="Serviços Elétricos")
    
    class Config:
        orm_mode = True

class Ordem(OrdemBase):
    """Schema completo de uma ordem de serviço"""
    id: int = Field(..., description="ID único da ordem", example=1)
    fornecedor: Optional[FornecedorSimples] = Field(None, description="Dados do fornecedor associado")
    
    class Config:
        orm_mode = True

class FornecedorBase(BaseModel):
    nome: str = Field(..., description="Nome ou razão social", example="HidroFix Serviços")
    especialidade: str = Field(..., description="Área de especialização", example="Hidráulica Residencial") 
    contato: str = Field(..., description="Telefone ou email", example="(35) 99999-9999")

class FornecedorCreate(FornecedorBase):
    """Schema para criar um novo fornecedor"""
    pass

class Fornecedor(FornecedorBase):
    """Schema completo de um fornecedor"""
    id: int = Field(..., description="ID único do fornecedor", example=1)
    
    class Config:
        orm_mode = True