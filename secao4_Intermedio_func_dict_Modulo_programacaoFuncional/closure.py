def funcao_externa(mensagem='bom dia'):
    texto = mensagem
    
    def funcao_interna():
        print(texto)
    return funcao_interna()

funcao_externa()