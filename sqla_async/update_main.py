"""
    1 - Buscar o registro a ser atualizado
    2 - Faz as alterações no registro
    3 - Salva o registro no banco de dados
"""
from conf.db_session import create_session

from models.sabor import Sabor
from models.picole import Picole

def atualizar_sabor(id_sabor:int, novo_nome:str) -> None:
    with create_session() as session:
        # Passo 1
        sabor: Sabor = session.query(Sabor).filter(Sabor.id == id_sabor).one_or_none()
        
        # Passo 2
        if sabor:
            sabor.nome = novo_nome
            
            # Passo 3
            session.commit()
        else:
            print(f'Não existe sabor com ID {id_sabor}')
            
def atualizar_picole(id_picole:int, novo_preco:float, novo_sabor:int = None) -> None:
    with create_session() as session:
        # Passo 1
        picole: Picole = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        
        # Passo 2
        if picole:
            picole.preco = novo_preco
            # Se quisermos alterar o sabor também...
            if novo_sabor:
                picole.id_sabor = novo_sabor
            
            # Passo 3
            session.commit()
        else:
            print(f'Não existe picolé com ID {id_picole}')

if __name__ == '__main__':
    # from select_main import select_filtro_sabor
    # id_sabor = 42
    
    # # Antes
    # select_filtro_sabor(id_sabor=id_sabor)
    
    # # Atualizando
    # atualizar_sabor(id_sabor=id_sabor, novo_nome='Abacate')
    
    # # Depois
    # select_filtro_sabor(id_sabor=id_sabor)
    from select_main import select_filtro_picole
    
    id_picole = 21
    novo_preco = 9.99
    id_novo_sabor = 42
    
    # Antes
    select_filtro_picole(id_picole=id_picole)
    
    # Atualizando
    atualizar_picole(id_picole=id_picole, novo_preco=novo_preco, novo_sabor=id_novo_sabor)
    
    # Depois
    select_filtro_picole(id_picole=id_picole)