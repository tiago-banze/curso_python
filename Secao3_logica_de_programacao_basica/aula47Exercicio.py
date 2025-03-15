"""
faça um jogo para usuário adivinhar qual 
a palavra secreta.
- você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para 
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba*.
faça a contagem de tentativas do seu usuário.
"""
palavra_secreta = 'tiago'
tentativa = 0

while True:
    digite_uma_letra = input('Digite uma letra qualquer: ')
    tentativa +=1
    if digite_uma_letra in palavra_secreta:
        print(f"{digite_uma_letra} está na palavra secreta!")
        break
    else:
        print('*')
    print(f'tentava {tentativa}')
    
    
if tentativa == 0:
    print(f'O senhor conseguiu logo de primeira')
elif tentativa ==1:
   print(f' O senhor tentou {tentativa} vez')
elif tentativa > 1:
    print(f'O senhor tentou {tentativa} vezes')

    
    # tentativa +=1