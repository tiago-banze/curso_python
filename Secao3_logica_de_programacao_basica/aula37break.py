"""
Repetição 
While (enquanto)
execta um acão enquanto uma condição  for verdadeira
loop -> quando um codigo não tem fim
"""
contador = 0

while contador < 100:
    contador += 1
    
    if contador == 6:
        print('Não vou mostrar o 6.')
        continue
    if contador >= 10 and contador <= 28:
        # print(f'Não vou mostrar o {contador}.')
        continue
    print(contador)
    
    if contador == 40:
        break
print('Fim de Jogo')