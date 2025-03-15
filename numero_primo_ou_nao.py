numero = input('Digite um nr: ')
numero_convertido = int(numero)
contador = 0
for i in range(1, numero_convertido+1):
    if numero_convertido % i == 0:
        contador += 1


if contador == 2:
    print(f'O numero {numero_convertido} é primo')
else:
    print(f'O numero {numero_convertido} nao é primo')
    
    