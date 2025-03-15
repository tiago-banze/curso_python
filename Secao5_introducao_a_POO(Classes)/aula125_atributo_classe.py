class Pessoa:
    ano_actual = 2025
    
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa - self.idade
    
pessoa1 = Pessoa('Tiago', 26)
print(pessoa1.get_ano_nascimento())