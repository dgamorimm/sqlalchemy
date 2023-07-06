from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from datetime import datetime

from models.revendedor import Revendedor
from models.lote import Lote

# Nota Fiscal pode ter vários lotes
# uma entidade que é de 1 para muitos 1:*
class LotesNotaFiscal(SQLModel, table=True):
    __tablename__ = 'lotes_nota_fiscal'
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    id_nota_fiscal: Optional[int] = Field(foreign_key='notas_fiscais.id')
    id_lote: Optional[int] = Field(foreign_key='lotes.id')

class NotaFiscal(SQLModel, table=True):

    __tablename__: str = 'notas_fiscais'
    
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime = Field(default=datetime.now, index=True)

    valor: float = Field()
    numero_serie: str = Field(max_length=45, unique=True)
    descricao: str = Field(max_length=200)
    
    id_revendedor: Optional[int] = Field(foreign_key='revendedores.id', ondelete='CASCADE')
    revendedor: Revendedor = Relationship('Revendedor', lazy='joined', cascade='delete')
    
    lotes: List[Lote] = Relationship('Lote', link_model=LotesNotaFiscal, back_populates='lote', lazy='dynamic')
    
    def __repr__(self) -> str:
        return f'<Nota Fiscal: {self.numero_serie}>'