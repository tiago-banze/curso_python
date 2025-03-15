"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x,y):
    print(f'{x=} {y=} | {x} + {y} = {x+y}')
    
soma(4,3) # Argumento posicional ou não Nominal
soma(y=3,x=4) # Argumento Nominal