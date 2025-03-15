Produtos = [
    {'nome': 'Produto 5', 'preco': 10.0},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90}
]

novos_produtos = filter(
    lambda p:p['preco'] >10, 
    Produtos
)

print(*novos_produtos, sep='\n')