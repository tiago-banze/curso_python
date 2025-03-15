# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem 
# Composição - É dono de, Herança - é um

# Herança ou Composição

# Classe principal (Pessoa)
#  -> super class, base class, parent class
# Classes filhas (Cliente)
#  ->sub class, child class, derived class

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def falar(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)  
        
          
class Cliente(Pessoa):
    ...
    
class Aluno(Pessoa):
    ...
    
c1 = Cliente('Tiago', 'banze')
c1.falar()

a1 = Aluno('Victor', 'Rungo')
a1.falar()
