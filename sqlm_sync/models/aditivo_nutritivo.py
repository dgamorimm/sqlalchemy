from typing import Optional

from sqlmodel import Field, SQLModel
from sqlalchemy import UniqueConstraint

from datetime import datetime


class AditivoNutritivo(SQLModel, table=True):
    __tablename__: str = 'aditivos_nutritivos'
    __table_args__ = (UniqueConstraint("nome"), UniqueConstraint("formula_quimica"))

    id: Optional[int] = Field(default=None, primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)
    
    nome: str = Field(max_length=45)
    formula_quimica: str = Field(max_length=100)

    def __repr__(self) -> str:
        return f'<Aditivo Nutritivo: {self.nome}>'

