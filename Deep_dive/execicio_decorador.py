# Criação de um Closure Simples
# 1. Escreva uma função multiplicador que recebe um 
# número e retorna uma função que, quando chamada, 
# multiplica esse número pelo valor passado inicialmente.

# def multiplicador(numero):
#     def operacao(x):
#         return numero * x
#     return operacao


# print('Multiplicação')
# print(multiplicador(2)(5))
# print(multiplicador(2)(10))



# 2.Somador com Closure
# Crie uma função somador que recebe um número e 
# retorna uma função que adiciona esse número a 
# um argumento passado para ela.

# def somador(numero):
#     def adiciona(x):
#         return numero + x
#     return adiciona


# print('\nSOMA')
# print(somador(3)(8))
# print(somador(3)(10))



# 3.Encapsulando Estado com Closure
# Escreva uma função contador que inicializa um 
# contador em zero e retorna uma função que 
# incrementa esse contador toda vez que é chamada.

# def contador(Inicializador = 0):
#     cont = Inicializador
#     def inc():
#         nonlocal cont
#         cont += 1
#         return cont
    
#     return inc

# count = contador(5)
# print(count())
# print(count())
# print(count())


# 4.Closure com Parâmetro de Valor Padrão
# Crie um closure que tem um valor padrão, e 
# quando chamado, ele somará esse valor ao 
# argumento passado.

def somadar_com_valor_padrao(numero):
    def somar(default = 0):
        return numero + default
    return somar

print(somadar_com_valor_padrao(5)(20))
print(somadar_com_valor_padrao(5)())


