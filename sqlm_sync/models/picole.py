from typing import Optional, List

from sqlmodel import Field, SQLModel, Relationship

from pydantic import condecimal

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
    id_conservante: Optional[int] = Field(foreign_key='conservantes.id')

# Picole pode ter vários aditivos nutritivos
class AditivosNutritivosPicole(SQLModel, table=True):
    __tablename__ = 'aditivos_nutritivos_picole'
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    id_picole: Optional[int] = Field(foreign_key='picoles.id')
    id_aditivo_nutritivo: Optional[int] = Field(foreign_key='aditivos_nutritivos.id')

class Picole(SQLModel, table=True):

    __tablename__: str = 'picoles'
    
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime = Field(default=datetime.now, index=True)
    
    preco: condecimal(max_digits=5, decimal_places=2) = Field(default=0)
    
    id_sabor: Optional[int] = Field(foreign_key='sabores.id')
    sabor: Sabor = Relationship(lazy='joined')
    
    id_tipo_embalagem: Optional[int] = Field(foreign_key='tipos_embalagem.id')
    tipo_embalagem: TipoEmbalagem = Relationship(lazy='joined')
    
    id_tipo_picole: Optional[int] = Field(foreign_key='tipos_picole.id')
    tipo_picole: TipoPicole = Relationship(lazy='joined')
    
    # Um picole pode ter vários ingredientes
    ingredientes: List[Ingrediente] = Relationship(link_model=IngredientesPicole, back_populates='ingrediente', lazy='joined')
    
    # Um picole pode ter vários conservantes ou mesmo nenhum
    conservantes: Optional[List[Conservante]] = Relationship(link_model=ConservantesPicole, back_populates='conservante', lazy='joined')
    
    # Um picole pode ter vários aditivos nutritivos ou mesmo nenhum
    aditivos_nutritivos: Optional[List[AditivoNutritivo]] = Relationship(link_model=AditivosNutritivosPicole, back_populates='aditivo_nutritivo', lazy='joined')
    
    def __repr__(self) -> str:
        return f'<Picole: {self.tipo_picole.nome} com sabor {self.sabor.nome} e preço {self.preco}>'