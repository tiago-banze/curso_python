# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass, asdict, astuple

@dataclass
class Pessoa:
    nome: str
    sobrenome: str
    # def __init__(self, nome, sobrenome):
    #     self.nome = nome
    #     self.sobrenome = sobrenome
    #     self.nome_completo = f'{self.nome} {self.sobrenome}'
    
    # def __post_init__(self):
    #     self. nome_completo = f'{self.nome} {self.sobrenome}'
    # idade: int
    # @property
    # def nome_completo(self) -> str:
    #     return f'{self.nome} {self.sobrenome}'
    # @nome_completo.setter
    # def nome_completo(self, valor: str):
    #     nome , *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)
        
    
if __name__ == '__main__':
    p1 = Pessoa('Tiago', 'Banze')
    print(asdict(p1))
    print(asdict(p1).keys())
    print(astuple(p1))
    # print(p1.nome_completo)
    # print(p1.nome_completo)
    # p1.nome_completo = 'Victor Rungo Guifutela'
    # print(p1.nome_completo)
    # p2 = Pessoa('Luiz', 30)
    # print(dir(p1))
    # print(p1 == p2)