# Relações entre classes: associação, agregação e composição
# Agregação é uma forma mais especializada de associação
# entre dois ou mais objetos. Cada objeto terá
# seu ciclo de vida independente.
# Geralmente é uma relação de um para muitos, onde um
# objeto tem um ou muitos objetos.
# Os objetos podem viver separadamente, mas pode
# se tratar de uma relação onde um objeto precisa de
# outro para fazer determinada tarefa.
# (existem controvérsias sobre as definições de agregação).

class Cliente:
    def __init__(self, name):
        self.name = name
        self.enderecos = []
    
    def inserir_endereco(self,rua, numero):
        self.enderecos.append(Enderecos(rua, numero))
        
    def listar_enderecos(self):
        for  endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

class Enderecos:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero
    
    def __del__(self):
        print('Apagando,' , self.rua, self.numero)
        
cliente1 = Cliente('Tiago')

cliente1.inserir_endereco('10 de novembro' , 125)
cliente1.inserir_endereco('25 de  junho' , 15)
cliente1.inserir_endereco('bairro novo' , 5)


print(cliente1.name)
cliente1.listar_enderecos()


# class CarrinhoDeCompra:
#     def __init__(self):
#         self._produtos = []
        
#     def inserir_produtos(self, *produtos):
#         for produto in produtos:
#             self._produtos.append(produto)
    
#     def total(self):
#         return sum([p.preco for p in self._produtos])
    
#     def Lista_Produtos(self):
#         for produto in self._produtos:
#             print(produto.nome, produto.preco)

# class Produtos:
#     def __init__(self, nome, preco):
#         self.nome =nome
#         self.preco = preco
        
# cariinho = CarrinhoDeCompra()
# produto, produto2 = Produtos("cante", 10), Produtos('caderno', 120)

# cariinho.inserir_produtos(produto, produto2)
# cariinho.Lista_Produtos()
# print(cariinho.total())