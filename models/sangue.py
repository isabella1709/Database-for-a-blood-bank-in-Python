#importando objetos do init:
from models import Base
from models import hospital, coleta, doacao
#importando funcionalidades:
from sqlalchemy import create_engine
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, VARCHAR, ForeignKey

class sangue(Base): #nomeando uma classe para a tabela "sangue"
    __tablename__ = "sangue"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    id_sangue: Mapped[int] = mapped_column(INTEGER, nullable=False, primary_key=True, autoincrement=True)
    quantidade: Mapped[int] = mapped_column(INTEGER, nullable=False)
    id_hospital: Mapped[int] = mapped_column(INTEGER, ForeignKey(hospital.id_hospital), nullable=False)
    id_coleta: Mapped[int] = mapped_column(INTEGER, ForeignKey(coleta.id_coleta), nullable=False)
    cpf_doador: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(coleta.cpf_doador), nullable=False)
    coleta_cpf_funcionario: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(coleta.cpf_funcionario), nullable=False)
    id_doacao: Mapped[int] = mapped_column(INTEGER, ForeignKey(doacao.id_doacao), nullable=False, unique=True)
    cpf_paciente: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(doacao.cpf_paciente), nullable=False)
    doacao_cpf_funcionario: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(doacao.cpf_funcionario), nullable=False)

