import pygame
from pygame.locals import *
from sys import exit
from random import randint

# Inicializando o Pygame
pygame.init()

pygame.mixer.music.set_volume(0.1)

musica_fundo = pygame.mixer.music.load('jogo/Eminem_-_Not_Afraid(256k).mp3')
pygame.mixer.music.play(-1)
barrulho = pygame.mixer.Sound('jogo/Eminem_-_Lose_Yourself_[HD](256k).mp3')
barrulho.set_volume(0.2)

# Definindo a largura e altura da janela do jogo
largura = 640
altura = 480
x = int(largura /2 - 50/2)
y = int(altura/2 - 50/2)
x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

# Criando a janela do jogo
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo do Banze')  # Definindo o título da janela
relogio = pygame.time.Clock()

# Loop principal do jogo
while True:
    relogio.tick(30) 
    janela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    text_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:  # Se o evento for QUIT, encerra o jogo
            pygame.quit()
            exit()
                     
        if pygame.key.get_pressed()[K_a]:
            x = x - 20 
        if pygame.key.get_pressed()[K_d]:
            x = x + 20 
        if pygame.key.get_pressed()[K_w]:
            y = y - 20 
        if pygame.key.get_pressed()[K_s]:
            y = y + 20 
            
          
    # Desenhando formas na janela
    rect_vermelho = pygame.draw.rect(janela, (255, 0, 0), (x, y, 50, 50))  # Desenhando um retângulo
    rect_azul = pygame.draw.rect(janela, (0, 0, 255), (x_azul, y_azul, 50, 50))  # Desenhando um retângulo
    
    if rect_vermelho.colliderect(rect_azul):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos +=1
        barrulho.play()

    janela.blit(text_formatado, (450,40))
    pygame.display.update()