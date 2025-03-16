# Escopo da classe e de metódos da classe

# class Animal:
#     def __init__(self, nome):
#         self.nome = nome
#         variavel = 'valor'
#         print(variavel)
        
#     def comer(self, comendo = 'nada'):
#         print(f'{self.nome} está comendo {comendo}!')
        
        
# leao = Animal(nome='Leão')
# print(leao.nome)
# leao.comer('Banana')

class Carro:
    rodas = 4 # variavel do escopo da classe
    print(id(rodas))
    def __init__(self, marca, rodas):
        self.marca = marca
        self.rodas = rodas
        print(id(self.rodas))
        print(f"{self.rodas}")
    def mostrar_rodas(self):
        return f'{self.marca} tem {self.rodas} rodas!'

        
carro1 = Carro('Toyota', 6)
print(carro1.mostrar_rodas())