"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são: ')
minuto = input('quantos minutos se passam: ')

try:
    hora_convertida = int(hora)
    minuto_convertido = int(minuto)
    if (hora_convertida >= 0) and (hora_convertida <= 11):
        print(f'    Bom dia! \n Agora são {hora_convertida}:{minuto_convertido}min')
    elif (hora_convertida>= 12) and (hora_convertida <= 17):
        print(f'    Boa tarde! \n   Agora são {hora_convertida}:{minuto_convertido}min')
    elif (hora_convertida >= 18) and (hora_convertida <= 23):
        print(f'    Boa Noite! \n   Agora são {hora_convertida}:{minuto_convertido}min')
    else:
        print('Não existe isso!')
except:
    print('Entre a hora e minuto alguma coisa não corresponde a realidade')