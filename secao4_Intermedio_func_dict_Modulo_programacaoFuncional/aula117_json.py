import json


pessoa ={
    'nome' : 'Tiago Victor/',
    'Sobrenome': 'Banze',
    'endereco': [
        {'rua': 'R1', 'número': 32},
        {'rua': 'R2', 'numero': 55}
    ],
    'altura': 1.8,
    'numeros_preferidos': (2,4,6,8,10),
    'dev': True,
    'nada': None
}

with open('aula117.json', 'w', encoding= 'utf8') as arquivo:
    json.dump( 
        pessoa, 
        arquivo, 
        ensure_ascii=False,
        indent=2,
        )

with open('aula117.json', 'r', encoding='utf8') as arquivo:
    pessoas = json.load(arquivo)
    # print(json.dumps(pessoas))
    
    
for pessoa in pessoas.items():
    print(pessoa)
    