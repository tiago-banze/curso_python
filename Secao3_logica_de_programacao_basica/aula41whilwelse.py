"""
While/else
"""
string = 'Valorqualquer'

i = 0

while i < len(string):
    letra =string[i]
    
    if letra == " ":
        break
    
    print (letra)
    
    i += 1
else:
    print('Não encontrei nenhum espaço na string')
    print('O else foi executado')