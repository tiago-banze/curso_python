# 1. Filtragem de Dados de uma Lista de Dicionários
# Dada uma lista de dicionários que contém informações sobre 
# produtos (nome, categoria e preço), crie uma nova lista que 
# contenha apenas os produtos da categoria "eletrônicos" com 
# preço inferior a 500.

import pprint

def Print(valor):
    pprint.pprint(valor, sort_dicts=False)

produtos = [
    {'nome': 'Smartphone', 'categoria': 'eletrônicos', 'preço': 700},
    {'nome': 'Fone de Ouvido', 'categoria': 'eletrônicos', 'preço': 150},
    {'nome': 'Camiseta', 'categoria': 'vestuário', 'preço': 50},
    {'nome': 'Laptop', 'categoria': 'eletrônicos', 'preço': 1200},
    {'nome': 'Teclado', 'categoria': 'eletrônicos', 'preço': 80},
]

new_list = [
    electronic 
    for electronic in produtos 
    if electronic['categoria'] =="eletrônicos" and electronic['preço']<500
             ]

Print(new_list)