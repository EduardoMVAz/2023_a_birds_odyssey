import numpy as np
import pygame

from entities.birds.abstract_bird import AbstractBird
from entities.birds.bullet import Bullet


class GunBird(AbstractBird):

    def __init__(self, x, y, vx, vy, radius):
        super().__init__(x, y, vx, vy, radius)

        self.color = (255, 255, 255)
        self.bullet = Bullet(self.pos[0], self.pos[1], self.vel[0], self.vel[1], 1)


    def draw(self, screen):
        super().draw(screen)
        pygame.draw.circle(screen, self.bullet.color, (self.bullet.pos[0], self.bullet.pos[1]), self.bullet.radius)


    def ability(self):
        d = pygame.mouse.get_pos() - self.pos
        self.bullet.vel = d/np.linalg.norm(d) * 2
        self.used_ability = True