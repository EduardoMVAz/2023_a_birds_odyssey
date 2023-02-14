import pygame
import numpy as np

from entities.celestial import CelestialBody
from entities.bird import Bird
from entities.goal import Goal

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
COR_GOAL = (20, 30, 200)

# Inicializar posicoes
s0 = np.array([50,200])
v0 = np.array([15, -15]) * 0.1
s0_corpo_celeste = np.array([600,200])

bird = Bird(s0[0], s0[1], 0, 0, 5)
corpo_celeste = CelestialBody(x=s0_corpo_celeste[0], y=s0_corpo_celeste[1], radius=10, gravity=2500, gravity_radius=100)
goal = Goal(750, 200, 20)


rodando = True
while rodando:
    # Capturar eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            d = pygame.mouse.get_pos() - bird.pos
            bird.vel = d/np.linalg.norm(d) * 2


    if bird.pos[0]<bird.radius or bird.pos[0]>WIDTH - bird.radius or bird.pos[1]<bird.radius or bird.pos[1]>HEIGHT - bird.radius or bird.crash(corpo_celeste): # Se eu chegar ao limite da tela, reinicio a posição do personagem
        bird.pos = s0
        bird.vel = 0

    # Controlar frame rate
    clock.tick(FPS)
    
    if bird.crash(corpo_celeste.gravity):
        d = corpo_celeste.pos - bird.pos
        d1 = d/np.linalg.norm(d)
        bird.acc = d1 * corpo_celeste.gravity.gravity/np.linalg.norm(d)**2
    elif (bird.crash(goal)):
        rodando = False
    else:
        bird.acc = np.array([0,0])

    # Processar posicoes
    bird.update()

    # Desenhar fundo
    screen.fill(BLACK)

    # Desenhar personagem
    corpo_celeste.draw(screen, COR_CORPO_CELESTE)
    bird.draw(screen, COR_PERSONAGEM)
    corpo_celeste.gravity.draw(screen, COR_CORPO_CELESTE)
    goal.draw(screen, COR_GOAL)

    # Update!
    pygame.display.update()

# Terminar tela
pygame.quit()