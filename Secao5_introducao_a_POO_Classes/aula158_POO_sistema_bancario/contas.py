from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self,agencia: int, numero: int,saldo: float=0) -> None:
        self.agencia = agencia
        self.conta = numero
        self.saldo = saldo
        
    @abstractmethod
    def sacar(self, valor: float) -> float:
        ...
    def depositar (self, valor: float) -> float:
        self.saldo += valor
        self.detalhes(f'✔️ DEPÔSITO: {valor}mt')
        return self.saldo
        
    def detalhes(self,msg: str ='') -> None:
        print(
            f"{msg} \n🔃 O seu saldo é {self.saldo:.2f}mt"
            )  
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r},{self.saldo})'
        return f'{class_name}{attrs}'
        
class ContaPoupanca(Conta):
    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'✔️ SAQUE: {valor}mt')
            return self.saldo
        
        print('❌Saque negado: saldo insuficiente')
        self.detalhes(f'❌ SAQUE NEGADO: {valor}mt')
        return self.saldo
        

class ContaCorrente(Conta):
    def __init__(self,agencia: int, numero: int, saldo: float=0, limite: float=0):
        super().__init__(agencia,numero,saldo)
        self.limite = limite
        
    def sacar(self, valor) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'✔️ SAQUE: {valor}mt')
            return self.saldo
        
        print('❌❌ Saque negado: saldo insuficiente')
        print(f'Seu limite é {-self.limite:.2f}')
        self.detalhes(f'❌ SAQUE NEGADO: {valor}mt')
        return self.saldo
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r},{self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'
    
if  __name__ == '__main__':
    contapoupanca1 = ContaPoupanca(111, 222, 19)
    print('#'*15,contapoupanca1.__class__.__name__,'#'*15)
    contapoupanca1.sacar(12)
    contapoupanca1.depositar(20)
    contapoupanca1.sacar(1)
    contapoupanca1.sacar(27)
    print()
    contacorrente1 = ContaCorrente(111, 222, 0,100)
    print('#'*15,contacorrente1.__class__.__name__,'#'*15)
    contacorrente1.sacar(12)
    contacorrente1.depositar(20)
    contacorrente1.sacar(1)
    contacorrente1.sacar(27)

    