import asyncio

"""
1 - Buscar o registro a ser atualizado;
2 - Faz as alterações no registro;
3 - Salva o registro no banco de dados;
"""
from conf.db_session import create_session

from sqlmodel import select

from models.sabor import Sabor
from models.picole import Picole


async def select_filtro_picole(id_picole: int) -> None:
    async with create_session() as session:
        picole: Picole = await session.get(Picole, id_picole)

        if picole:
            print(f'ID: {picole.id}')
            print(f'Sabor: {picole.sabor.nome}')
            print(f'Preço: {picole.preco}')
        else:
            print('Não existe o picole com o id informado')



async def atualizar_sabor(id_sabor: int, novo_nome: str) -> None:
    async with create_session() as session:
        # Passo 1
        sabor: Sabor = await session.get(Sabor, id_sabor)

        if sabor:
            # Passo 2
            sabor.nome = novo_nome
            # Passo 3
            await session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')



async def atualizar_picole(id_picole: int, novo_preco: float, novo_sabor: int = None):
    async with create_session() as session:
        # Passo 1
        picole: Picole = await session.get(Picole, id_picole)

        if picole:
            # Passo 2
            picole.preco = novo_preco
            # Se quisermos alterar o sabor também....
            if novo_sabor:
                picole.id_sabor = novo_sabor
            # Passo 3
            await session.commit()
        else:
            print(f'Não existe picole com id {id_picole}')


async def atualiza_sabor():
    from select_main import select_filtro_sabor

    id_sabor = 42

    # # Antes
    await select_filtro_sabor(id_sabor=id_sabor)

    # # # Atualizando
    await atualizar_sabor(id_sabor=id_sabor, novo_nome='Banana')

    # # # Depois
    await select_filtro_sabor(id_sabor=id_sabor)


async def atualiza_picole():
    id_picole = 21
    novo_preco = 6.66
    id_novo_sabor = 42

    # Antes
    await select_filtro_picole(id_picole=id_picole)

    # Atualizando
    await atualizar_picole(id_picole=id_picole, novo_preco=novo_preco, novo_sabor=id_novo_sabor)

    # Depois
    await select_filtro_picole(id_picole=id_picole)



if __name__ == '__main__':
    # asyncio.run(atualiza_sabor())
    
    asyncio.run(atualiza_picole())
