import pygame
from pygame.locals import*
from sys import exit

pygame.init()

largura = 640
altura = 480

imagem = pygame.image.load('jogo/sprites/animation-master/attack_4.png')
imagem_transformada = pygame.transform.scale(imagem,(largura,altura))

janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('TIAGO')

rodando = True
while rodando:
    janela.fill((0,8,20))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            exit()
    janela.blit(imagem_transformada,(0,0))
    pygame.display.flip()