# Getters and Setters

class Test:
    def __init__(self,valor):
        self.valorvalor = valor # configuração de uma variável valor que recebe o valor que o usuario vai colocar como argumento da da configuração da classe
    
    @property    
    def get_valor(self):
        return self.valorvalor
    
    @get_valor.setter
    def set_valor(self, valor):
        self.valorvalor= valor
        
teste1 = Test(123)
print(f'Valor do Objecto: {teste1.get_valor}')
teste1.set_valor=903483

print(f'Valor do Objecto apos ter sofrido uma alteracao: {teste1.get_valor}')
# print(teste1.valor)

