# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       DEVE ser usado dentro da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.


class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protegido'
        self.__private = 'Isso e privado'
        self._protected_method()
        
    
    def metodo_public(self):
        return 'Metodo_Publico'
    
    def _protected_method(self):
        return 'Metodo_protegido'
    
    @property
    def private(self):
        return self.__private
    
f = Foo()

print(f.metodo_public())
print(f._protected_method())