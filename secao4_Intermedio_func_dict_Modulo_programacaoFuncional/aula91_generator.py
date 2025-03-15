# Introdução às Generator funtions em python
# generator = (n for n in rangue(1000000))


def generator (n=0):
    yield 1 #pausar
    print('Continuando...')
    yield 2
    print('Continuando...')
    
gen = generator(n=0)
print(next(gen))
print(next(gen))