# combinations, permitations e product - Itertools
# combinação - ordem não importa - iteravel + tamanho do grupo
# permutação - ordem importa
# Produto - Ordem importa e repete valores únicos

from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'joão', 'Joana', 'Luiz', 'Leticia',
]

camisetas = [
    ['preta', 'branca'],
    ['p', 'm','a'],
    ['masculino', 'Feminino', 'Unisex'],
]

print_iter(combinations(pessoas,2))
print_iter(combinations(pessoas,3))
print_iter(permutations(pessoas,2))
print_iter(product(*camisetas))
