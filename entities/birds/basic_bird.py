import numpy as np
import pygame

from entities.birds.abstract_bird import AbstractBird


class BasicBird(AbstractBird):

    def __init__(self, x, y, vx, vy, radius):
        super().__init__(x, y, vx, vy, radius)

        self.color = (30, 200, 20)
    
    def ability(self):
        self.vel = self.vel * 2
        self.acc = 0
        self.used_ability = True