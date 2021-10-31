import MySQLdb

def conectar():
    try:
        conn = MySQLdb.connect(
                db='pmysql',
                host='localhost',
                user='caiozim',
                passwd='caiozim'
            )
        print('Connectado ao Mysql!')
        return conn
    except MySQLdb.Error as e:
        print(f'Error na conexão do Mysql server: {e}')
   

def desconectar(conn):
    conn.close()

def listar():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()

    if len(produtos) > 0:
        print(produtos)
    else:
        print('Não existe produtos cadastrados!')
    desconectar(conn)


def inserir():
    conn = conectar()
    cursor = conn.cursor()
    
    nome = input('Nome do produto: ')
    preco = float(input('Preco do produto: '))
    estoque = int(input('Quantidade de produtos: '))

    cursor.execute(f"INSERT INTO produtos (nome, preco, estoque) VALUES ('{nome}', {preco}, {estoque})")
    conn.commit()
    
    if (cursor.rowcount == 1):
        print('Dados inseridos com sucesso!')
    else:
        print('Não foi possível inserir dados!')

def atualizar():
    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Digite o id a ser atualizado: '))
    nome = input('Digite o nome do produto: ')
    preco = float(input('Digite o preco do produto: '))
    estoque = int(input('Digite o valor do estoque: '))

    cursor.execute(f"UPDATE produtos SET nome='{nome}', preco={preco}, estoque={estoque} WHERE id = {id}")
    conn.commit()
    if(cursor.rowcount == 1):
        print('Os dados foram atualizados.')
    else:
        print('Não foi possível atualizar os dados.')


def deletar():
    conn = conectar()
    cursor = conn.cursor()

    id = int(input('Digite o ID para ser deletado: '))
    cursor.execute(f'DELETE FROM produtos WHERE id = {id}')
    conn.commit()

    if (cursor.rowcount == 1):
        print('Produto excluído com sucesso!')
    else:
        print('Não foi possível excluir o produto!')

def menu():
    print('===============Gerenciamento de produtos===============')
    print('Selecione uma opcão: ')
    print('1 - Listar produtos')
    print('2 - Inserir produtos')
    print('3 - Atualizar produto')
    print('4 - Deletar produto')

    opcao = int(input('Digite uma opcao: '))

    if(opcao == 1):
        listar()
    elif (opcao ==2):
        inserir()
    elif (opcao == 3):
        atualizar()
    elif (opcao == 4):
        deletar()
