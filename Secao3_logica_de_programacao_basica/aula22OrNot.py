# entrada = input('[E]ntrar [S]air')
# senh_digitada=input('Senha:')
# senha_permitida= '123456'
# if (entrada =='E' or entrada=='e') and senh_digitada==senha_permitida:
#     print('entrada')
# else:
#     print('Sair')
#avaliacao de curto circuito
senha = input('Senha:') or 'Sem senha'
# print(0 or False or 0 or 'abc')
print(senha)