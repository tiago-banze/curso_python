# 5)	Escreva um programa que peça a idade do usuário e diga 
# se ele é maior ou menor de idade.

idade = int(input('insira sua idade por favor: '))

if idade >= 18:
    print('Parabéns O/a senhor/a é Maior de idade!')
elif idade < 18 and idade >= 0:
    print('Desculpa O/a senhor/a é Manor de idade!')
else:
    print('Desculpa essa idade nao existe!')
    