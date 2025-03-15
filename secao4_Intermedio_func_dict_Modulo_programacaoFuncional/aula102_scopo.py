# variaveis livres + nonlocal (locals, globals)
# print(globals())
# def fora(x):
#     # a = x
#     # print(locals())
#     def dentro():
#         # print(locals())
#         return a
#     return dentro

# dentro1 = fora(10)
# dentro2 = fora(40)
# print(dentro1())
# print(dentro2())

# def funcao_externa():
#     saudacao = 'Olá'
#     def funcao_interna(nome:str):# closure
#         nonlocal saudacao
#         saudacao += f', {nome}!'
#         print(saudacao)
#     return funcao_interna
# #criando um closures
# closure = funcao_externa()
# closure('tiago Banze')
# closure_1 = funcao_externa()
# closure_1('João')

# def funcao_externa():
#     x = 5
#     print(f'Funcao Externa Inicio: {x}')  # A variável x foi modificada pela função interna
    

#     def funcao_interna():
#         nonlocal x  # Referencia a variável x do escopo da função externa
#         x = 10
#         print(f'Funcao interna: {x}')

#     funcao_interna()
#     print(f'Funcao Externa fim: {x}')  # A variável x foi modificada pela função interna
#     for i in locals().items():
#         print(f'Variável Local: {i}')
#     print()
#     for i in globals().items():
#         print(f'Variável global: {i}')


# funcao_externa()

# def concatenar(string_inicial):
#     valor_final = string_inicial
    
#     def interna(valor_a_concatenar)->str:
#         nonlocal valor_final
#         valor_final += valor_a_concatenar
#         return valor_final
#     return interna

# c = concatenar('a')
# print(c.__qualname__)
# print(c.__code__.co_freevars)
# print(c('b'))
# print(c('c'))
# print(c('d'))

a = [12,2,3,4,5]
b = a
b[1]=90 
print(b)
print(a)
    