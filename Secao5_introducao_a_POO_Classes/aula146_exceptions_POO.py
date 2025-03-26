 # Criando Exceptions em Python Orientado a Objetos
 # Para criar uma Exception em Python, você só
 # precisa herdar de alguma exceção da linguagem.
 # A recomendação da doc é herdar de Exception.
 # https://docs.python.org/3/library/exceptions.html
 # Criando exceções (comum colocar Error ao final)
 # Levantando (raise) / Lançando (throw) exceções
 # Relançando exceções
 # Adicionando notas em exceções (3.11.0)
 
class MyError(Exception):
    pass

class OutroError(Exception):
    pass

def lenvantar_exception():
    exception_ = MyError("a","b","c")
    exception_.add_note("Olha a nota 1")
    exception_.add_note("voce errou")
    raise exception_
try:
    # 1/0
    lenvantar_exception()
except (MyError, ZeroDivisionError) as errorr:
    print(errorr.args)
    print(errorr.__class__.__name__)
    print()
    exception_ = OutroError("Vou lancar de novo")
    exception_.__notes__ = errorr.__notes__.copy()
    raise exception_ from errorr