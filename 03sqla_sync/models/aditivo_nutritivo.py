import sqlalchemy as sa

from datetime import datetime

from models.model_base import ModelBase

class AditivoNutritivo(ModelBase):
    # nome da tabela
    __tablename__: str = 'aditivos_nutritivos'
    
    id: int = sa.Column(sa.BigInteger, primary_key=True, autoincrement=True)
    # datetime.now => informa qual a função que deve ser executada, mas ela não é executada
    """
        index => é uma estrutura de dados usada para melhorar o desempenho de consultas 
        em bancos de dados tem que tomar cuidado ao usar para overhead em operações de inserção, 
        atualização e exclusão de registros. Portanto, é recomendável avaliar cuidadosamente 
        quais colunas devem ser indexadas com base nas consultas frequentes realizadas
        no banco de dados.
    """
    data_criacao: datetime = sa.Column(sa.DateTime, default=datetime.now, index=True)
    # unique => o nome tem que ser único
    # nullable => não pode ser nulo, ou seja, tem que estar preenchido
    nome: str = sa.Column(sa.String(45), unique=True, nullable=False)
    formula_quimica: str = sa.Column(sa.String(45), unique=True, nullable=False)
    
    # Mostra como a minha classe quer ser reprensentada
    def __repr__(self) -> str:
        return f'<Aditivo Nutritivo: {self.nome}>'