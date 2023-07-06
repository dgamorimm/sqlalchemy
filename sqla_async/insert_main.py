from rich import print
import asyncio

from conf.db_session import create_session

# Insert Parte I
from models.aditivo_nutritivo import AditivoNutritivo
from models.sabor import Sabor
from models.tipo_embalagem import TipoEmbalagem
from models.tipo_picole import TipoPicole
from models.ingrediente import Ingrediente
from models.conservante import Conservante
from models.revendedor import Revendedor

# Insert Parte II
from models.lote import Lote
from models.nota_fiscal import NotaFiscal
from models.picole import Picole

# 1 Aditivo Nutritivo
async def insert_aditivo_nutritivo() -> AditivoNutritivo:
    print('Cadastrando aditivo nutritivo')
    
    nome: str = input('Informe o nome do Aditivo Nutritivo: ')
    formula_quimica: str = input('Informe a fórmula química do aditivo: ')
    
    an: AditivoNutritivo = AditivoNutritivo(
        nome=nome,
        formula_quimica=formula_quimica
    )
    
    async with create_session() as session:
        session.add(an)
        await session.commit()
        
        # return an
    
        print('Aditivo Nutritivo cadastrado com sucesso')
        print(f'ID: {an.id}')
        print(f'Data Criação: {an.data_criacao}')
        print(f'Nome: {an.nome}')
        print(f'Fórmula Química: {an.formula_quimica}')
    
# 2 Sabor
async def insert_sabor() -> None:
    print('Cadastrando sabor')
    
    nome: str = input('Informe o nome do sabor: ')
    
    sabor: Sabor = Sabor(nome=nome)
    
    async with create_session() as session:
        session.add(sabor)
        await session.commit()
    
        print('Sabor cadastrado com sucesso')
        print(f'ID: {sabor.id}')
        print(f'Data Criação: {sabor.data_criacao}')
        print(f'Nome: {sabor.nome}')

# 3 Tipo de Embalagem
async def insert_tipo_embalagem() -> None:
    print('Cadastrando tipo de embalagem')
    
    nome: str = input('Informe o nome do tipo de embalagem: ')
    
    te: TipoEmbalagem = TipoEmbalagem(nome=nome)
    
    async with create_session() as session:
        session.add(te)
        await session.commit()
    
        print('Tipo de embalagem cadastrado com sucesso')
        print(f'ID: {te.id}')
        print(f'Data Criação: {te.data_criacao}')
        print(f'Nome: {te.nome}')
    
# 4 Tipo de Picolé
async def insert_tipo_picole() -> None:
    print('Cadastrando tipo de picolé')
    
    nome: str = input('Informe o nome do tipo de picolé: ')
    
    tp: TipoPicole = TipoPicole(nome=nome)
    
    async with create_session() as session:
        session.add(tp)
        await session.commit()
    
        print('Tipo de picolé cadastrado com sucesso')
        print(f'ID: {tp.id}')
        print(f'Data Criação: {tp.data_criacao}')
        print(f'Nome: {tp.nome}')

# 5 Ingrediente
async def insert_ingrediente() -> Ingrediente:
    print('Cadastrando o ingrediente')
    
    nome: str = input('Informe o nome do ingrediente: ')
    
    ingrediente: Ingrediente = Ingrediente(nome=nome)
    
    async with create_session() as session:
        session.add(ingrediente)
        await session.commit()
    
        # return ingrediente
        
        print('Ingrediente cadastrado com sucesso')
        print(f'ID: {ingrediente.id}')
        print(f'Data Criação: {ingrediente.data_criacao}')
        print(f'Nome: {ingrediente.nome}')

# 6 Conservante
async def insert_conservante() -> Conservante:
    print('Cadastrando o conservante')
    
    nome: str = input('Informe o nome do conservante: ')
    descricao: str = input('Informe a descrição do conservante: ')
    
    conservante: Conservante = Conservante(
        nome=nome,
        descricao=descricao
    )
    
    async with create_session() as session:
        session.add(conservante)
        await session.commit()
    
        # return conservante
        print('Conservante cadastrado com sucesso')
        print(f'ID: {conservante.id}')
        print(f'Data Criação: {conservante.data_criacao}')
        print(f'Nome: {conservante.nome}')
        print(f'Descrição: {conservante.descricao}')
    
# 7 Revendedor
async def insert_revendedor() -> Revendedor:
    print('Cadastrando Revendedor')
    
    cnpj: str = input('Informe o CNPJ do revendedor: ')
    razao_social: str = input('Informe a razão social do revendedor: ')
    contato: str = input('Informe o contato do revendedor: ')
    
    revendedor: Revendedor = Revendedor(
        cnpj=cnpj,
        razao_social=razao_social,
        contato=contato
    )
    
    async with create_session() as session:
        session.add(revendedor)
        await session.commit()
    
        print('Conservante cadastrado com sucesso')
        return revendedor

