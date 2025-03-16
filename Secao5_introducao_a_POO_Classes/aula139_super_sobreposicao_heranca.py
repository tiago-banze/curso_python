# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem 
# Composição - É dono de, Herança - é um

# Herança ou Composição

# Classe principal (Pessoa)
#  -> super class, base class, parent class
# Classes filhas (Cliente)
#  ->sub class, child class, derived class

# class MinhaString(str):
#     def upper(self):
#         print('CHAMOU UPPER')
#         retorno = super().lower() # esse upper não é da classe minhastrin, mas sim da classe str que é a nossa superclasse
#         print ('DEPOIS DO UPPER')
#         return retorno
    
# string = MinhaString('Tiago')
# print(string.upper( ))

class A:
    def __init__(self, atributo):
        self.atributo = atributo
    atributo_a = 'Valor a'
    def metodo(self):
        print('A')
        
class B(A):
    atributo_b = 'Valor b'
    
    def metodo(self):
        print('B')
        
class C(B):
    atributo_c = 'Valor c'
    
    def metodo(self):
        # super(B, self).metodo()
        # super(C, self).metodo()
        # super().metodo()
        print('C')

c = C('Tiago')
c.metodo()
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)