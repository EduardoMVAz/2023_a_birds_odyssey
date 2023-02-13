import pygame
import numpy as np

from entities.celestial import CelestialBody
from entities.rock import Bird

pygame.init()

# Tamanho da tela e definição do FPS
WIDTH = 800
HEIGHT = 450
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()
FPS = 60  # Frames per Second

BLACK = (0, 0, 0)
COR_PERSONAGEM = (30, 200, 20)
COR_CORPO_CELESTE = (200, 30, 20)

# Inicializar posicoes
s0 = np.array([50,200])
v0 = np.array([15, -15]) * 0.1
s0_corpo_celeste = np.array([600,200])

pedra = Bird(s0[0], s0[1], 0, 0, 5)
corpo_celeste = CelestialBody(s0_corpo_celeste[0], s0_corpo_celeste[1], 10, 0.1, 100)


rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            d = pygame.mouse.get_pos() - pedra.pos
            pedra.vel = d/np.linalg.norm(d) * 5


    if pedra.pos[0]<pedra.radius or pedra.pos[0]>WIDTH - pedra.radius or pedra.pos[1]<pedra.radius or pedra.pos[1]>HEIGHT - pedra.radius or pedra.crash(corpo_celeste): # Se eu chegar ao limite da tela, reinicio a posição do personagem
        pedra.pos = s0
        pedra.vel = 0

    # Controlar frame rate
    clock.tick(FPS)
    
    if pedra.crash(corpo_celeste.gravity):
        d = pedra.pos - corpo_celeste.pos
        d = d/np.linalg.norm(d)
        pedra.acc = corpo_celeste.gravity.gravity/d**2
    else:
        pedra.acc = np.array([0,0])

    # Processar posicoes
    pedra.update()

    # Desenhar fundo
    screen.fill(BLACK)

    # Desenhar personagem
    pygame.draw.circle(screen, COR_CORPO_CELESTE, (corpo_celeste.pos[0], corpo_celeste.pos[1]), corpo_celeste.radius)
    pygame.draw.circle(screen, COR_PERSONAGEM, (pedra.pos[0], pedra.pos[1]), pedra.radius)

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()