'''
Interpolação de strings onde:
s- string
d e i - int
d - float
x e X - Hexadecimal (ABCDEF0123456789)
'''

NOME = 'Tiago'
PRECO = 1000.90
Interpolacao_de_string = '%s, o preço é %.2fmt ' % (NOME, PRECO)
print(Interpolacao_de_string)
print('O hexadecimal de %d é %04x' %(1 , 1))