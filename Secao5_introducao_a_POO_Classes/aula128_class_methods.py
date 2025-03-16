# Métodos de classe 
# São métodos onde "sel" será "cls", ou seja, 
# ao invés de receber a instância no primeiro 
# Parâmetro, receberemosa a propria classe.

# class Pessoa:
#     ano = 2023 # atributo da classe
#     def __init__(self, nome , idade):
#         self.nome = nome
#         self.idade = idade
    
#     @classmethod
#     def metodo_de_classe(cls):
#         print('Hey')

        
# p1 = Pessoa('tiago', 26)
# # p1.metodo_de_classe()
# # Pessoa.metodo_de_classe()

# class Carro:
#     contador_de_carros = 0
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo
#         Carro.contador_de_carros += 1
#     @classmethod    
#     def obter_contador_de_carros(cls):
#         return cls.contador_de_carros
# # Criando estância da classe    
# carro1 = Carro('Toyota', 'Ratice')
# carro2 = Carro('Mazda', 'verisa')
# carro3 = Carro('Mazda', 'Demio')
# carro3 = Carro('Mazda', 'D')
# # Chamando class Method
# print(Carro.obter_contador_de_carros())

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    @classmethod    
    def criar_novo_carro(cls, marca, modelo):
        return cls(marca, modelo, 2025)
    
novo_carro = Carro.criar_novo_carro('Toyota', 'corola')
print(novo_carro.__dict__)
