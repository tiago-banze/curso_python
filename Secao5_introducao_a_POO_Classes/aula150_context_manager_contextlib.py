from contextlib import contextmanager
from pathlib import Path

CAMINHO = Path(__file__).parent / 'aula149.txt'
@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("abrindo arquivo")
        arquivo= open(caminho_arquivo, modo, encoding='utf9')
        yield arquivo
    finally:
        print("Fechando o arquivo")
        arquivo.close()
    
with my_open(CAMINHO, 'w') as arquivo:
    arquivo.write('linha 123\nmais linhas\nmais linhas')
    print('WITH', arquivo)