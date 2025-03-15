# try, except, else e finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions

try:
    print("ABRIR ARQUIVO")
    print()
    8/1

except ZeroDivisionError as e:# captura do erro
    print('ERRO: ',e)
    print('TIPO DE ERRO: ',e.__class__.__name__)
    print()
else:
    print('Não deu nenhum erro!')
    print()
finally:
    print('Fechar ARQUIVO')