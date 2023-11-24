#importando objetos do init:
from models import Base
from models import paciente, funcionario, hospital
#importando funcionalidades:
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, DateTime, VARCHAR, ForeignKey
from datetime import datetime

class doacao(Base): #nomeando uma classe para a tabela "doação"
    __tablename__ = "doacao"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    id_doacao: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True, unique=True, autoincrement=True)
    data_doacao: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    cpf_paciente: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(paciente.cpf_paciente), nullable=False)
    cpf_funcionario: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(funcionario.cpf_funcionario), nullable=False)
    id_hospital: Mapped[int] = mapped_column(INTEGER, ForeignKey(hospital.id_hospital), nullable=False)

