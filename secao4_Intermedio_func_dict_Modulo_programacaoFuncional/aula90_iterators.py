# Generator expression, Iterables e Iterators em Python
import sys
# import time

# lista = [i for i in range(100000)]
# print(type(lista))
# print(sys.getsizeof(lista))

# lista = (i for i in range(100000))
# print(type(lista))
# print(next(lista))
# print(next(lista ))
# print(sys.getsizeof(1))

# yield

lista = [n for n in range(1000000)]
generator = (n for n in range(1000000))
print(sys.getsizeof(lista))

print(sys.getsizeof(generator))

print(generator)
