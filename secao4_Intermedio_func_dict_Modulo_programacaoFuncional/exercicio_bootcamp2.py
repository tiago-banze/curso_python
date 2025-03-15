'''
Criar um programa que peça ao usuário um número e diga se ele é para ou ímpar.
'''
print("Programa que mostra se um nr é par ou ímpar\n")
valor = input("Digite um nr: ")

numero = float(valor)
if numero%2==0:
    print (f'{numero} é par')
else:
    print (f'{numero} é Impar')