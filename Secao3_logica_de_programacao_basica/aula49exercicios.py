"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['maria', 'Helena', 'Luiz']
lista.append('tiago')
# indice = 0
indices = range (len(lista))
for indice in indices:
    print(lista[indice], ' está no indice ', indice)
    # indice +=1