"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
numero = input("Imprima um nr inteiro: ")
# numero_convertido =int(numero)
# if numero_convertido % 2 == 0:
#     print(f'nr {numero_convertido} é Par')
# else:
#     print(f'nr {numero_convertido} é Ímpar')
try:
    numero.isdigit()
    numero_convertido =int(numero)
    if numero_convertido % 2 == 0:
        print(f'nr {numero_convertido} é PAR')
    else:
        print(f'nr {numero_convertido} é ÍMPAR')
except:
    print(f'\'{numero}\' não é um nr inteiro')