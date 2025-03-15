# isinstace - para saber se objeto é de determinado tipo
lista = [
    'a', 1, 1.1, True, False, [0, 1, 2], (1, 2),
    {0, 1}, {'nome': 'Luiz'},
]
print(lista)
print(isinstance(True, int))

for item in lista:
    if isinstance(item, str):
        print(f'{item} é uma [string]')
        
    elif isinstance(item, list):
        print(f'{item} é uma [Lista]')
        
    elif isinstance(item, tuple):
        print(f'{item} é uma [Tupla]')
        
    elif isinstance(item, float):
        print(f'{item} é um [Float]')  
        
    elif isinstance(item, dict):
        print(f'{item} é um [Dicionario]') 
        
    elif isinstance(item, bool):
        print(f'{item} é uma [bool]... {type(item)}')
        print(f'{item} * {2} = {item * 2}')
        
    elif isinstance(item, bool):
        print(f'{item} é uma [Inteiro]... ')
        
    elif isinstance(item, set):
        print(f'{item} é uma [Set/Conjunto]')
        
    else:
        print(f'**{item} não sei que tipo de dado é!**') 
        
