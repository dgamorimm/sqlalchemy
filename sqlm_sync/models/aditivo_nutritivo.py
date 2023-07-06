from typing import Optional

from sqlmodel import Field, SQLModel

from datetime import datetime

# table = True => informa que ele vai ser uma tabela do banco de dados e não só um objeto python
class AditivoNutritivo(SQLModel, table=True):
    # nome da tabela
    __tablename__: str = 'aditivos_nutritivos'
    
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    # datetime.now => informa qual a função que deve ser executada, mas ela não é executada
    """
        index => é uma estrutura de dados usada para melhorar o desempenho de consultas 
        em bancos de dados tem que tomar cuidado ao usar para overhead em operações de inserção, 
        atualização e exclusão de registros. Portanto, é recomendável avaliar cuidadosamente 
        quais colunas devem ser indexadas com base nas consultas frequentes realizadas
        no banco de dados.
    """
    data_criacao: datetime = Field(default=datetime.now, index=True)
    # unique => o nome tem que ser único
    # nullable => não pode ser nulo, ou seja, tem que estar preenchido
    # max_length => quantidade de caracteres
    nome: str = Field(max_length=45, unique=True)
    formula_quimica: str = Field(max_length=100, unique=True)
    
    # Mostra como a minha classe quer ser reprensentada
    def __repr__(self) -> str:
        return f'<Aditivo Nutritivo: {self.nome}>'