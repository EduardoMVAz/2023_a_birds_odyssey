import numpy as np
import pygame

class CelestialBody:
    def __init__(self, x, y, radius, gravity, gravity_radius, planet):
        self.pos = np.array([x, y])
        self.vel = np.array([0, 0])
        self.acc = np.array([0, 0])
        self.radius = radius
        self.planets = [pygame.image.load("planet_1.png"), pygame.image.load("planet_2.png"), pygame.image.load("planet_3.png"), pygame.image.load("planet_4.png")]
        self.planet = planet
        self.gravity = Gravity(x, y, gravity, gravity_radius)

    def draw(self, screen):
        screen.blit(self.planets[self.planet], (self.pos[0] - self.radius, self.pos[1] - self.radius))
        self.gravity.draw(screen)
    
    def update(self):
        return


class Gravity:
    def __init__(self, x, y, gravity, radius):
        self.pos = np.array([x, y])
        self.radius = radius
        self.gravity = gravity

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.pos[0], self.pos[1]), self.radius, width=1)