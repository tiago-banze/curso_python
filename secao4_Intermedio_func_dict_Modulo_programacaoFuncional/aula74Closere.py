"""
Closure e funções que retornam outras funções
"""

def criar_saudacao(saudacao, nome):
    return f'{saudacao}, {nome}'

saudacao = criar_saudacao('olá','Tiago')
print(saudacao)...