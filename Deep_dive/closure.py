def minha_funcao(nome, idade=25):
    print(f'Nome: {nome}, Idade: {idade}')
    print(f'variaveis locais sao: {locals()}')
    
minha_funcao('tiago')
