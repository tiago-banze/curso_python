nome = 'Tiago Victor Banze'
altura =1.80
peso = 95
imc = peso / (altura ** 2)
elipsis = ...
print(elipsis)
# formatação de Srings onde o f -> Formatação
linha_1 = f"{nome} tem {altura:,.2f} de altura"
linha_2 = f'pesa {peso}k e o seu IMC é {imc:.2f}'
print(linha_1)
print(linha_2)

# print(nome, 'tem', altura, 'de altura,','pesa', peso, 'quilos e o seu IMC é',imc )