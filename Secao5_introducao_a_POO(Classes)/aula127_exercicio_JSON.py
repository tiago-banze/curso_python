# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.class Pessoa:
import json
class Pessoa:
    ano_actual = 2025
    
    def __init__(self, nome, idade):
        self.nome= nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_actual - self.idade
    
pessoa1 = Pessoa('Tiago', 26)
pessoa2 = Pessoa('nelia', 26)
pessoa3 = Pessoa('leu', 40)
lista= [pessoa1.__dict__, vars(pessoa2),pessoa3.__dict__]

# dados = lista.__dict__
file = 'aula127.json'
caminho = "D:\\Curso Python\\Secao5_introducao_a_POO(Classes)\\" +file
print()
# print(vars(Pessoa))
def fazer_dump():
    with open(caminho, 'w', encoding = 'utf8')as arquivo:
        print('Fazendo o dump')
        json.dump(lista, arquivo, indent= 2, ensure_ascii=False)

if __name__ == '__main__':
    fazer_dump()