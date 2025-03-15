frase = 'O python é uma linguagem de progração'\
    ' multiparadigma.' \
        ' python foi criado por guido vannnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn Rossum. 861015546  '.lower()
# print(frase.count(''))
indice = 0
texto = ''
apareceu_mais_vezes=''
letra_anterior = 0

while len(frase) > indice:
    letra_actual = frase[indice]

    if letra_actual == ' ' or letra_actual in texto or letra_actual == ".":
        pass
    else:
        if letra_anterior < frase.count(letra_actual):
            letra_anterior = frase.count(letra_actual)
            apareceu_mais_vezes = letra_actual
        print (f'{letra_actual} foi repetido {frase.count(letra_actual)} vezes')
    indice += 1
    texto +=letra_actual
# print(texto[::1])
print(f'\nA letra que apareceu mais vezes foi "{apareceu_mais_vezes}" com um marco de {letra_anterior}')