from typing import List, Optional

from sqlmodel import Field, SQLModel, Relationship
from sqlalchemy import UniqueConstraint

from pydantic import condecimal

from datetime import datetime

from models.revendedor import Revendedor
from models.lote import Lote

# Nota Fiscal pode ter vários lotes
class LotesNotaFiscal(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    id_nota_fiscal: Optional[int] = Field(default=None, foreign_key='notas_fiscais.id')
    id_lote: Optional[int] = Field(default=None, foreign_key='lotes.id')



class NotaFiscal(SQLModel, table=True):
    __tablename__: str = 'notas_fiscais'
    __table_args__ = (UniqueConstraint("numero_serie"),)

    id: Optional[int] = Field(primary_key=True)
    data_criacao: datetime = Field(default=datetime.now(), index=True)

    valor: condecimal(max_digits=5, decimal_places=2) = Field(default=0)
    numero_serie: str = Field(max_length=45)
    descricao: str = Field(max_length=200)

    id_revendedor: Optional[int] = Field(foreign_key='revendedores.id')
    revendedor: Revendedor = Relationship(sa_relationship_kwargs={"lazy": "joined", "cascade": "delete"})

    # Uma nota fiscal pode ter vários lotes e um lote está ligado a uma nota fiscal
    lotes: List[Lote] = Relationship(link_model=LotesNotaFiscal , sa_relationship_kwargs={"lazy": "dynamic"})

    def __repr__(self) -> int:
        return f'<Nota Fiscal: {self.numero_serie}>'

