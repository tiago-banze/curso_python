# # Exercício - Lista de tarefas com desfazer e refazer
# # todo = [] -> lista de tarefas
# # todo = ['fazer café'] -> Adicionar fazer café
# # todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# # desfazer = ['fazer café',] -> Refazer ['caminhar']
# # desfazer = [] -> Refazer ['caminhar', 'fazer café']
# # refazer = todo ['fazer café']
# # refazer = todo ['fazer café', 'caminhar']
# import os
# import json

# def print_nada_na_lista(string):
#     print(f'\nNao existe nada para {string} na lista!\n')

# def listar(lista):
#     for index,tarefa in enumerate(iter(lista)):
#         print(f'Tarefa {index+1} = {tarefa}')

# def ler_arquiv_json(caminho, lista):
#     try:
#         with open(caminho, 'r', encoding='utf8') as arquivo:
#             lista = json.load(arquivo)
        
#     except FileNotFoundError:
#         with open(caminho, 'w', encoding='utf8') as arquivo:
#             json.dump(lista,arquivo,indent=2,ensure_ascii=False)
#     if caminho == True:
#         with open(caminho, 'w', encoding='utf8') as arquivo:
#             json.dump(lista,arquivo,indent=2,ensure_ascii=False)
            
        
# caminho = 'lista_de_tarefas.json'
# lista_de_tarefa = []
# lista_de_tarefas = lista_de_tarefa

# lista_removido = []
# comandos = ['listar', 'desfazer', 'refazer', 'x','clear']

# while True:
#     print("Comandos: listar, desfazer, refazer")
#     entry = input('Digete uma tarefa ou comando: ').lower()
    
#     if entry == comandos[3]:
#         break
    
#     if entry == comandos[0]:
#         if not lista_de_tarefas:
#             print_nada_na_lista('listar')
            
            
#         elif len(lista_de_tarefas) > 0:
#             print('\n       LISTA DE TAREFAS')
#             listar(lista_de_tarefas)
                
                
#     elif entry == comandos[1]:
#         if not lista_de_tarefas:
#             print_nada_na_lista('desfazer')
            
#         elif len(lista_de_tarefas) > 0:
#             removido = lista_de_tarefas.pop()
#             lista_removido.append(removido)            
#             print('\n       LISTA DE DISFEITA')
#             listar(lista_de_tarefas)
            
#             if len(lista_de_tarefas) <= 0:
#                 print_nada_na_lista('desfazer')
                
                
#     elif entry == comandos[2]:
#         if not lista_removido:
#             print_nada_na_lista('refazer')
            
#         elif len(lista_removido) > 0:
#             # lista_removido.reverse()
#             remover = lista_removido.pop()
#             lista_de_tarefas.append(remover)
#             print('\n       LISTA DE REFAZIDA')
#             listar(lista_de_tarefas)
#             # listar(lista_removido)
            
#             if len(lista_removido) <= 0:
#                 print_nada_na_lista('refazer')
    
    
#     elif entry == comandos[4]:
#         os.system('cls')
    
    
#     elif entry is not comandos:
#         lista_de_tarefas.append(entry)

