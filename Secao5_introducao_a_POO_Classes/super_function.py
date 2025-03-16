class Animal:
    def falar(self):
        print('O animal faz um som...')

class Cachorro(Animal):
    def falar(self):
        super().falar()
        print('O cachorro está latindo...')


cachorro = Cachorro()
cachorro.falar()