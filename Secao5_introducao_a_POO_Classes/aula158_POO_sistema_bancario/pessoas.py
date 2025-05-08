import contas
class Pessoa():
    def __init__(self, nome: str, idade: int) -> None:
        self._nome = nome
        self._idade = idade
        
    @property
    def nome(self):
        print(self._nome)
        
    @nome.setter
    def nome(self, novo_nome:str):
        if isinstance(novo_nome,str) and novo_nome.strip():
            self._nome = novo_nome
        else:
            print('Nome não valído!')
            
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self._nome!r}, {self._idade!r})'
        return f'{class_name}{attrs}'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome,idade)
        self.conta: contas.Conta |None = None
        
        
if __name__ == '__main__':
    c1 = Cliente('tiago',25)
    c1.conta = contas.ContaCorrente(111,222,0,0)
    
    c1.conta.depositar(200)
    c1.conta.detalhes()
    print(c1)
    print(c1.conta)
        
