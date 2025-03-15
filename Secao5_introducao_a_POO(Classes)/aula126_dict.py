class Pessoa:
    ano_actual = 2025
    
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_actual - self.idade
    
pessoa1 = Pessoa('Tiago', 26)
pessoa1.nome = 'Banze'

# print(f'{pessoa1.nome} é de {pessoa1.get_ano_nascimento()}')
print(pessoa1.__dict__)
print(vars(pessoa1))