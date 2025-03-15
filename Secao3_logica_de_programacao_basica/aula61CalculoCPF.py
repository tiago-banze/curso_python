
import re
import random
import sys

# cpf = '14687629075'.replace('.','')
entrada = input('CPF [146.876.290-75]')
cpf = re.sub(
    r'[^0-9]',
    '',
    entrada)

#
novo_digito = cpf[:9]
# sys.exit()
contador_regressivo1 = 10
primeiro_digito = 0
resultado = 0
for digito in novo_digito:
    resultado += int(digito)*contador_regressivo1
    contador_regressivo1 -= 1
resultado *= 10
if resultado % 11 > 9:
    primeiro_digito
else:
    primeiro_digito = resultado % 11



novo_digito2 = novo_digito + str(primeiro_digito)
contador_regressivo2 = 11
resultado2= 0
segundo_digito = 0
for digito in novo_digito2:
    resultado2 += int(digito)*contador_regressivo2
    contador_regressivo2 -= 1
resultado2 *= 10
if resultado2 % 11> 9:
    segundo_digito
else:
    segundo_digito = resultado2 % 11
    
cpf_gerado_pelo_calculo = f'{novo_digito}{primeiro_digito}{segundo_digito}'
if cpf == cpf_gerado_pelo_calculo:
    print (f'{cpf} é valido')
else:
    print(f'CPF é invalído')