# Crie um programa que Peça ao usuário um número e exiba o dobro, o triplo 
# e a raiz quadrada desse número.

numero =  int(input('Insira um numero: '))

dobro = numero*2
triplo = numero*3
raiz = numero**(1/2)

print(f'O  dobro de {numero} é {dobro}')
print(f'O  triplo de {numero} é {triplo}')
print(f'A raiz quadrada de {numero} é {raiz}')