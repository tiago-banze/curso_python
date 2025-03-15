## **Básico**  

### **1. Criando um Iterável Básico**  
# Crie uma classe chamada `MeuIteravel` que implemente 
# `__iter__` e retorne um iterador. O iterador deve 
# percorrer uma lista de números de 1 a 5. 
class MeuIteravel:
    def __iter__(self):
        self.iteravel = [1, 2, 3, 4, 5]
        return iter(self.iteravel)
    
# m = MeuIteravel()

# for numero in m:
#     print(numero)
# for numero in m:
#     print(numero)


# ### **2. Criando um Iterador Personalizado**  
# Implemente uma classe `Contador` que recebe um 
# valor inicial e um valor final e itera de forma
# crescente. Utilize os métodos `__iter__` e 
# `__next__`.
class Contador:
    def __init__(self, inicio, fim):
        self.fim = fim
        self.actul = inicio
    
    def __iter__(self):
          return self
    
    def __next__(self):
        if self.actul >self.fim:
            raise StopIteration
        valor_actual = self.actul
        self.actul += 1
        return valor_actual
    
# contador = Contador(1,5)

# print(contador.__next__())
# print(contador.__next__())
# print(contador.__next__())
# print(contador.__next__())
# print(contador.__next__())
# print(contador.__next__())



# **Intermediário**  

# ### **3. Iterador Reverso**  
# Crie um iterador chamado `Reverso` que recebe
# uma string e a percorre de trás para frente.  

class Reverso:
    def __init__(self, string):
        self.string = string
        self.pos = len(string)
        
    def __iter__(self):
        return self

    def __next__(self):
        if self.pos == 0:
            raise StopIteration
        self.pos -=1
        return self.string[self.pos]

# r = Reverso('Tiago')
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())
# print(r.__next__())
# print(list(r.__next__()))


# **4. Iterador Infinito**  
# Implemente um iterador `Ciclo` que recebe
# uma lista e percorre infinitamente seus 
# elementos.

class Ciclo:
    def __init__(self,lista):
        self.lista = lista
        self.i = 0
        
    def __iter__(self):
        return self
    @property
    def __next__(self):
        if not self.lista:
            raise StopIteration
        vvalor = self.lista[self.i]
        self.i = (self.i + 1) % len(self.lista)
        
        return vvalor

# c = Ciclo([1,2,3,4,5,6])
