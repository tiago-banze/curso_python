# # programa que filtra numeros pares de duplicar os mesmo

# numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,12,14]

# lista_de_nrs_pares_duplicado = [par *2 for par in numeros if par % 2 == 0]

# print (lista_de_nrs_pares_duplicado)

# # Filtrar numa lista strings como comprimento >= 5

# palavras = ['python','é','muito','legal','e', 'poderoso']

# filtro_de_string = [string for string in palavras if len(string) >= 5] 

# print(filtro_de_string)
import pprint

def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'nome': 'p1', 'preco': 20, },
    {'nome': 'p2', 'preco': 10, },
    {'nome': 'p3', 'preco': 30, },
]

filtro = [valor for valor in produtos if valor['preco'] > 10]

p(filtro)
print()

p(produtos)