'''
enumerate - enumerar iteráveis (índices)
'''

nome = ['maria', 'Helena', 'Luiz']
nome.append('tiago')
lista_enumerada = enumerate(nome, start= 10)
for item in enumerate(nome, start=20):
    print(item)
for item in enumerate(nome):
    indice,valor=item
    print(indice,'  ',valor)