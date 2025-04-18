# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma 
# classe "callable" .

class CallMe:
    def __init__(self, phone):
        self.phone = phone
        
    def __call__(self,nome):
        print(f'{nome} ligando para {self.phone}')
        
call1=CallMe(847388489)
call1('tiago')
call1('paito')