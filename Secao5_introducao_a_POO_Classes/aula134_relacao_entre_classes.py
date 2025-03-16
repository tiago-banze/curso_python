# Relações entre classes: associação, agregação e composição
# Associação é um tipo de relação onde os objetos
# estão ligados dentro do sistema.
# Essa é a relação mais comum entre objetos e tem subconjuntos
# como agregação e composição (que veremos depois).
# Geralmente, temos uma associação quando um objeto tem
# um atributo que referencia outro objeto.
# A associação não especifica como um objeto controla
# o ciclo de vida de outro objeto.
class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever

print(caneta.escrever())
print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())


# class Motor:
#     def __init__(self, tipo):
#         self._tipo = tipo
        
#     @property
#     def tipo(self):
#         return self._tipo
    
# class Carro:
#     def __init__(self, marca, motor):
#         self._marca = marca
#         self._motor = motor
    
#     @property
#     def marca(self):
#         return self._marca
        
#     @property
#     def motor(self):
#         return self._motor
    
# motor_v8 = Motor("V8")

# carro1 = Carro("Mercedes", motor_v8)

# print(f'Carro de marca {carro1.marca} tem um motor {carro1.motor.tipo} 😜')