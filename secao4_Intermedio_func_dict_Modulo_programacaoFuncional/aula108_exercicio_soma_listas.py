"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
lista_a     = [1, 20, 31, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 48]
def sum_function(l1,l2):
    sum_list = [
        x + y for x , y in zip(l1, l2)
    ]
    return sum_list

# Outra solução
# def sum_function(l1,l2):
#     intervalo_maximo = min(len(l1),len(l2))
#     sum_list = [
#         l1[i]+l2[i] for i in range(intervalo_maximo)
#     ]
#     return sum_list


print(sum_function(lista_a, lista_b))