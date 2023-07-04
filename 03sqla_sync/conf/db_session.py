import sqlalchemy as sa

# Criar uma sessão
from sqlalchemy.orm import sessionmaker
# Vamos criar objetos do tipo session
from sqlalchemy.orm import Session
# Criar o motor do banco de dados
from sqlalchemy.future.engine import Engine

# Criar diretório e arquivos (Usado no SQLite)
from pathlib import Path
# Tipagem de dados que o caracteriza como um dado opcional
from typing import Optional

# CRUD nas tabelas no banco de dados, precisamos instanciar essa classe base
from models.model_base import ModelBase

# capturar a variavel de ambiente
from os import getenv

# carregara as variaveis de ambiente
from dotenv import load_dotenv
load_dotenv()

# usamos a engine para realizar a conexão com o banco de dados
# definir qual vai ser a connection com qual o banco
__engine: Optional[Engine] = None

def create_engine(sqlite:bool = False):
    global __engine
    
    if __engine:
        return
    
    if sqlite:
        file_db = 'db/picoles.sqlite'
        folder = Path(file_db).parent
        # Vai criar o arquivo caso não exista, se já existir, não vai fazer nada
        folder.mkdir(parents=True, exist_ok=True)
        
        conn = f'sqlite:///{file_db}'
        __engine = sa.create_engine(url=conn, echo=False, connect_args={'check_same_thread' : False})
        
    else:
        conn = f'postgres://{getenv("PGSQL_USERNAME")}:{getenv("PGSQL_PASSWORD")}@localhost:5432/picoles'