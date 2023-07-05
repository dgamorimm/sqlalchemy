"""
    1 - Buscar o registro a ser deletado
    2 - Fazer a deleção do objeto
    3 - Persistir no banco de dados
"""

from typing import Optional

from conf.db_session import create_session

from models.revendedor import Revendedor
from models.picole import Picole

def deletar_picole(id_picole:int) -> None:
    with create_session() as session:
        # Passo 1
        picole: Optional[Picole] = session.query(Picole).filter(Picole.id == id_picole).one_or_none()
        
        if picole:
            # Passo 2 
            session.delete(picole)
            # Passo 3
            session.commit()
        else:
            print(f'Não encontrei picolé com ID {id_picole}')

def deletar_revendedor(id_revendedor:int) -> None:
    with create_session() as session:
        # Passo 1
        revendedor: Optional[Revendedor] = session.query(Revendedor).filter(Revendedor.id == id_revendedor).one_or_none()
        
        if revendedor:
            # Passo 2 
            session.delete(revendedor)
            # Passo 3
            session.commit()
        else:
            print(f'Não encontrei revendedor com ID {id_revendedor}')

if __name__ == '__main__':
    # from select_main import select_filtro_picole
    
    # id_picole = 21
    
    # # Antes
    # select_filtro_picole(id_picole=id_picole)
    
    # # Deletando
    # deletar_picole(id_picole=id_picole)
    
    # # Depois
    # select_filtro_picole(id_picole=id_picole)
    
    from select_main import select_filtro_revendedor
    
    # -- 3: Não vinculado em uma nota fiscal
    id_revendedor_nv = 3
    # -- 6: Vinculado em uma nota fiscal
    id_revendedor_v = 6
    
    # Antes
    select_filtro_revendedor(id_revendedor=id_revendedor_v)
    
    # Deletando
    deletar_revendedor(id_revendedor=id_revendedor_v)
    
    # Depois
    select_filtro_revendedor(id_revendedor=id_revendedor_v)