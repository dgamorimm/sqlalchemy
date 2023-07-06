import asyncio
from typing import List, Optional
from rich import print

from sqlalchemy import func  # Funções de agregação
from sqlalchemy.future import select

from conf.helpers import formata_data
from conf.db_session import create_session

# Select Simples
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.revendedor import Revendedor

# Select Compostos / Complexos
from models.picole import Picole

## Select Simples -> SELECT * FROM aditivos_nutritivos
async def select_todos_aditivos_nutritivos() -> None:
    async with create_session() as session:
        query = select(AditivoNutritivo)
        resultado = await session.execute(query)
        aditivos_nutritivos: List[AditivoNutritivo] = resultado.scalars().all()
        
        for an in aditivos_nutritivos:
            print(f'ID: {an.id}')
            print(f'Data Criação: {formata_data(an.data_criacao)}')
            print(f'Nome: {an.nome}')
            print(f'Fórmula Química: {an.formula_quimica}')

# SELECT * FROM sabores WHERE id = <numero>
async def select_filtro_sabor(id_sabor:int) -> None:
    async with create_session() as session:
        query = select(Sabor).filter(Sabor.id == id_sabor)
        # query = select(Sabor).where(Sabor.id == id_sabor)
        resultado = await session.execute(query)
        
        # Forma 1  # None - caso não encontre
        # sabor: Sabor = resultado.scalars().first()
        
        # Forma 2  # None - caso não encontre
        # sabor: Sabor = resultado.scalars().one_or_none()
        
        # Forma 3  # Exception - caso não encontre
        # sabor: Sabor = resultado.scalars().one()
        
        # Forma 4  # None - caso não encontre
        sabor: Sabor = resultado.scalar_one_or_none()  # Recomendado
        
        print(f'ID: {sabor.id}')
        print(f'Data Criação: {formata_data(sabor.data_criacao)}')
        print(f'Nome: {sabor.nome}')
        
# SELECT * FROM sabores WHERE id = <numero>
async def select_filtro_picole(id_picole:int) -> None:
    async with create_session() as session:
        query = select(Picole).filter(Picole.id == id_picole)
        resultado = await session.execute(query)
        picole: Picole = resultado.unique().scalar_one_or_none()  # Recomendado
        
        if picole:
            print(f'ID: {picole.id}')
            print(f'Preço: {picole.preco}')
            print(f'ID Sabor: {picole.id_sabor}')
            print(f'Sabor: {picole.sabor.nome}')
        else:
            print('Não existe o picolé com o id informado')

# SELECT * FROM revendedores WHERE id = <numero>
async def select_filtro_revendedor(id_revendedor:int) -> None:
    async with create_session() as session:
        query = select(Revendedor).filter(Revendedor.id == id_revendedor)
        resultado = await session.execute(query)
        revendedor: Revendedor = resultado.scalar_one_or_none()  # Recomendado
        
        if revendedor:
            print(f'ID: {revendedor.id}')
            print(f'Razão Social: {revendedor.razao_social}')
        else:
            print(f'Não encontrei nenhum revendedor com ID {id_revendedor}')

async def select_complexo_picole() -> None:
    async with create_session() as session:
        query = select(Picole)
        resultado = await session.execute(query)
        picoles: List[Picole] = resultado.scalars().unique().all()  # Unique é semelhante ao DISTINCT do SQL
        
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
async def select_order_by_sabor() -> None:
    async with create_session() as session:
        query = select(Sabor).order_by(Sabor.data_criacao.desc())
        resultado = await session.execute(query)
        sabores: List[Sabor] = resultado.scalars().all()
        
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Data Criação: {formata_data(sabor.data_criacao)}')
            print(f'Nome: {sabor.nome}')

# SELECT * FROM picoles GROUP BY id, id_tipo_picole 
async def select_group_by_picole() -> None:
    async with create_session() as session:
        query = select(Picole).group_by(Picole.id, Picole.id_tipo_picole)
        resultado = await session.execute(query)
        picoles: List[Picole] = resultado.scalars().unique().all()
        
        
        for picole in picoles:
            print(f'\nID: {picole.id}')
            print(f'Tipo Picolé: {picole.tipo_picole.nome}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')

# SELECT * FROM sabores LIMIT 25
async def select_limit() -> None:
    async with create_session() as session:
        query = select(Sabor).limit(25)
        resultado = await session.execute(query)
        sabores: List[Sabor] = resultado.scalars()
        
        for sabor in sabores:
            print(f'ID: {sabor.id}')
            print(f'Data Criação: {formata_data(sabor.data_criacao)}')
            print(f'Nome: {sabor.nome}')

# SELECT COUNT(*) FROM revendedores
async def select_count_revendedor() -> None:
    async with create_session() as session:
        query = select(func.count(Revendedor.id))
        resultado = await session.execute(query)
        qtd: int = resultado.scalar()  # scalar só traz um elemento
        print(f'Total de Revendedores: {qtd}')

async def select_agregacao() -> None:
    async with create_session() as session:
        query = select(
            func.sum(Picole.preco).label('soma'),
            func.avg(Picole.preco).label('média'),
            func.min(Picole.preco).label('mínimo'),
            func.max(Picole.preco).label('máximo'),
        )
        resultado = await session.execute(query)
        resultado = resultado.all()
        print(f'Resultado: {resultado}')
        
        print(f'A soma de todos os picolés é: {resultado[0][0]}')
        print(f'A média de todos os picolés é: {resultado[0][1]}')
        print(f'O picolé mais barato é: {resultado[0][2]}')
        print(f'A picolé mais caro é: {resultado[0][3]}')

if __name__ == '__main__' :
    # asyncio.run(select_todos_aditivos_nutritivos())
    # asyncio.run(select_filtro_sabor(21))
    # asyncio.run(select_complexo_picole())
    # asyncio.run(select_order_by_sabor())
    # asyncio.run(select_group_by_picole())
    # asyncio.run(select_limit())
    # asyncio.run(select_count_revendedor())
    asyncio.run(select_agregacao())