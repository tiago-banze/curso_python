"""
Iterável -> str, range, etc
Iterador -> que sabe entregar um valor por vez
next -> me entregue o proxímo valor
iter -> me entregue seu iterador
"""

# texto = iter('Tiago')#__iter__()

# print(texto.__next__()) # print (next(texto))
# print(texto.__next__())# print (next(texto))
# print(texto.__next__())# print (next(texto))
# print(texto.__next__())# print (next(texto))
# print(texto.__next__())# print (next(texto))
# print(texto.__next__())# print (next(texto)) aqui vai dar erro de StopIteration

# for letra in texto:
texto = "tiago banze" #objecto iteravel
# iterador = iter(texto) # Iterator
# while True:
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)