from typing import Optional

from sqlmodel import Field, SQLModel, Relationship

from datetime import datetime

from models.tipo_picole import TipoPicole

class Lote(SQLModel, table=True):

    __tablename__: str = 'lotes'
    
    id: Optional[int] = Field(primary_key=True, autoincrement=True)
    data_criacao: datetime = Field(default=datetime.now, index=True)
    
    # chave estrangeira tipos_picole.id => nomedatabela.colunareferenciada
    id_tipo_picole: Optional[int] = Field(foreign_key='tipos_picole.id')
    tipo_picole: TipoPicole = Relationship(lazy='joined', back_populates='tipo_picole')
    
    quantidade: int = Field()
    
    def __repr__(self) -> str:
        return f'<Lote: {self.id}>'
    
# lazy="select": Imagine que você tenha uma aplicação de blog e cada post tenha uma lista de comentários. Nesse caso, você pode definir o relacionamento entre Post e Comment com lazy="select". Quando você acessar os comentários de um post específico, o SQLAlchemy executará uma consulta adicional para buscar os comentários associados a esse post.

# lazy="joined": Suponha que você esteja desenvolvendo um sistema de gerenciamento de produtos, onde cada produto está associado a uma categoria. Usando lazy="joined", você pode carregar o objeto de categoria junto com o objeto de produto em uma única consulta. Isso evita consultas adicionais ao banco de dados quando você precisa acessar as informações da categoria.

# lazy="subquery": Considere um sistema de comércio eletrônico em que cada produto possa ter várias variantes. Nesse caso, você pode usar lazy="subquery" para evitar o efeito de multiplicação de linhas que ocorreria com lazy="joined". Ao buscar os produtos, as variantes relacionadas serão carregadas usando uma subconsulta.

# lazy="dynamic": Suponha que você esteja desenvolvendo uma aplicação de mídia social, onde cada usuário tem uma lista de amigos. Ao definir lazy="dynamic" para o relacionamento de amigos, você pode obter uma consulta especial que ainda não foi executada. Você pode adicionar filtros adicionais, como amigos online ou amigos de uma determinada cidade, antes de executar a consulta e recuperar os resultados.

# lazy="noload": Imagine que você tenha um modelo de usuário que tenha um relacionamento com um grande número de registros de atividades. Usando lazy="noload", você desativa o carregamento automático das atividades relacionadas. Em vez disso, você pode carregar explicitamente as atividades apenas quando necessário, evitando carregar em massa dados desnecessários.

# lazy="dynamic,noload": Suponha que você esteja trabalhando em um sistema de pesquisa de produtos, onde cada produto tenha uma lista de avaliações. Usando lazy="dynamic,noload", você obtém a flexibilidade de carregar dinamicamente as avaliações apenas quando necessário, mas também desativa o carregamento automático padrão. Isso pode ser útil quando você deseja controlar manualmente o carregamento das avaliações com base em ações do usuário, como rolagem na página.

# Esses são apenas alguns exemplos de como os diferentes valores de lazy podem ser aplicados em situações reais, dependendo dos requisitos e do desempenho desejado para o acesso aos dados.