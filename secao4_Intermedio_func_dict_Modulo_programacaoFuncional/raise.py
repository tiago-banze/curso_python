def verificar_positividade(numero):
    if numero <0:
        raise ValueError('O número deve ser positivo / Maior ou igual a 0  ')

    return numero

# print(verificar_positividade(-1))

try:
    print(verificar_positividade(-1))
except ValueError as v:
    print(f'Ocorreu um erro: {v} ')