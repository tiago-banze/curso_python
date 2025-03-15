# # meses_sistema = [
# #     'jan2022','fev2022','marc2022',
# #     'abr2022','mai2022','jun2022',
# #     'jul2022','ago2022','set2022',
# #     'out2022','nov2022','dez2022'
# #     ]

# # print(len(meses_sistema))

# def soma1(n):
#     soma = 0 
#     for i in range(n +1):
#         soma += i
#     return soma
# print(soma1(5))

# def soma2(n):
#     # if n == 0:
#     #     return 0
#     return n + soma2(n - 1)

# print(soma2(5))

# def recursiva (inicio = 0, fim = 4):
#     print(inicio,'] [',fim)
    
#     # caso base 
#     if inicio >= fim:
#         return fim
#     inicio += 1
#     return recursiva(inicio , fim)
    
# print(recursiva(fim= 1000))



# def funcao_simples (inicio = 0, fim = 4):
#     # caso base 
#     for i in range(fim + 1):
#         print(inicio,'] [',fim)
#         inicio += i
#         if inicio >= fim:
#             return fim
       
    # return recursiva(inicio , fim)
    
# print(funcao_simples(fim= 1000))

def factorial(n):
    
    if n == 0:
        return 1
    else:
        print(n)
        
    return n * factorial(n-1)

print(factorial(5))
print()

numero = 5
contador = 1
for i in range(1,numero+1):
    print(i)
    contador= contador *  i

print(contador)
# print(range.__doc__)
 
