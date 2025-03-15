"""
Valores padrão para parâmetros
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
usado.
Refatorar: editar o seu código.
"""
def soma(x, y, z=None):
    if z is not None:
        print(f'{x=} {y=} {z=} | {x} + {y} + {z} = {x+y+z}')
    else:
        print(f'{x=} {y=} | {x} + {y} = {x+y}')

soma(1,7,0)
soma(19,2,1)
soma(8,9)
soma(y=2, z=0, x=9)