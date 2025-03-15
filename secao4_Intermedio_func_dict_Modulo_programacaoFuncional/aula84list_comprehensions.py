# Criar lista de numeros ao quadrado

# numeros = [1,3,4,5,6,7,8,9,0,12,34,54,23]


# quadrados = [x**2 for x in numeros]
# print(quadrados)

# # Filtro na lista numero pares e colocar numa nova lista

# numeros_pares = [
#     x 
#     for x in numeros 
#     if x % 2 == 0 
#     if x !=0
#     ] 

# print(f'\n{numeros_pares}')

# # Combinar duas listas em um tupla
# lista_nomes = ['tiago', 'nelia', 'dercia']
# lista_idades = [26,26,22]

# combinado = [
#     (nome, idade) 
#     for nome , idade in zip(lista_nomes, lista_idades)
#     ]

# print(f'\n{combinado}')
# import random

# random.randint(1 ,10)

# numeros =[]
# for i in range(20):
#     numero_aleatorio= random.randint(1,20)
#     numeros.append(numero_aleatorio)
# numeros = [
#     random.randint(1,10)
#     for _ in range(20) 
#     ]
    
# print(numeros)
# texto = 'P4yth)on] &L@ang**uage'

# letras_puras =''.join( [letra for letra in texto if letra.isspace() or letra.isalpha()])

# print(letras_puras)

# Caso 1: Dobrar o valor de um produto
# Caso 2: Todos os productos que custarem acima de 1.000 dolares, imposto de 50% sobre o valor total

lista_de_preco = [500, 1500, 2000, 100, 25]

dobrar_preco = [preco*2 for preco in lista_de_preco] # Caso 1
imposto = [preco + (preco * 0.5) if preco > 1000 else preco for preco in lista_de_preco] # Caso 2


# print(dobrar_preco)
print(lista_de_preco)
print(imposto)