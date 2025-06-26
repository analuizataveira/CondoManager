from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class OrdemDeServico(Base):
    __tablename__ = "ordens"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String, nullable=False)
    descricao = Column(String)
    status = Column(String)
    data_agendada = Column(Date)
    fornecedor_id = Column(Integer, ForeignKey("fornecedores.id"), nullable=True)
    
    # Relacionamento
    fornecedor = relationship("Fornecedor", back_populates="ordens")

class Fornecedor(Base):
    __tablename__ = "fornecedores"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    especialidade = Column(String)
    contato = Column(String)
    
    # Relacionamento
    ordens = relationship("OrdemDeServico", back_populates="fornecedor")