# Problema dos parâmetros mutáveis em funções python

def adiciona_clientes(nome, lista=None):
    if lista is None:
        lista = []
    lista.append(nome)
    return lista
# lista = []
# lista1 = []
first_list = adiciona_clientes('Tiago')
secund_list = adiciona_clientes('banze')
print(first_list)
print(secund_list)