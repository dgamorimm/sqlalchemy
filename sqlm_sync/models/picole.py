from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from datetime import datetime
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.aditivo_nutritivo import AditivoNutritivo

# Picole pode ter vários ingredientes
class IngredientesPicole(SQLModel, table=True):
    __tablename__ = 'ingredientes_picole'
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    id_picole: Optional[int] = Field(foreign_key='picoles.id')
    id_ingrediente: Optional[int] = Field(foreign_key='ingredientes.id')

# Picole pode ter vários conservantes
class ConservantesPicole(SQLModel, table=True):
    __tablename__ = 'conservantes_picole'
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    id_picole: Optional[int] = Field(foreign_key='picoles.id')
    id_conservantes: Optional[int] = Field(foreign_key='conservantes.id')

# Picole pode ter vários aditivos nutritivos
class AditivosNutritivosPicole(SQLModel, table=True):
    __tablename__ = 'aditivos_nutritivos_picole'
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    id_picole: Optional[int] = Field(foreign_key='picoles.id')
    id_conservantes: Optional[int] = Field(foreign_key='aditivos_nutritivos.id')

class Picole(ModelBase):

    __tablename__: str = 'picoles'
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    
    preco: float = sa.Column(sa.DECIMAL(8,2), nullable=False)
    
    id_sabor: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey('sabores.id'))
    sabor: orm.Mapped[Sabor] = orm.relationship('Sabor', lazy='joined')
    
    id_tipo_embalagem: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey('tipos_embalagem.id'))
    tipo_embalagem: orm.Mapped[TipoEmbalagem] = orm.relationship('TipoEmbalagem', lazy='joined')
    
    id_tipo_picole: orm.Mapped[int] = orm.mapped_column(sa.Integer, sa.ForeignKey('tipos_picole.id'))
    tipo_picole: orm.Mapped[TipoPicole] = orm.relationship('TipoPicole', lazy='joined')
    
    # Um picole pode ter vários ingredientes
    ingredientes: orm.Mapped[List[Ingrediente]] = orm.relationship('Ingrediente', secondary=ingredientes_picole, backref='ingrediente', lazy='joined')
    
    # Um picole pode ter vários conservantes ou mesmo nenhum
    conservantes: orm.Mapped[Optional[List[Conservante]]] = orm.relationship('Conservante', secondary=conservantes_picole, backref='conservante', lazy='joined')
    
    # Um picole pode ter vários aditivos nutritivos ou mesmo nenhum
    aditivos_nutritivos: orm.Mapped[Optional[List[AditivoNutritivo]]] = orm.relationship('AditivoNutritivo', secondary=aditivos_nutritivos_picole, backref='aditivo_nutritivo', lazy='joined')
    
    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'