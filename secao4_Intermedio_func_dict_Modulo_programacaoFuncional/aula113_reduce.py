# reduce - faz a redução de um iteravel em um valor
from functools import reduce

Produtos = [
    {'nome': 'Produto 5', 'preco': 10.0},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]

def funcao_do_reduce(acumulador, produto):
    print(f'acumulador: {acumulador}')
    print(f'produto: {produto}')
    return acumulador + produto['preco']

total = reduce(
    funcao_do_reduce,
    Produtos,
    0
)
print(total)