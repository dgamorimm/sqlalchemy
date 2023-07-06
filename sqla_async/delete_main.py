"""
    1 - Buscar o registro a ser deletado
    2 - Fazer a deleção do objeto
    3 - Persistir no banco de dados
"""

from typing import Optional

from conf.db_session import create_session

from models.revendedor import Revendedor
from models.picole import Picole

from sqlalchemy.future import select

import asyncio

async def deletar_picole(id_picole:int) -> None:
    async with create_session() as session:
        # Passo 1
        query = select(Picole).where(Picole.id == id_picole)
        resultado = await session.execute(query)
        picole: Picole = resultado.unique().scalar_one_or_none()
        
        if picole:
            # Passo 2 
            await session.delete(picole)
            # Passo 3
            await session.commit()
        else:
            print(f'Não encontrei picolé com ID {id_picole}')

async def deletar_revendedor(id_revendedor:int) -> None:
    async with create_session() as session:
        # Passo 1
        query = select(Revendedor).where(Revendedor.id == id_revendedor)
        resultado = await session.execute(query)
        revendedor: Revendedor = resultado.scalar_one_or_none()
        
        if revendedor:
            # Passo 2 
            await session.delete(revendedor)
            # Passo 3
            await session.commit()
        else:
            print(f'Não encontrei revendedor com ID {id_revendedor}')

async def deletando_picole():
    from select_main import select_filtro_picole
    
    id_picole = 21
    
    # Antes
    await select_filtro_picole(id_picole=id_picole)
    
    # Deletando
    await deletar_picole(id_picole=id_picole)
    
    # Depois
    await select_filtro_picole(id_picole=id_picole)
    

async def deletando_revendedor():
    from select_main import select_filtro_revendedor
    
    # -- 3: Não vinculado em uma nota fiscal
    id_revendedor_nv = 1
    # -- 6: Vinculado em uma nota fiscal
    id_revendedor_v = 6
    
    # Antes
    await select_filtro_revendedor(id_revendedor=id_revendedor_v)
    
    # Deletando
    await deletar_revendedor(id_revendedor=id_revendedor_v)
    
    # Depois
    await select_filtro_revendedor(id_revendedor=id_revendedor_v)

if __name__ == '__main__':
    # asyncio.run(deletando_picole())
    asyncio.run(deletando_revendedor())