from sqlalchemy_utils import create_database, database_exists #impotando objetos da biblioteca SQLalchemy, que realiza o mapeamento obejto-relacional SQL
from sqlalchemy import create_engine # importando a função "create_engine" do módulo "sqlalchemy_utils"
from sqlalchemy.orm import Session # importando a classe "Session" do módulo "sqlalchemy_utils"
from urllib.parse import quote # importando a função "quote" do módulo "urllib.parse"

#realizando a conexão com o banco no MySQL, usando o sqlalchemy_utils
instance: str = f'mysql+pymysql://root:{quote("@1234")}@localhost:3306/sangue'

# verificar se o banco de dados não existe e criá-lo, se necessário
if not database_exists(instance):
    create_database(instance)

# imprimir se o banco de dados existe após a verificação e possível criação
print(database_exists(instance))

# criar um mecanismo de banco de dados usando SQLAlchemy
# o parâmetro 'echo=True' permite que as consultas SQL sejam exibidas no console
engine = create_engine(instance, echo = True) 
# criar uma sessão de banco de dados usando SQLAlchemy
# a sessão está vinculada ao mecanismo (engine) criado acima
# 'autocommit=False' significa que as alterações não são automaticamente confirmadas no banco de dados
# 'autoflush=True' significa que as alterações são automaticamente enviadas para o banco de dados, quando necessário
session = Session(bind = engine, autocommit = False, autoflush = True)

