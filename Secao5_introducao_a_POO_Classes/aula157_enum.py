#Enum -> Enumerações
# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas para escolher.
# Enums têm membros e seus valores são constantes.
# Enums em python:
#   - são um conjunto de nomes simbólicos (membros) ligados a valores únicos
#   - podem ser iterados para retornar seus membros canônicos na ordem de
#       definição
# enum.Enum é a superclasse para suas enumerações. Mas também pode ser usada
#   diretamente (mesmo assim, Enums não são classes normais em Python).
# Você poderá usar seu Enum com type annotations, com isinstance e
# outras coisas relacionadas com tipo.
# Para obter os dados:
# membro = Classe(valor), Classe['chave']
# chave = Classe.chave.name
# valor = Classe.chave.value
from enum import Enum,auto

# import enum

# Direcoes = enum.Enum("Direcoes", ['ESQUERDA', 'DIREITA'])
class Direcoes(Enum):
    ESQUERDA =auto()
    DIREITA =auto()
    
print(Direcoes(2), Direcoes['DIREITA'], Direcoes.ESQUERDA.value)
def mover(direcao):
    if not isinstance(direcao,Direcoes):
        raise ValueError('Direção não existe!')
    
    print(f"Movendo para {direcao}")
    
mover(Direcoes.ESQUERDA)
mover(Direcoes.DIREITA)
# mover('direita')

# class Cor(Enum):
#     RED = 1
#     BLUE = 2
#     GREEN = 3

# print(Cor.BLUE)
# print(Cor.BLUE.value)
# print(Cor.BLUE.name)
# print(len(Cor))
# print(list(Cor))
# print(Cor(1))
# print(Cor['GREEN'])