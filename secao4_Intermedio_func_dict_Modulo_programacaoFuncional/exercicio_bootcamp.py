"""
Saudações 
O exercício de hoje para ser apresentado na aula: faça um programa que recebe do usuário o
número de processo do estudante,  
o seu nome, as notas de teste 1,  teste 2 e a nota de trabalho.

"""
PERCENTO_TES = 0.3
PERCENTO_TRABAL = 0.4
print('Digite os seguintes dados do estudante \n\n')
nome_estudante = input('Nome: ')
processo = input('Processo:')
teste1 = input('Teste 1:')
teste2 = input('Teste 2:')
trabalho = input('Trabalho: ')
RESULTADO = ...
media=(float(teste1)*PERCENTO_TES)+(float(teste2)*PERCENTO_TES)+(float(trabalho)*PERCENTO_TRABAL)
def informacao():
    print('___________________________')
    print(f'Processo            :{processo}')
    print(f'Nome                :{nome_estudante}')
    print(f'Teste 1             : {float(teste1)}')
    print(f'Teste 2             : {float(teste2)}')
    print(f'Trabalho            : {float(trabalho)}')
    print(f'Média do estudante  : {int(media)} {RESULTADO}')

if media >=14:
    RESULTADO ="DISPENSA"
    informacao()
elif (media >=10) & (media<14):
    RESULTADO = 'APROVADO'
    informacao()
else:
    RESULTADO = "REPROVADO"
    print('alguma coisa foi digitado errado')