#importando objetos do init:
from models import Base
from models import coleta, doacao
#importando funcionalidades:
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import BOOLEAN, INTEGER, VARCHAR, ForeignKey

class compatibilidade(Base): #nomeando uma classe para a tabela "compatibilidade"
    __tablename__ = "compatibilidade"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    id_compatibilidade : Mapped[int] = mapped_column(INTEGER, primary_key=True)
    compativel: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    id_coleta: Mapped[int] = mapped_column(INTEGER, ForeignKey(coleta.id_coleta), nullable=False)
    cpf_doador: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(coleta.cpf_doador), nullable=False)
    coleta_cpf_funcionario: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(coleta.cpf_funcionario), nullable=False)
    coleta_id_hospital: Mapped[int] = mapped_column(INTEGER, ForeignKey(coleta.id_hospital), nullable=False)
    id_doacao: Mapped[int] = mapped_column(INTEGER, ForeignKey(doacao.id_doacao), nullable=False)
    cpf_paciente: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(doacao.cpf_paciente), nullable=False)
    doacao_cpf_funcionario: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(doacao.cpf_funcionario), nullable=False)
    doacao_id_hospital: Mapped[int] = mapped_column(INTEGER, ForeignKey(doacao.id_hospital), nullable=False)

