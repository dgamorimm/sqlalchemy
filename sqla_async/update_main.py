"""
    1 - Buscar o registro a ser atualizado
    2 - Faz as alterações no registro
    3 - Salva o registro no banco de dados
"""
from conf.db_session import create_session

from models.sabor import Sabor
from models.picole import Picole

from sqlalchemy.future import select

import asyncio

async def atualizar_sabor(id_sabor:int, novo_nome:str) -> None:
    async with create_session() as session:
        # Passo 1
        query = select(Sabor).where(Sabor.id == id_sabor)
        resultado = await session.execute(query)
        sabor: Sabor = resultado.scalar_one_or_none()
        
        # Passo 2
        if sabor:
            sabor.nome = novo_nome
            
            # Passo 3
            await session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')
            
async def atualizar_picole(id_picole:int, novo_preco:float, novo_sabor:int = None) -> None:
    async with create_session() as session:
        # Passo 1
        query = select(Picole).where(Picole.id == id_picole)
        resultado = await session.execute(query)
        picole: Picole = resultado.unique().scalar_one_or_none()
        
        # Passo 2
        if picole:
            picole.preco = novo_preco
            # Se quisermos alterar o sabor também...
            if novo_sabor:
                picole.id_sabor = novo_sabor
            
            # Passo 3
            await session.commit()
        else:
            print(f'Não existe picolé com ID {id_picole}')

async def atualizando_sabor():
    from select_main import select_filtro_sabor
    id_sabor = 42
    
    # Antes
    await select_filtro_sabor(id_sabor=id_sabor)
    
    # Atualizando
    await atualizar_sabor(id_sabor=id_sabor, novo_nome='Abacate')
    
    # Depois
    await select_filtro_sabor(id_sabor=id_sabor)

async def atualizando_picole():
    from select_main import select_filtro_picole
    
    id_picole = 21
    novo_preco = 9.99
    id_novo_sabor = 42
    
    # Antes
    await select_filtro_picole(id_picole=id_picole)
    
    # Atualizando
    await atualizar_picole(id_picole=id_picole, novo_preco=novo_preco, novo_sabor=id_novo_sabor)
    
    # Depois
    await select_filtro_picole(id_picole=id_picole)

if __name__ == '__main__':
    # asyncio.run(atualizando_sabor())
    asyncio.run(atualizando_picole())