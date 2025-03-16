# @property @setter - getter e setter no modo pythonico
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo


class Caneta:
    def __init__(self, cor):
        self._cor = cor
    
    @property
    def cor(self):
        print('GETTER')
        return self._cor
    
    @cor.setter
    def cor(self, cor):
        print(f'\nVAlor SETTER: {cor}\n ')
        self._cor = cor

caneta = Caneta('Preto')
print(caneta.cor)
caneta.cor = 'VERMELHO'
print(caneta.cor)

# def my_func(value):
#     if value == 5:
#         return range(5)  # Retorna uma lista diretamente
#     else:
#         yield from range(value)  # Gera valores de 0 até value-1

# print(list(my_func(4)))