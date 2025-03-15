# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.
class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self. enderecos = []
        
    def insirir_endereco(self, rua, numero_casa):
        self.enderecos.append(Endereco(rua, numero_casa))
        
    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero_casa)