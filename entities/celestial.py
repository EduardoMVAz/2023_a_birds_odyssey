import numpy as np
import pygame

class CelestialBody:
    def __init__(self, x, y, radius, gravity, gravity_radius):
        self.pos = np.array([x, y])
        self.vel = np.array([0, 0])
        self.acc = np.array([0, 0])
        self.radius = radius
        self.gravity = Gravity(x, y, gravity, gravity_radius)

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.pos[0], self.pos[1]), self.radius)


class Gravity:
    def __init__(self, x, y, gravity, radius):
        self.pos = np.array([x, y])
        self.radius = radius
        self.gravity = gravity

    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.pos[0], self.pos[1]), self.radius, width=1)