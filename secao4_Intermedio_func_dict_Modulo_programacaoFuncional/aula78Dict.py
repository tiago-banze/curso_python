# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - Apaga um item com a chave especificada (del)
# popitem - Apaga o último item adicionado
# update - Atualiza um dicionário com outro
import copy

chave = 'bairro'

pessoa = {
    'nome': 'Tiago victor',
    'sobrenome': 'Banze',
    'idade': 25,
    'altura': 1.6,
}
pessoa2 = copy.deepcopy(pessoa)# copia profunda


# print(pessoa.__len__())
# print(pessoa.keys())
# print(pessoa.values())
# print(pessoa.items())
pessoa.setdefault(chave, "george dimitrov")
pessoa.setdefault('bairro','2 de setembro')
print(pessoa2.get('bairro', f'nao existe chave: {chave} neste dicionario'))
print(pessoa2)
pessoa2.update(bairro= 'Benfica', rua=19)
print(pessoa2)

for chave , valor in pessoa2.items():
    print(chave , valor, sep='=')
























