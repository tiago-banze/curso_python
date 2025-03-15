# # programa que diz se um nr é par ou impar

# numero = 4

# verificar = lambda numero: 'PAR' if numero % 2 ==0 else 'IMPAR' 
# print(verificar(numero))
# #sort()
# lista = ['tiago','banze','victor','zoida','zoada','zaida','zeida']

# lista.sort(reverse=True)
# print(lista)
# Lista de dicionários 
# pessoas = [{'nome': 'João', 'idade': 25}, {'nome': 'Ana', 'idade': 30}, {'nome': 'Carlos', 'idade': 20}] 
# # Ordenar no lugar pela idade usando uma função lambda 
# pessoas.sort(key=lambda pessoa: pessoa['nome']) 
# print(pessoas)

# def soma(x,y):
#     return x+y

# # resultado = soma
# print(soma(2,9))

# resultado1 = lambda x,y: x+y
# print(resultado1(2,9))
# lista_de_listas_de_inteiros = [
#     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
#     [9, 1, 8, 9, 9, 7, 2, 1, 6, 8],
#     [1, 3, 2, 2, 8, 6, 5, 9, 6, 7],
#     [3, 8, 2, 8, 6, 7, 7, 3, 1, 9],
#     [4, 8, 8, 8, 5, 1, 10, 3, 1, 7],
#     [1, 3, 7, 2, 2, 1, 5, 1, 9, 9],
#     [10, 2, 2, 1, 3, 5, 10, 5, 10, 1],
#     [1, 6, 1, 5, 1, 1, 1, 4, 7, 3],
#     [1, 3, 7, 1, 10, 5, 9, 2, 5, 7],
#     [4, 7, 6, 5, 2, 9, 2, 1, 2, 1],
#     [5, 3, 1, 8, 5, 7, 1, 8, 8, 7],
#     [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
# ]
# organizado = lambda lista: sorted(lista)
# for lista in lista_de_listas_de_inteiros:
#     print(organizado(lista))

pessoas = [{'nome': 'João', 'idade': 25}, 
           {'nome': 'Ana', 'idade': 30}, 
           {'nome': 'Carlos', 'idade': 20}]

pessoas.sort(key = lambda x: x['idade'])

print(pessoas)
