# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)
import copy
produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]
print(produtos)


def aumento_percentagem_produto(lista:list, percentagem:float, preco:str):
    aumento_percentagem = copy.deepcopy(produtos)
    
    for valor_aumento_per in aumento_percentagem:
        valor_aumento_per.update({preco: round((valor_aumento_per[preco] * percentagem)+valor_aumento_per[preco],2)})
    return aumento_percentagem

aumento_10_porcento = aumento_percentagem_produto(produtos, 0.1, 'preco')

    
    
# Gere novos_produtos por deep copy (cópia profunda)
novos_produtos = copy.deepcopy(aumento_10_porcento)


# Ordene os produtos por nome decrescente (do maior para menor)
novos_produtos.sort(key = lambda i :i['nome']  ,reverse=True)
for i in novos_produtos:
    print(i)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
print()
produtos_ordenados_por_nome = copy.deepcopy(produtos)

# Ordene os produtos por preco crescente (do menor para maior)
produtos_ordenados_por_nome.sort(key=lambda i : i['nome'])
print(*produtos_ordenados_por_nome, sep='\n')

# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
print()
produtos_ordenados_por_preco = copy.deepcopy(produtos)
produtos_ordenados_por_preco.sort(key=lambda i :i['preco'])
print(*produtos_ordenados_por_preco, sep='\n')
print()
print(produtos)