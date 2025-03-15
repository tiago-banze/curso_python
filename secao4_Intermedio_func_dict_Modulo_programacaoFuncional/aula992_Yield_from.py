# Yield from
def gen1():
    yield 1
    yield 2
    yield 3
    
def gen2(gen):
    yield from gen()
    yield 4
    yield 5
    
g = gen2(gen1)
for i in g:
    print()