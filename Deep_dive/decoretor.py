def decoretor(func):
    def interna(*args, **kwargs):
        print('Antes de decorar a funcao!')
        resultado = func(*args, **kwargs)
        print(resultado)
        print('Depois de decorar a funcao!')
        # return resultado
    return interna

@decoretor
def soma(a,b):
    return a + b

soma(2,5)
print(soma)