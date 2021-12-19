from pygame import display, init, time as pytime, draw, event, quit
from pygame import QUIT, K_LEFT, K_RIGHT, K_DOWN, K_UP
import pygame

init()

x = 400
y = 300

velocidade = 1

janela = display.set_mode((800,600))
display.set_caption("Desenho      Click no x para fechar no final.")

j_b = True
while j_b :


    for event in pygame.event.get():
            if event.type == QUIT:
                j_b = False



    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y -= velocidade
    if comandos[pygame.K_DOWN]:
        y += velocidade
    if comandos[pygame.K_RIGHT]:
        x += velocidade
    if comandos[pygame.K_LEFT]:
        x -= velocidade

    draw.circle(janela, (0,255,0),(x,y),10)
    display.update()








pygame.quit()
