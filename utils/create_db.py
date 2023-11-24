from models import * # importando as classes de modelo definidas no módulo "models"
from services.database import engine # importando o mecanismo de banco de dados (engine) do módulo "services.database"

def create_db():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    # usando a propriedade "metadata" da classe base "Base" (definida em "models") para criar todas as tabelas no banco de dados associado ao mecanismo (engine)
