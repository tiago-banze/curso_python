from abc import ABC, abstractmethod

#Classe abstracta
class Veiculo(ABC):
    @abstractmethod
    def mover(self):
        ...
    
    @abstractmethod
    def parar(self):
        ...

#Classe que herda a classe abstracta     
class Carro(Veiculo):
    def __init__(self, nome):
        self.nome = nome
    def mover(self):
        print(f"O carro de marca {self.nome} está andar!")
        
    def parar(self):
        print(f"O carro de marca {self.nome} está parando!")
        
#Outra classe que herda classe abstracta
class Aviao(Veiculo):
    def __init__(self, nome):
        self.nome = nome
        
    def mover(self):
        print(f'O avião da {self.nome} está voar!')
   
    def parar(self):
        print(f'O avião da {self.nome} está aterrando!')
        
        
toyota = Carro('TOYOTA RACTIS')
toyota.mover()
toyota.parar()
print()

alm_aviao = Aviao('LAM')
alm_aviao.mover()
alm_aviao.parar()

