import pygame
from pygame.locals import *
from sys import exit
from random import randint

# pygame.mixer.music.set_volume(0.1)

# musica_fundo = pygame.mixer.music.load('jjogo/smw_lemmy_wendy_correct.wav')
# pygame.mixer.music.play(-1)
# barrulho = pygame.mixer.Sound('jogo/smw_coin.wav')
# barrulho.set_volume(0.2)

pygame.init()
largura = 640
altura = 438
x_cobra = int(largura /2 - 50/2)
y_cobra = int(altura/2 - 50/2)

velocidade = 10
x_controle = velocidade
y_controle =0


x_maca = randint(40, 600)
y_maca = randint(50, 430)

morreu = False

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

janela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Tiago banze')
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5

def aumenta_cobra (lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(janela, (0,255,0),(xey[0],xey[1], 20,20))
        
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra,y_cobra,lista_cobra,lista_cabeca, x_maca,y_maca, morreu
    pontos = 0
    comprimento_inicial =5
    x_cobra = int(largura /2 - 50/2)
    y_cobra = int(altura/2 - 50/2) 
    lista_cobra=[]
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False 
     

while True:
    relogio.tick(30) 
    janela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    text_formatado = fonte.render(mensagem, True, (0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit
        
        if event.type ==KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra+y_controle
    cobra = pygame.draw.rect(janela, (0, 255, 0),(x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(janela, (255,0,0),(x_maca,y_maca,20,20))
    
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos +=1
        # barrulho.play()
        comprimento_inicial += 1
        
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)
    
    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 20,True, True)
        mensagem = 'Game over! Pressione a tecla R para jogar novamente.'
        texto_formatado = fonte2.render(mensagem, True, (0,0,0))
        rect_texto = texto_formatado.get_rect()
        morreu =True
        while morreu:
            janela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type ==KEYDOWN:
                    if event.key ==K_r:
                        reiniciar_jogo()
            rect_texto.center = (largura//2 ,altura//2) 
            janela.blit(texto_formatado, rect_texto)
            pygame.display.update()
    if x_cobra > largura:
        x_cobra =0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0
    
    if len(lista_cobra)> comprimento_inicial:
        del lista_cobra[0]
    
    aumenta_cobra(lista_cobra)
 
    janela.blit(text_formatado, (450,40))
    pygame.display.update()