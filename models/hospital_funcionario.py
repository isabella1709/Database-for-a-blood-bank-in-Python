#importando objetos do init:
from models import Base 
from models import hospital, funcionario
#importando funcionalidades:
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import INTEGER, VARCHAR, ForeignKey 

class hospital_funcionario(Base): #nomeando uma classe para a tabela "hospital_funcionário"
    __tablename__ = "hospital_funcionario"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    id_hospital_funcionario : Mapped[int] = mapped_column(INTEGER, primary_key=True)
    id_hospital: Mapped[int] = mapped_column(INTEGER, ForeignKey(hospital.id_hospital), nullable=False)
    cpf_funcionario: Mapped[str] = mapped_column(VARCHAR(11), ForeignKey(funcionario.cpf_funcionario), nullable=False)


