#importando objetos do init:
from typing import List
from models import Base, pessoa 
#importando funcionalidades:
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, BOOLEAN, DECIMAL, VARCHAR, CHAR

class doador(Base): #nomeando uma classe para a tabela "doador"
    __tablename__ = "doador"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    cpf_doador: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(pessoa.cpf),  primary_key=True, unique=True)
    genero: Mapped[str] = mapped_column(CHAR(1), nullable=False)
    apto: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=False)
    tipo_sanguineo_doador: Mapped[str] = mapped_column(VARCHAR(3), nullable=False)
    peso: Mapped[float] = mapped_column(DECIMAL(3,1), nullable=False)


