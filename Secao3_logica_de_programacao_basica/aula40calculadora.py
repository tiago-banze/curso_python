""" Calculadora com while"""
# s = 3.49
# t =3.50
# print(f"s = {round(s)}\n t = {round(t)}")
while True:
    numero1 = input('digite um número: ')
    numero2 = input('digite outro número: ')
    Operador = input('Digite operador (+-/*): ')
    
    numeros_validos = None
    numero1_convertido = 0
    numero2_convertido = 0
    
    try:
        numero1_convertido = float(numero1)
        numero2_convertido = float(numero2)
        numeros_validos = True
    except:
        numeros_validos = None
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue
    operadores_permitidos = "+-/*"
    if Operador not in operadores_permitidos:
        print(f'Operador "{Operador}", não é válido!')
        continue
    if len(Operador) > 1:
        print('Digite apenas um operador.')
        continue
    result = 0
    print('Realizando sua conta. Confira o resultado abaixo com aredondamento(excesso/defeito):')
    if Operador == '+':
        result = numero1_convertido + numero2_convertido
        print (f'{numero1_convertido} + {numero2_convertido} = {round(result,2)}')
    elif Operador == '-':
        result = numero1_convertido - numero2_convertido
        print (f'{numero1_convertido} - {numero2_convertido} = {round(result,2)}')
    elif Operador == '*':
        result = numero1_convertido * numero2_convertido
        print (f'{numero1_convertido} * {numero2_convertido} = {round(result,2)}')
    elif Operador == '/':
        if numero2_convertido ==0:
            result = 0
            print (f'Cannot divide {numero1_convertido} by {numero2_convertido}:')
        else:
            print (f'{numero1_convertido} / {numero2_convertido} = {round(result,2)}')
    sair = input('Quer sair? [S]im: ').lower().startswith("s")
    if sair is True:
        break
    print(sair)
print('fim')