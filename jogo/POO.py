class Cachhoros:
    def __init__(self,nome, cor_pelo, idade, tamanho,):
        self.cor_pelo = cor_pelo
        self.nome = nome
        self.idade = idade
        self.tamanho = tamanho
    def latir(self):
        print('au au')
cachoro1 =Cachhoros('toby', 'preto', 5, 'grande')
print(cachoro1.nome)
print(cachoro1.cor_pelo)
print(cachoro1.idade)
print(cachoro1.tamanho)
cachoro1.latir()
        