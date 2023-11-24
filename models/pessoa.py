#importando objetos do init:
from models import Base
#importando funcionalidades:
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import VARCHAR, Date
from datetime import date

class pessoa(Base): #nomeando uma classe para a tabela "pessoa"
    __tablename__ = "pessoa"
    #inserindo dados da tabela, criando e mapeando suas colunas:
    cpf: Mapped[str] = mapped_column(VARCHAR(11), primary_key=True, unique=True)
    nome: Mapped[str] = mapped_column(VARCHAR(256), nullable=False)
    data_nasc: Mapped[date] = mapped_column(Date(), nullable=False)
    end_pais: Mapped[str] = mapped_column(VARCHAR(30), nullable=False)
    end_estado: Mapped[str] = mapped_column(VARCHAR(2), nullable=False)
    end_cidade: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    end_rua: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    end_bairro: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)
    end_complemento: Mapped[str] = mapped_column(VARCHAR(50), nullable=False)

    