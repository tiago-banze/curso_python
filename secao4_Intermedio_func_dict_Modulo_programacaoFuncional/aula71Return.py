"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
x, y, *resto = 1, 2, 3, 4
# print(x, y, resto)


def soma(*argumentos):
    acumulador = 0
    for numero in argumentos:
        # print(f'{acumulador} + {numero}')
        acumulador += numero
    return acumulador

        
    # return x + y
numeros = (1,3,4,8,1,6,7,8,6)
soma_argumento = soma(*numeros)
print(soma_argumento)
print(sum(numeros))