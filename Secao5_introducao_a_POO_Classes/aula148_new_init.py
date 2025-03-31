# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        instancia = super().__new__(cls)
        return instancia

    def __init__(self, x):
        self.x = x
        print('Inicializando a instância!')

    def __repr__(self):
        print()
        print("Representando a parte tecnica do objecto instanciado.")
        return 'A()'


a = A(123)
print(a.x)
print(repr(a))