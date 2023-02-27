import numpy as np
import pygame

class CelestialBody:
    '''
    A classe CelestialBody é classe dos obstáculos que possuem gravidade, ou seja, os planetas.
    Esses obstáculos exercem gravidade sobre os pássaros, e são os principais desafios das fases.
    Esses objetos possuem uma relação com outro objeto, a Gravidade, que representa seu campo
    gravitacional. A gravidade é criada ao inicializar o objeto CelestialBody.
    '''

    def __init__(self, x, y, radius, gravity, gravity_radius, planet):
        self.pos = np.array([x, y])
        self.vel = np.array([0, 0])
        self.acc = np.array([0, 0])
        self.radius = radius
        self.planets = [pygame.image.load("assets/planet_1.png"), pygame.image.load("assets/planet_2.png"), pygame.image.load("assets/planet_3.png"), pygame.image.load("assets/planet_4.png")]
        self.planet = planet
        self.gravity = Gravity(x, y, gravity, gravity_radius)

    def draw(self, screen):
        screen.blit(self.planets[self.planet], (self.pos[0] - self.radius, self.pos[1] - self.radius))
        self.gravity.draw(screen)
    
    def update(self):
        return


class Gravity:
    '''
    A gravidade é um classe complementar de CelestialBody, que representa o Campo gravitacional do planeta.
    Sua função draw desenha um círculo branco ao redor do planeta, para sinalizar o campo gravitacional ao jogador.
    '''    
    def __init__(self, x, y, gravity, radius):
        self.pos = np.array([x, y])
        self.radius = radius
        self.gravity = gravity

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.pos[0], self.pos[1]), self.radius, width=1)