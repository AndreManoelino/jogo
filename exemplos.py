import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('smw_game_over.wav')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')
barulho_colisao.set_volume(0.5)

largura = 1000
altura = 600
x = int(largura / 2)
y = int(altura / 2)

x_azul = randint(40, 600)
y_azul = randint(50, 460)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, bold=True, italic=True)
texto_formatado = fonte.render(f'Pontos: {pontos}', True, (255, 255, 255))

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo')
relogio = pygame.time.Clock()

snake = pygame.Surface((40, 50))
snake.fill((0, 255, 0))

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    if pygame.key.get_pressed()[K_a]:
        x = x - 10
    if pygame.key.get_pressed()[K_d]:
        x = x + 10
    if pygame.key.get_pressed()[K_w]:
        y = y - 10
    if pygame.key.get_pressed()[K_s]:
        y = y + 10

    cobra = pygame.Rect(x, y, 40, 50)
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_azul, y_azul, 40, 50))

    if cobra.colliderect(maca):
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()

    tela.blit(texto_formatado, (450, 40))
    tela.blit(snake, (x, y))
    pygame.display.update()
