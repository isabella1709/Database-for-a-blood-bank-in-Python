#importando objetos do init:
from typing import List
from models import Base, pessoa 
#importando funcionalidades:
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, VARCHAR, Date
from datetime import date

class funcionario(Base): #nomeando uma classe para a tabela "funcionário"
    __tablename__ = "funcionario"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    cpf_funcionario: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(pessoa.cpf), primary_key=True, unique=True)
    data_contratacao: Mapped[date] = mapped_column(Date(), nullable=False)
    cargo: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)


