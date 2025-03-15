#desempacotamento em chamadas
# de métodos e funções
string = 'ABCD'
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduardo']
tupla = 'python', 'é', 'legal'

# a,b,c, *_ = lista
# print (a,c)
# for nome in lista:
#     print(nome,  end=' ')
print(*lista)
print(*tupla)
print(*string)