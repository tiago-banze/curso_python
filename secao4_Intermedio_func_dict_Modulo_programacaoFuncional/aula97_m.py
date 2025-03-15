print('este modulo chama-se ', __name__)
lista = [1,2,3,4,5,6,7,8,9]
def gerador(lista):
    for i in lista:
        yield i
    