import numpy as np
import pygame

from entities.birds.abstract_bird import AbstractBird


class RedirectBird(AbstractBird):

    def __init__(self, x, y, vx, vy, radius):
        self.s0 = np.array([x, y])
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])
        self.acc = np.array([0, 0])
        self.radius = radius
        self.has_ability = True

        self.color = (0, 255, 255)
    
    def ability(self):
        if self.has_ability:
            d = pygame.mouse.get_pos() - self.pos
            self.vel = d/np.linalg.norm(d) * 2
            self.has_ability = False