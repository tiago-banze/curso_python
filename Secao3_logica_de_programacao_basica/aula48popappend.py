"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis:
    append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista [3] ='tiago'
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(100)
removido=lista.pop()# remove o ultimo elemento da lista 

print(f'dados da lista = {lista}, dado removido da lista = {removido}' )