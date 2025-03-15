# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

# crie uma função fala se um número é par ou ímpar.
# Retorne se o número é para ou ímpar

def multiplicar(*numeros):
    acumulador = 1
    for numero in numeros:
        acumulador *= numero
    return acumulador

def par_ou_impar(x):
    if x % 2==0:
        return f'{x} é PAR'
    return f'{x} é Ímpar'

total = multiplicar(2,2,2,2)
print(total)

par_impar = par_ou_impar(3)
print(par_impar)