#importando objetos do init:
from models import Base
from models import doador, funcionario, hospital
#importando funcionalidades:
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, DateTime, VARCHAR, ForeignKey
from datetime import datetime

class coleta(Base): #nomeando uma classe para a tabela "coleta"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    __tablename__ = "coleta"
    id_coleta: Mapped[int] = mapped_column(INTEGER, primary_key=True, nullable=False, unique=True, autoincrement=True)
    data_coleta: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    cpf_doador: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(doador.cpf_doador), nullable=False)
    cpf_funcionario: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(funcionario.cpf_funcionario), nullable=False)
    id_hospital: Mapped[int] = mapped_column(INTEGER, ForeignKey(hospital.id_hospital), nullable=False)



