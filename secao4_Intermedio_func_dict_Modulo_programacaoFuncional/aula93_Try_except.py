# Try, except, else e finally

string = 'tiago' # str

try:
    a=18
    b = 0
    # print('linhsa 1'[1000])
    c = a/b
   
    
except ZeroDivisionError as e:
    print('Dividiu por Zero:', e)
    print( e.__class__.__name__)
except NameError:
    print('Nome nao está definido')
    
except (TypeError, IndexError) as error:
    print('TypeError + IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print("Erro desconhecido")
    
print('Continua')


# try:
#     while True:
#         print(1)
# except InterruptedError:
#     print('programa enterrupido!')