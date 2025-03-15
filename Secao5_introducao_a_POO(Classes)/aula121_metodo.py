# métodos em instancias de classes Python

class Carro:
    def __init__(self, nome = None):
        self.nome = nome
        
    def acelerar(self):
        print(f'{self.nome} está acelerando')
        
toyota = Carro('Toyota mazda')
print(toyota.nome)
toyota.acelerar()

Isuzo = Carro('Isuzo')
print(toyota.nome)
toyota.acelerar()