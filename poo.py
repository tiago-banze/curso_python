class Animal:
    def __init__(self, nome: str, idade: int,raca: str):
        self.nome = nome
        self._idade = idade
        self.raca = raca
        
    @property
    def idade(self):
        print(self._idade)
        
    @idade.setter   
    def idade(self, valor):
        self._idade = valor
        
        
if __name__ == '__main__':
    a1 = Animal("aquilivio", 48, "pitbull")
    print(a1.idade)
    a1.idade = 89
    print(a1.idade)