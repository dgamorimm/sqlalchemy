from typing import List
from rich import print

from sqlalchemy import func  # Funções de agregação

from conf.helpers import formata_data
from conf.db_session import create_session

# Select Simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

# Select Compostos / Complexos
from models.picole import Picole

## Select Simples -> SELECT * FROM aditivos_nutritivos
def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        # Forma 1 - Esse retorna em formato de objeto
        # aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo)
        
        # Forma 2 - Esse retorna em formato de lista
        aditivos_nutritivos: List[AditivoNutritivo] = session.query(AditivoNutritivo).all()
        
        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data Criação: {formata_data(an.data_criacao)}')
            print(f'Nome: {an.nome}')
            print(f'Fórmula Química: {an.formula_quimica}')

# SELECT * FROM sabores WHERE id = <numero>
def select_filtro_sabor(id_sabor:int) -> None:
    with create_session() as session:
        # Forma 1 - caso não encontre vai retornar nulo(None)
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).first()
        
        # Forma 2  - caso não encontre vai retornar nulo(None) (Remendado) - Função nomeada explicitamente
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        
        # Forma 3  - exec.NoResultFound caso não encontre
        # sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one()
        
        # Forma 4  - usando where ao invés de filter (one(), one_or_none(), first())
        sabor: Sabor = session.query(Sabor).where(Sabor.id == id_sabor).one_or_none()
        
        print(f'ID: {sabor.id}')
        print(f'Data Criação: {formata_data(sabor.data_criacao)}')
        print(f'Nome: {sabor.nome}')

def select_complexo_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).all()
        for picole in picoles:
            print(f'\nID: {picole.id}')
            print(f'Data Criação: {formata_data(picole.data_criacao)}')
            print(f'Preço: {picole.preco}')
            
            print(f'ID Sabor: {picole.id_sabor}')
            print(f'Sabor: {picole.sabor.nome}')
            
            print(f'ID Embalagem: {picole.id_tipo_embalagem}')
            print(f'Embalagem: {picole.tipo_embalagem.nome}')
            
            print(f'ID Tipo Picolé: {picole.id_tipo_picole}')
            print(f'Tipo Picolé: {picole.tipo_picole.nome}')
            
            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Conservantes: {picole.conservantes}')
            print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')

# SELECT * FROM sabores ORDER BY data_criacao DESC
def select_order_by_sabor() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).order_by(Sabor.data_criacao.desc()).all()
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Data Criação: {formata_data(sabor.data_criacao)}')
            print(f'Nome: {sabor.nome}')

# SELECT * FROM picoles GROUP BY id, id_tipo_picole 
def select_group_by_picole() -> None:
    with create_session() as session:
        picoles: List[Picole] = session.query(Picole).group_by(Picole.id, Picole.id_tipo_picole).all()
        for picole in picoles:
            print(f'\nID: {picole.id}')
            print(f'Tipo Picolé: {picole.tipo_picole.nome}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')

# SELECT * FROM sabores LIMIT 25
def select_limit() -> None:
    with create_session() as session:
        sabores: List[Sabor] = session.query(Sabor).limit(25).all()
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Data Criação: {formata_data(sabor.data_criacao)}')
            print(f'Nome: {sabor.nome}')

# SELECT COUNT(*) FROM revendedores
def select_count_revendedor() -> None:
    with create_session() as session:
        qtd: List[Revendedor] = session.query(Revendedor).count()
        print(f'Total de Revendedores: {qtd}')

def select_agregacao() -> None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('média'),
            func.min(Picole.preco).label('mínimo'),
            func.max(Picole.preco).label('máximo'),
        ).all()
        
        print(f'Resultado: {resultado}')
        
        print(f'A soma de todos os picolés é: {resultado[0][0]}')
        print(f'A média de todos os picolés é: {resultado[0][1]}')
        print(f'O picolé mais barato é: {resultado[0][2]}')
        print(f'A picolé mais caro é: {resultado[0][3]}')

if __name__ == '__main__' :
    # select_todos_aditivos_nutritivos()
    # select_filtro_sabor(21)
    # select_complexo_picole()
    # select_order_by_sabor()
    # select_group_by_picole()
    # select_limit()
    # select_count_revendedor()
    select_agregacao()