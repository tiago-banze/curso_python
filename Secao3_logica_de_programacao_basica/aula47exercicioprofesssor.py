
import os

tentativas = 0
palavra_secreta = 'tiago'
letras_acertada = ''

while True:
    letra_digitada = input('digite uma letra: ')
    tentativas += 1
    
    if len(letra_digitada) < 1 or len(letra_digitada) > 1:
        print('por favor digite uma letra')
        continue
    
    if letra_digitada in palavra_secreta:
        letras_acertada += letra_digitada
    
    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertada:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
    print(f'A palavra formada : {palavra_formada}')
    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('parabens, você ganhou')
        print(f'a palavra secreta é {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        tentativas = 0
        letras_acertada = ''