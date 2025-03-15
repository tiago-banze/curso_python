""""
Faca uma lista de compras com listas.
O usuario deve ter a possibilidade de 
enserir, apagar e listar valores da sua lista.
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
import os

inserir,apagar,listar='i','a','l'
resposta = ''
opcao_inserida = ''
lista_de_compras = []
produto = ''
_ = "_"*30


while True:
    opcao_inserida = input("Selecione uma opção\n[i]nserir [a]pagar [l]istar:   \n").lower()
    
    if opcao_inserida == inserir:
        os.system('clear')
        produto = input('Insira o produto na carinha: ')
        lista_de_compras.append(produto)
        print(f'Lista de produtos atualizado\n{_}')
        for item in enumerate(lista_de_compras, start=1):
            indice, valor = item
            print(f'{indice}    {valor}')
            
            
    elif opcao_inserida == apagar:
        if len(lista_de_compras) != 0:
            indice_str = input("Insira o indice: ")
            try:
                indice = int(indice_str)
                del lista_de_compras[indice]
            except:
                print("Não foi poss'ivel apagar nada na lista")
                
    elif opcao_inserida == listar:
        os.system("clear")
        
        if len(lista_de_compras) ==0:
            print("Lista Vazia!")
            
        elif len(lista_de_compras)>1:
            print(f'Lista de produtos atualizado\n{_}')
            for item in enumerate(lista_de_compras, start=1):
                indice, valor = item
                print(f'{indice}    {valor}')
    else:
        print("Opcao invalida")
        continue
        
    resposta=input("deseja continuar? [S] para continuar").upper()
    if resposta == "S":
        pass
    else:
        break
print("Fim das compras") 