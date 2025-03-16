from aula127_exercicio_JSON import Pessoa, caminho,json

with open(caminho, 'r', encoding = 'utf8') as arquivo:
    dictionary = json.load(arquivo)
    
# print(dictionary)

pessoa1 = Pessoa(**dictionary[0])
pessoa2 = Pessoa(**dictionary[1])
pessoa3 = Pessoa(**dictionary[2])
print(pessoa2.get_ano_nascimento())
print(vars(pessoa2))