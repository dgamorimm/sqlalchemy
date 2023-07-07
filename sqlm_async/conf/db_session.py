# Criar diretório e arquivos (Usado no SQLite)
from pathlib import Path
# Tipagem de dados que o caracteriza como um dado opcional
from typing import Optional

from sqlmodel import create_engine as _create_engine
from sqlmodel import SQLModel
from sqlmodel.ext.asyncio.session import AsyncSession, AsyncEngine

# capturar a variavel de ambiente
from os import getenv

# carregara as variaveis de ambiente
from dotenv import load_dotenv
load_dotenv()

# usamos a engine para realizar a conexão com o banco de dados
# definir qual vai ser a connection com qual o banco
__async_engine: Optional[AsyncEngine] = None

def create_engine(sqlite:bool = False) -> AsyncEngine:
    """
        Função para configurar a conexão ao banco de dados
    """
    global __async_engine
    
    if __async_engine:
        return
    
    if sqlite:
        file_db = 'db/picoles.sqlite'
        folder = Path(file_db).parent
        # Vai criar o arquivo caso não exista, se já existir, não vai fazer nada
        folder.mkdir(parents=True, exist_ok=True)
        
        conn = f'sqlite+aiosqlite:///{file_db}'
        __async_engine = AsyncEngine(_create_engine(url=conn, echo=False, connect_args={'check_same_thread' : False}))
        
    else:
        # Echo = True, você consegue ver no inicio da execução a query sendo montada no seu banco
        conn = f'postgresql+asyncpg://{getenv("PGSQL_USERNAME")}:{getenv("PGSQL_PASSWORD")}@localhost:5432/picoles'
        __async_engine = AsyncEngine(_create_engine(url=conn, echo=False))

    return __async_engine

def create_session() -> AsyncSession:
    """
        Função para criar a sessão de conexão ao banco de dados
    """
    global __async_engine
    
    if not __async_engine:
        create_engine()  # Se não usar o Postgres => create_engine(sqlite=True)
    
    async_session: AsyncSession = AsyncSession(__async_engine)
    
    return async_session

async def create_tables() -> None:
    global __async_engine
    
    if not __async_engine:
        create_engine()
    
    import models.__all_models
    async with __async_engine.begin() as conn:
        # Vai apagar todas a tabelas
        await conn.run(SQLModel.metadata.drop_all)
        #Vai criar todas as tabelas
        await conn.run(SQLModel.metadata.create_all)