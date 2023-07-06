from typing import Optional

from sqlmodel import Field, SQLModel

from datetime import datetime


class Conservante(SQLModel, table=True):

    __tablename__: str = 'conservantes'
    
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime = Field(default=datetime.now, index=True)
    nome: str = Field(max_length=45, unique=True)
    descricao: str = Field(max_length=45)
    
    def __repr__(self) -> str:
        return f'<Conservante: {self.nome}>'