# Exercícios
# Criar funções que duplicam e quadruplicam
# o Nímero recebido como parâmetro

# def criar_multiplicador (numero):
#     def duplicar():
#         return f'duplo de  {numero} é {numero*2}'
#     def triplicar():
#         return f'triplo de  {numero} é {numero*3}'
#     def quadruplicar():
#         return f' quadriplo de  {numero} é {numero*4}'
#     return duplicar(), triplicar(), quadruplicar()

# resultado = criar_multiplicador(2)
numero = 2

def criar_multiplicador (multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(f'duplo de  {numero} é {duplicar(numero)}')
print(f'triplo de  {2} é {triplicar(numero)}')
print(f'quadruplo de  {2} é {quadruplicar(numero)}')
print(quadruplicar.__closure__)