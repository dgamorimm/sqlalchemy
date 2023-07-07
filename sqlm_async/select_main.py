from typing import List

from sqlalchemy import func # Funções de agregação 

from sqlmodel import select
from sqlalchemy.future import select as _select


from conf.helpers import formata_data
from conf.db_session import create_session



# Select Simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

# Select Compostos / Complexos
from models.picole import Picole

## Select simples -> SELECT * FROM aditivos_nutritivos;
def select_todos_aditivos_nutritivos() -> None:
    with create_session() as session:
        query = select(AditivoNutritivo)
        aditivos_nutritivos = session.exec(query) # Objeto iterável
        aditivos_nutritivos = aditivos_nutritivos.all() # Lista

        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data: {formata_data(an.data_criacao)}')
            print(f'Nome: {an.nome}')
            print(f'Fórmula Química: {an.formula_quimica}')


# SELECT * FROM sabores WHERE sabor.id == 21;
def select_filtro_sabor(id_sabor: int) -> None:
    with create_session() as session:
        # query = select(Sabor).filter(Sabor.id == id_sabor)
        # query = select(Sabor).where(Sabor.id == id_sabor)
        # resultado = session.exec(query)
        
        # Pode ter vários, pega o primeiro resultado
        # sabor: Sabor = resultado.first() # None
       
        # Execção em não resultado ou mais de 1
        # sabor: Sabor = resultado.one() 
        
        # None se não encontrar
        sabor: Sabor = session.get(Sabor, id_sabor)
       
        print(f'ID: {sabor.id}')
        print(f'Data: {formata_data(sabor.data_criacao)}')
        print(f'Nome: {sabor.nome}')


def select_complexo_picole() -> None:
    with create_session() as session:
        query = select(Picole)
        resultado = session.exec(query)
        picoles: List[Picole] = resultado.unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Data: {formata_data(picole.data_criacao)}')
            print(f'Preço: {picole.preco}')

            print(f'ID Sabor: {picole.id_sabor}')
            print(f'Sabor: {picole.sabor.nome}')

            print(f'ID Embalagem: {picole.id_tipo_embalagem}')
            print(f'Embalagem: {picole.tipo_embalagem.nome}')

            print(f'ID Tipo Picole: {picole.id_tipo_picole}')
            print(f'Tipo Picole: {picole.tipo_embalagem.nome}')

            print(f'Ingredientes: {picole.ingredientes}')
            print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')
            print(f'Conservantes: {picole.conservantes}')


def select_order_by_sabor() -> None:
    with create_session() as session:
        query = select(Sabor).order_by(Sabor.data_criacao.desc())
        resultado = session.exec(query)

        sabores: List[Sabor] = resultado.all()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Nome: {sabor.nome}')


def select_group_by_picole() -> None:
    with create_session() as session:
        query = select(Picole).group_by(Picole.id, Picole.id_tipo_picole)
        resultado = session.exec(query)
        picoles: List[Picole] = resultado.unique().all()

        for picole in picoles:
            print(f'ID: {picole.id}')
            print(f'Tipo Picole: {picole.tipo_picole.nome}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')


def select_limit() -> None:
    with create_session() as session:
        # query = select(Sabor).limit(25)
        query = select(Sabor).offset(25).limit(25)
        resultado = session.exec(query)
        sabores: List[Sabor] = resultado.all()

        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Sabor: {sabor.nome}')


def select_count_revendedor() -> None:
    with create_session() as session:
        qtd: int = session.query(Revendedor).count()

        print(f'Quantidade de revendedores: {qtd}')



def select_agregacao() -> None:
    with create_session() as session:
        resultado: List = session.query(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('media'),
            func.min(Picole.preco).label('mais_barato'),
            func.max(Picole.preco).label('mais_caro'),
        ).all()

        print(f'Resultado: {resultado}')

        print(f'A soma de todos os picolés é: {resultado[0][0]}')
        print(f'A média de todos os picolés é: {resultado[0][1]}')
        print(f'O picolé mais barato é: {resultado[0][2]}')
        print(f'O picolé mais caro é: {resultado[0][3]}')



if __name__ == '__main__':
    # select_todos_aditivos_nutritivos()
    
    # select_filtro_sabor(21)

    # select_complexo_picole()

    # select_order_by_sabor()

    # select_group_by_picole()

    # select_limit()

    select_count_revendedor()

    # select_agregacao()
