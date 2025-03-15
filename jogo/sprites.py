from typing import Any
import pygame
from pygame.locals import*
from sys import exit

# from pygame.sprite import _Group

pygame.init()

largura = 640
altura = 480

largura_altura_janela = (largura ,altura)

preto = (0,0,0)

janela = pygame.display.set_mode(largura_altura_janela)
pygame.display.set_caption('Sprites')

class Sapos(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lista_sprite = []
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_1.png'))
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_2.png'))
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_3.png'))
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_4.png'))
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_5.png'))
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_6.png'))
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_7.png'))
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_8.png'))
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_9.png'))
        self.lista_sprite.append(pygame.image.load('jogo/sprites/animation-master/attack_10.png'))
        self.atual = 0
        self.image = self.lista_sprite[self.atual]
        self.image = pygame.transform.scale(self.image,(128*3, 64*3))
        
        self.rect = self.image.get_rect()
        self.rect.topleft = 100 ,100
        self.animar= False
        
    def atacar(self):
        self.animar = True
        
    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >=  len(self.lista_sprite):
                self.atual = 0
                self.animar = False
            self.image = self.lista_sprite[int(self.atual)]
            self.image = pygame.transform.scale(self.image,(128*3, 64*3))

        
        
todas_sprites = pygame. sprite.Group()       
sapo1 = Sapos()
todas_sprites.add(sapo1)

relogio = pygame.time.Clock() 

while True:
    relogio.tick(10)
    janela.fill(preto)
    for event in pygame.event.get():
        if event.type ==  QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            sapo1.atacar()
            
    todas_sprites.draw(janela)
    todas_sprites.update()
            
    pygame.display.flip()