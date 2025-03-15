# exercicio - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]
contador = 0

print("sistema de perguntas e respostas\nEscolha a opção correcta de 0 á 3")
for pergunta in perguntas:
   print(pergunta['Pergunta'])
   print()
   
   for indice, alternativa  in enumerate(pergunta['Opções']):
       print(f'{indice}) {alternativa}')
   resposta = input('qual é a opção correta: ')
   
   resposta_convertida = None
   if resposta.isdigit():
       resposta_convertida = int(resposta)
       try:
            if pergunta['Opções'][resposta_convertida] == pergunta['Resposta']:
                print('acertou ✔️\n')
                contador +=1
            else:
                print('Errou ❌\n')
       except IndexError:
            print('Errou ❌\nnão existe essa opção')
               
   else:
       print('Errou ❌\nnão existe essa opção')

if contador == len(perguntas):      
    print(f'\n🫡  Acertou {contador} de {len(perguntas)}\nMAU')
elif contador >= 1 < len(perguntas):
    print(f'\n😜 Acertou {contador} de {len(perguntas)}\n')
else:
    print(f'\n😒 Acertou {contador} de {len(perguntas)}')