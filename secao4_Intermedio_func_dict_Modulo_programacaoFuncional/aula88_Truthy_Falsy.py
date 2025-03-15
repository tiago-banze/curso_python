# Valores Truthy e Falsy, Tipos Mutáveis e Imutáveis
# Mutáveis [] {} set()
# Imutáveis () "" 0 0.0 None False range(0, 10)
lista = [0]
dicionario = {}
conjunto = set()
tupla = ()
string = ' '
inteito = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def falsy_truthy(valor):
    return 'Falsy' if not valor else 'Truthy'

print(f'{lista=} é {falsy_truthy(lista)}')
print(f'{tupla=} é {falsy_truthy(tupla)}')
print(f'{dicionario=} é {falsy_truthy(dicionario)}')
print(f'{conjunto=} é {falsy_truthy(conjunto)}')
print(f'{inteito=} é {falsy_truthy(inteito)}')
print(f'{flutuante=} é {falsy_truthy(flutuante)}')
print(f'{nada=} é {falsy_truthy(nada)}')
print(f'{falso=} é {falsy_truthy(falso)}')
print(f'{string=} é {falsy_truthy(string)}')
print(f'{intervalo=} é {falsy_truthy(intervalo)}')