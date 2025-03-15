lista = ['tiago', 1,2,7,9,7,6,7,6,8,9,0,8,7,'tiago']
lista_testador_de_repeticao = set()
contador = 0
for valor in lista:
    if valor in lista_testador_de_repeticao:
        contador += 1
        print(f' {valor=} repetido')
        break``
        print()
    lista_testador_de_repeticao.add(valor)