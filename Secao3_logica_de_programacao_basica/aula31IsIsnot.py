"""
Flag (Bandeira) - Marcar um local
None = não valor
is is no = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = True
#Marcamos uma bandeira para posteriormente saber se passou do if ou nao
# para tal marcamos a bandeira como 'None' ou '...' ou sem nada 'reservamos para receber alguma coisa ao andar do codigo'
passou_no_if = None
# passou_no_if = ...
if condicao:
    passou_no_if = True
    print('Faça Algo')
else:
    print('Não faça algo')

if passou_no_if is not None:
    print('Passou no If')
if passou_no_if is None:
    print('Não passou no If')