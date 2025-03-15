# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

nomes = ['Salvador', 'Ubatuba', 'Belo Horizonte']
siglas = ['BA', 'SP', 'MG', 'RJ']

combinado = zip(nomes,siglas)

print(list(combinado))
def zipper(lista1:list, lista2:list):
    intervalo_maximo = min(len(lista1), len(lista2))
    return [
        (lista1[i],lista2[i]) for i in range(intervalo_maximo)
    ]
print(zipper(nomes,siglas))
    