import sqlite3
from pathlib import Path

RAIZ = Path(__file__).parent / 'produtos.sqlite'
conn = sqlite3.Connection(RAIZ)
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS produtos('
    'id integer PRIMARY KEY,' 
    'nome vachar(40),'
    'preco DECIMAL(10,2),'
    'estoque integer'
    ')'
)
conn.commit()

# cursor.execute(
#     'INSERT INTO produtos(id, nome,preco, estoque)'
#     'VALUES'
#     '(1, "peixe", 80,1 )'
# )
def inserir_produtos(id: int, nome:str, preco:float, estoque: int):
   cursor.execute(
    'INSERT INTO produtos(id, nome,preco, estoque)'
    'VALUES'
    f'({id},"{nome}" , {preco},{estoque} )'
    )
   print("registo adicionado com sucesso!")

# inserir_produtos(3,"bolacha Maria",40, 4)

cursor.execute('SELECT * FROM produtos')
lista_produtos = cursor.fetchall()
for i,valor in enumerate(lista_produtos):
    # print(type(valor))
    print(f'produto {i+1} = {valor[1]}')
# print(lista_produtos)
conn.commit()
cursor.close()
conn.close()

# print(RAIZ)