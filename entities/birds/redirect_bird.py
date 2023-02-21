import numpy as np
import pygame

from entities.birds.abstract_bird import AbstractBird


class RedirectBird(AbstractBird):

    def __init__(self, x, y, vx, vy, radius):
        super().__init__(x, y, vx, vy, radius)

        self.color = (0, 255, 255)
    
    def ability(self):
        d = pygame.mouse.get_pos() - self.pos
        self.vel = d/np.linalg.norm(d) * 2
        self.used_ability = True