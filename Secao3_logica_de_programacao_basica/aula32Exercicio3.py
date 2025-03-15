"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
primeiro_nome = input('Insira teu primeiro nome: ')
# if len(primeiro_nome) == 4:
#     print('Seu nome é curto')
# elif (len(primeiro_nome) == 5) or (len(primeiro_nome) == 6) :
#     print('Seu nome é normal')
# elif len(primeiro_nome) > 6:
#     print('Seu nome é muito grande')
tamanho_nome = len(primeiro_nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif (tamanho_nome >= 5) and (tamanho_nome <= 6) :
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Digite pelo menos uma letra!')