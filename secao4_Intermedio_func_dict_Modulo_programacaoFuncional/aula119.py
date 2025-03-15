# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar'] 

import json

def ler(tarefas, caminho_arquivo):
    dados = []
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print('Arquivo nao exeste!')
        salvar(tarefas,caminho_arquivo)
    return dados
    
def salvar(tarefas, caminho_arquivo):
    dados = tarefas
    with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
        dados = json.dump(tarefas, arquivo, ensure_ascii=False, indent=2)
    return dados

def listar_tarefas(lista):
    print()
    print('\tLISTA DE TAREFA')
    for index, tarefa in enumerate(iter(lista)):
        print(f'\t{index+1}  =  {tarefa}')
    print()
    
def desfazer(lista, lista1):
    tarefa = lista.pop()
    lista1.append(tarefa)
    listar_tarefas(lista)

def refazer(lista, lista1):
    tarefa = lista1.pop()
    lista.append(tarefa)
    listar_tarefas(lista)
    
def adicionar(entrada, lista):
    lista.append(entrada)
    listar_tarefas(lista)
    
def sem_tarefa(comando):
    print()
    print(f'Não existe nada para {comando}!')
    print()
CAMINHO_ARQUIVO = 'aula119.json'
lista_de_tarefas = ler([], CAMINHO_ARQUIVO)
removidos = []
while True:
    
    print('Comands: listar, desfazer, refazer')
    entry = input('Digete uma tarefa ou comando!')
    if entry == 'x':
        break
    elif entry == 'listar':
        if not lista_de_tarefas:
            sem_tarefa('listar')
            continue
        listar_tarefas(lista_de_tarefas)
        
    elif entry == 'desfazer':
        if len(lista_de_tarefas) <=0:
            sem_tarefa('desfazer')
            continue
        desfazer(lista_de_tarefas, removidos)
        
    elif entry == 'refazer':
        if not removidos:
            listar_tarefas(lista_de_tarefas)
            sem_tarefa('refazer')
            continue
        refazer(lista_de_tarefas, removidos)
    else:
        adicionar(entry, lista_de_tarefas)
    salvar(lista_de_tarefas, CAMINHO_ARQUIVO)