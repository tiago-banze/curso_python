"""
Repetição 
While (enquanto)
execta um acão enquanto uma condição  for verdadeira
loop -> quando um codigo não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual é o seu nome:')
    print(f'seu nome é {nome}')
    if nome == 'sair':
        break
   
print('Fim de Jogo')