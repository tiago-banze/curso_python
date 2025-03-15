import pygame

pygame.init()

janela = pygame.display.set_mode((800,600))
azul_fundo = (178,200,167)
tela_fundo =  janela.fill(azul_fundo)

relogio = pygame.time.Clock()

while True:
    tela_fundo
    pygame.display.flip()
pygame.quit()
quit