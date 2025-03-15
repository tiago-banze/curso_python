"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
""" 
# nome = 'tiago'
# mudar = nome[1]
lista_nome = ['tiago', 'banze']
lista_b = lista_nome

print(lista_b)