import numpy as np
import pygame

from entities.birds.abstract_bird import AbstractBird
from entities.birds.bullet import Bullet


class GunBird(AbstractBird):

    def __init__(self, x, y, vx, vy, radius):
        self.s0 = np.array([x, y])
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])
        self.acc = np.array([0, 0])
        self.radius = radius
        self.has_ability = True
        self.bullet = Bullet(self.pos[0], self.pos[1], self.vel[0], self.vel[1], 1)

        self.color = (255, 255, 255)

    def draw(self, screen, color):
        super().draw
        pygame.draw.circle(screen, self.bullet.color, (self.bullet.pos[0], self.bullet.pos[1]), self.bullet.radius)
    
    def ability(self):
        if self.has_ability:
            d = pygame.mouse.get_pos() - self.pos
            self.bullet.vel = d/np.linalg.norm(d) * 2