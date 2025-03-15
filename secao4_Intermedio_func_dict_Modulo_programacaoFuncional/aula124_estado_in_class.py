# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando = False, fotografando = False):
        self.nome= nome
        self.filmando = filmando
        self.fotografando = fotografando
        
    def filmar(self):
        if self.fotografando:
            print(f'{self.nome} não pode filmar, porque está sendo usada para fotografar!')
        else:
            if not self.filmando:
                self.filmando = True
                print(f'{self.nome} está filmando')
            
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar...')
            return
        self.filmando = True 
        print(f'{self.nome} está fotografando')
        
c1 = Camera('Canon')
c1.filmar()
c1.fotografar()

