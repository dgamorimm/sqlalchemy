from typing import Optional

from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint

from datetime import datetime


class Revendedor(SQLModel, table=True):
    __tablename__: str = 'revendedores'
    __table_args__ = (UniqueConstraint("cnpj"),)

    id: Optional[int] = Field(primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)
    
    cnpj: str = Field(max_length=45)
    razao_social: str = Field(max_length=100)
    contato: str = Field(max_length=100)

    def __repr__(self) -> str:
        return f'<Revendedor: {self.razao_social}>'

