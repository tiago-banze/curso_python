# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover / Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o python
# Usar as funções decoradoras em outras funções

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou te decorar')
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('Ok, agora você foi decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
# invertida
# print(invertida)
    

# def meu_decorador(func):
#     def wrapper():
#         print('Algo ANTES da função ser chamada.')
#         func()
#         print('Algo DEPOIS da função ser chamada.')
#     return wrapper

# @meu_decorador
# def di_ola():
#     print('Olá')

# di_ola()
