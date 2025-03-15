'''
Introducão ao try/except
try-> tentar executar o código 
except -> Ocorreu algum erro ao tentar executar
'''
numero_str = input('Vou dobrar o nr que vc digitar: ')

try:
    numero_convertido = float(numero_str)
    print(f'O dobro de {numero_convertido} é {numero_convertido * 2}')
except:
    print('Isso não é um número')
     
# numero_str = input('Vou dobrar o nr que vc digitar: ')
# if numero_str.isdigit():
#     numero_convertido = float(numero_str)
#     print(f'O dobro de {numero_convertido} é {numero_convertido * 2}')
# else :
#     print('Isso não é um número')