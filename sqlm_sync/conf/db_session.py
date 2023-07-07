# Criar o motor do banco de dados
from sqlalchemy.future.engine import Engine

# Criar diretório e arquivos (Usado no SQLite)
from pathlib import Path
# Tipagem de dados que o caracteriza como um dado opcional
from typing import Optional

from sqlmodel import Session
from sqlmodel import create_engine as _create_engine
from sqlmodel import SQLModel

# capturar a variavel de ambiente
from os import getenv

# carregara as variaveis de ambiente
from dotenv import load_dotenv
load_dotenv()

# usamos a engine para realizar a conexão com o banco de dados
# definir qual vai ser a connection com qual o banco
__engine: Optional[Engine] = None

def create_engine(sqlite:bool = False) -> Engine:
    """
        Função para configurar a conexão ao banco de dados
    """
    global __engine
    
    if __engine:
        return
    
    if sqlite:
        file_db = 'db/picoles.sqlite'
        folder = Path(file_db).parent
        # Vai criar o arquivo caso não exista, se já existir, não vai fazer nada
        folder.mkdir(parents=True, exist_ok=True)
        
        conn = f'sqlite:///{file_db}'
        __engine = _create_engine(url=conn, echo=False, connect_args={'check_same_thread' : False})
        
    else:
        # Echo = True, você consegue ver no inicio da execução a query sendo montada no seu banco
        conn = f'postgresql://{getenv("PGSQL_USERNAME")}:{getenv("PGSQL_PASSWORD")}@localhost:5432/picoles'
        __engine = _create_engine(url=conn, echo=False)

    return __engine

def create_session() -> Session:
    """
        Função para criar a sessão de conexão ao banco de dados
    """
    global __engine
    
    if not __engine:
        create_engine()  # Se não usar o Postgres => create_engine(sqlite=True)
    
    session: Session = Session(__engine)
    
    return session

def create_tables() -> None:
    global __engine
    
    if not __engine:
        create_engine()
    
    import models.__all_models
    # Vai apagar todas a tabelas
    SQLModel.metadata.drop_all(__engine)
    #Vai criar todas as tabelas
    SQLModel.metadata.create_all(__engine)