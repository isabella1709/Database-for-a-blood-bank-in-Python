#importando objetos do init:
from typing import List
from models import Base, pessoa 
#importando funcionalidades:
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, VARCHAR, CHAR, DECIMAL

class paciente(Base): #nomeando uma classe para a tabela "paciente"
    __tablename__ = "paciente"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    cpf_paciente: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(pessoa.cpf), primary_key=True, unique=True)
    genero: Mapped[str] = mapped_column(CHAR(1), nullable=False)
    tipo_sanguineo_paciente: Mapped[str] = mapped_column(VARCHAR(3), nullable=False)
    peso: Mapped[float] = mapped_column(DECIMAL(3,1), nullable=False)


