#classes decoradoras (decorator classes)
# Classes decoradoras (Decorator classes)
class Multiplicar:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador

    def __call__(self, func):
        def interna(*args, **kwargs):
            resultado = func(*args, **kwargs)
            return resultado * self._multiplicador
        return interna


@Multiplicar(2)
def soma(x, y):
    return x + y


operacao = soma(5, 5)
print(operacao)