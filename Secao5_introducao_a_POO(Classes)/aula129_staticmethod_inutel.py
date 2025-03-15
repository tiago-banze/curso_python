# @staticmethod (métodos estáticos) são inúteis em Python =)
# Métodos estáticos são métodos que estão dentro da
# classe, mas não tem acesso ao self nem ao cls.
# Em resumo, são funções que existem dentro da sua
# classe.

class Classe:
    @staticmethod
    def funca_que_esta_na_classe(*args, **kwargs):
        print('Olá', *args, **kwargs)
        
def funcao(*args, **kwargs):
    print('Olá', *args, **kwargs)

c1 = Classe()
print(c1.funca_que_esta_na_classe('tiago','victor', 'banze'))
print()