# 8 Lote
async def insert_lote() -> Lote:
    print('Cadastrando Lote')
    
    id_tipo_picole: int = int(input('Informe o ID do tipo do picolé: '))
    quantidade: int = int(input('Informe a quantidade de picolé: '))
    
    lote: Lote = Lote(
        id_tipo_picole=id_tipo_picole,
        quantidade=quantidade
    )
    
    async with create_session() as session:
        session.add(lote)
        await session.commit()
    
        print('Lote cadastrado com sucesso')
        return lote

# 9 Nota Fiscal
async def insert_nota_fiscal() -> None:
    print('Cadastrando Nota Fiscal')
    
    valor: float = float(input('Informe o valor da nota fiscal: '))
    numero_serie: str = input('Informe o número de série: ')
    descricao: str = input('Informe a descrição: ')
    rev = await insert_revendedor()
    id_revendedor = rev.id
    
    nf: NotaFiscal = NotaFiscal(
        valor=valor,
        numero_serie=numero_serie,
        descricao=descricao,
        id_revendedor=id_revendedor
    )
    
    lote1 = await insert_lote()
    nf.lotes.append(lote1)
    
    lote2 = await insert_lote()
    nf.lotes.append(lote2)
    
    async with create_session() as session:
        session.add(nf)
        await session.commit()
        # para acessar os objetos após o commit, tem que dar o refresh no objeto
        await session.refresh(nf)
    
        print('Nota fiscal cadastrada com sucesso')
        print(f'ID: {nf.id}')
        print(f'Data Criação: {nf.data_criacao}')
        print(f'Valor: {nf.valor}')
        print(f'Número de Série: {nf.numero_serie}')
        print(f'Descrição: {nf.descricao}')
        print(f'ID Revendedor: {nf.id_revendedor}')
        print(f'Revendedor: {nf.revendedor.razao_social}')  # <--- para acessar esse valor é necessário o refresh

# 10 Picolé
async def insert_picole() -> None:
    print('Cadastrando Picolé')
    
    preco: float = float(input('Informe o preço do picolé: '))
    id_sabor: int = int(input('Informe o ID do sabor: '))
    id_tipo_picole: int = int(input('Informe o ID do tipo do picole: '))
    id_tipo_embalagem: int = int(input('Informe o ID do tipo da embalagem: '))
    
    
    picole: Picole = Picole(
        preco=preco,
        id_sabor=id_sabor,
        id_tipo_picole=id_tipo_picole,
        id_tipo_embalagem=id_tipo_embalagem
    )
    
    ingrediente1 = await insert_ingrediente()
    picole.ingredientes.append(ingrediente1)
    ingrediente2 = await insert_ingrediente()
    picole.ingredientes.append(ingrediente2)
    
    # Tem conservantes?
    conservante = await insert_conservante()
    picole.conservantes.append(conservante)
    
    # Tem aditivos nutritivos?
    aditivo_nutritivo = await insert_aditivo_nutritivo()
    picole.aditivos_nutritivos.append(aditivo_nutritivo)
    
    async with create_session() as session:
        session.add(picole)
        await session.commit()
        await session.refresh(picole)
    
        print('Picolé cadastrado com sucesso')
        print(f'ID: {picole.id}')
        print(f'Data Criação: {picole.data_criacao}')
        print(f'Valor: {picole.preco}')
        print(f'Sabor: {picole.sabor.nome}')
        print(f'Tipo Picolé: {picole.tipo_picole.nome}')
        print(f'Tipo da Embalagem: {picole.tipo_embalagem.nome}')
        print(f'Ingredientes: {picole.ingredientes}')
        print(f'Conservantes: {picole.conservantes}')
        print(f'Aditivos Nutritivos: {picole.aditivos_nutritivos}')

if __name__ == '__main__':
    # 1 Aditivo Nutritivo
    # asyncio.run(insert_aditivo_nutritivo())
    
    # 2 Sabor
    # asyncio.run(insert_sabor())
    
    # # 3 Tipo de Embalagem
    # asyncio.run(insert_tipo_embalagem())
    
    # # 4 Tipo de Picolé
    # asyncio.run(insert_tipo_picole())
    
    # # 5 Ingrediente
    # asyncio.run(insert_ingrediente())
    
    # # 6 Conservante
    # asyncio.run(insert_conservante())
    
    # # 7 Revendedor
    # rev = asyncio.run(insert_revendedor())
    # print(f'ID: {rev.id}')
    # print(f'Data Criação: {rev.data_criacao}')
    # print(f'CNPJ: {rev.cnpj}')
    # print(f'Razão Social: {rev.razao_social}')
    # print(f'Contato: {rev.contato}')
    
    # # 8 Lote
    # lote =  asyncio.run(insert_lote())
    # print(f'ID: {lote.id}')
    # print(f'Data Criação: {lote.data_criacao}')
    # print(f'ID_Lote: {lote.id_tipo_picole}')
    # print(f'Quantidade: {lote.quantidade}')
    
    # # 9 Nota Fiscal
    asyncio.run(insert_nota_fiscal())
    
    # # 10 Picolé
    # asyncio.run(insert_picole())