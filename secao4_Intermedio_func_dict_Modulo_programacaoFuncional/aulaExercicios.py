"""
Iterando string
"""
nome = 'Tiago Victor' #Iteraveis
contador = 0
tamanho_nome = len(nome)
while contador < tamanho_nome:
    print(f'"{nome}" *{nome[contador]}*')
    contador +=1
print(f'Há {contador} caracter em [{nome}]') 
print('Fim do Jogo')