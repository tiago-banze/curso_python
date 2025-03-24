# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, nome):
        self._name = None
        self.name = nome
  
    @property
    @abstractmethod
    def name(self):
        pass
  
    @name.setter
    @abstractmethod
    def name(self,nome):
        pass
    
class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)

    # @property
    # def name(self):
    #     return self._name
    
    @AbstractFoo.name.setter
    def name(self,name):
        self._name = name
        
if __name__ == '__main__':
    foo = Foo('telefone')
    print(foo.name)
    print(foo._name)
    foo._name = "televisao"
    print(foo._name)
    