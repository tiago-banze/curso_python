# Exercíco - Adiando execução de funções
def soma (x, y):
    return x + y

def multiplicar(x,y):
    return x * y

def criar_funcao(funcao, x):
    def interna(y):
        return funcao(y, x)
    return interna

soma_como_cinco = criar_funcao(soma, 5)
multiplicar_por_dez = criar_funcao(multiplicar, 10)
print(soma_como_cinco(1))
print(multiplicar_por_dez(10))