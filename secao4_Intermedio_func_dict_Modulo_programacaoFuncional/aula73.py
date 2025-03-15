"""
Higher Order Functions
funcões da primeira classe
"""
def saudacao(nome, apelido):
    return f'Olá, {nome} {apelido}!'

def return_saudacao(funcao , *args):
    return funcao(*args)

print(return_saudacao(saudacao,"Tiago", "Banze"))

