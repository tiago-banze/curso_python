# map - para mapear dados
from functools import partial
from types import GeneratorType
def print_iter(iterator):
    print(*list(iterator), sep = '\n')
    print()
    
Produtos = [
    {'nome': 'Produto 5', 'preco': 10.0},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]

def aumentar_percentagem(valor, porcentagem):
    return round(valor*porcentagem, 2)

aumentar_dez_porcento = partial(
    aumentar_percentagem,
    porcentagem = 1.5
)

# novos_produtos = [
#     {**p, 'preco':aumentar_percentagem(p['preco'],1.5)} 
#     for p in Produtos
# ]
def muda_preco_de_Produto(prod):
    return{
        **prod,
        'preco':aumentar_dez_porcento(
            prod['preco']
        )
    }
novos_produtos = map(muda_preco_de_Produto,
                     Produtos
                     )
print_iter(Produtos)
print_iter(novos_produtos)
print(isinstance(novos_produtos, GeneratorType))