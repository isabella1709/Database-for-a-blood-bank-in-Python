#importando objetos do init:
from models import Base
#importando funcionalidades:
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import VARCHAR

class hospital(Base): #nomeando uma classe para a tabela "hospital"
    __tablename__ = "hospital"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    id_hospital: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True, nullable=False)
    nome_hospital: Mapped[str] = mapped_column(VARCHAR(256), nullable=False)
    end_pais: Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    end_estado: Mapped[str] = mapped_column(VARCHAR(2), nullable=False)
    end_cidade: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    end_rua: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    end_bairro: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    end_complemento: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)