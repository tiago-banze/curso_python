# numeros = [1,2,3,4,5,6,7,8,9,10]

# novos_numeros = [numero/2 for numero in numeros]
# print(numeros)
# print(novos_numeros)

# novos_numeros = [numero for numero in numeros if numero > 5]
# if_ternario = [numero if numero !=6 else 600 for numero in numeros if numero > 5]
# print(novos_numeros)
# print(if_ternario)

# linhas_e_coluna = [
#     (x,y)
#     for x in range(1,11)
#     for y in range(1,6)
#     if x!=2
# ]
# print(linhas_e_coluna)

# set comprrehensions
quadrados_set = {x for x in range(1,21) if x % 2 == 0}
print(f'Tipo: {type(quadrados_set)}\nDados: {quadrados_set}')

#Dict Comprehensions
quadrados_dict = {f'chave_{x}' : x for x in range(1,21) if x % 2 !=0}
print(f'Tipo: {type(quadrados_dict)}\nDados: {quadrados_dict}')
