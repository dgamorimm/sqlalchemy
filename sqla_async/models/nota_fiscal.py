import sqlalchemy as sa
import sqlalchemy.orm as orm

from datetime import datetime
from typing import List

from models.model_base import ModelBase
from models.revendedor import Revendedor
from models.lote import Lote

# Nota Fiscal pode ter vários lotes
# uma entidade que é de muitos para muitos *:*
lotes_nota_fiscal = sa.Table(
    'lotes_nota_fiscal',
    ModelBase.metadata,
    sa.Column('id_nota_fiscal', sa.Integer, sa.ForeignKey('notas_fiscais.id')),
    sa.Column('id_lote', sa.Integer, sa.ForeignKey('lotes.id'))
)


class NotaFiscal(ModelBase):

    __tablename__: str = 'notas_fiscais'
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    # DECIMAL(8,2) => 12345678,12
    valor: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    numero_serie: str = sa.Column(sa.String(45), unique=True, nullable=False)
    descricao: str = sa.Column(sa.String(200), nullable=False)
    # ondelete e cascade: Ao fazer a deleção de algum revendedor a tabela de notas fiscais que contem este revendedor, seá apagado, mantendo assim a integridade
    id_revendedor: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey('revendedores.id', ondelete='CASCADE'))
    revendedor: orm.Mapped[Revendedor] = orm.relationship('Revendedor', lazy='joined', cascade='delete')
    
    # uma nota fiscal pode ter varios lotes
    # secundary => configuração da tabela secundária
    # backref='lote' qual é a referencia desta tabela, o nome do qrquicvo da classe Lote
    lotes: orm.Mapped[List[Lote]] = orm.relationship('Lote', secondary=lotes_nota_fiscal, backref='lote', lazy='dynamic')
    
    def __repr__(self) -> str:
        return f'<Nota Fiscal: {self.numero_serie}>'