from typing import Optional

from sqlmodel import Field, SQLModel

from datetime import datetime

class TipoPicole(SQLModel, table=True):

    __tablename__: str = 'tipos_picole'
    
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime = Field(default=datetime.now, index=True)
    nome: str = Field(max_length=45, unique=True)
    
    def __repr__(self) -> str:
        return f'<Tipo Picole: {self.nome}>'