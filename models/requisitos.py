#importando objetos do init:
from typing import List
from models import Base, doador 
#importando funcionalidades:
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import ForeignKey, BOOLEAN, VARCHAR, DECIMAL

class requisitos(Base): #nomeando uma classe para a tabela "requisitos"
    __tablename__ = "requisitos"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    id_requisitos: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True, nullable=False)
    cpf_doador: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(doador.cpf_doador) )
    saudavel: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=False)
    alimentacao: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=False)
    descanso: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=False)
    peso_minimo: Mapped[float] = mapped_column(BOOLEAN, nullable=False, default=False)
    idade_minima: Mapped[bool] = mapped_column(BOOLEAN, nullable=False, default=False)
    idade_maxima: Mapped[bool] = mapped_column( BOOLEAN, nullable=False, default=False)

