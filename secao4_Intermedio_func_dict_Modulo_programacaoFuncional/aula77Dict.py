# manipulando chaves e valores em dicionários
# pessoa = {
#     'nome': 'Tiago victor',
#     'sobrenome': 'Banze',
#     'idade': 25,
#     'altura': 1.6,
#     'enderecos': [
#         {'rua': 'tal tal', 'numero': 123},
#         {'rua': 'outa rua', 'numero': 233}
#     ]
# }
pessoa ={}
pessoa['nome']='Tiago Victor'
pessoa['sobrenome']='Banze'
pessoa['idade'] = 25
pessoa['altura'] = 1.70

pessoa.pop('nome')
for chave in pessoa:
    print(pessoa[chave])
    input()

# print(pessoa.keys())
# print(pessoa)