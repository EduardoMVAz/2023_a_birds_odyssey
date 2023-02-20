import numpy as np
import pygame

from entities.birds.abstract_bird import AbstractBird


class BasicBird(AbstractBird):

    def __init__(self, x, y, vx, vy, radius):
        self.s0 = np.array([x, y])
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])
        self.acc = np.array([0, 0])
        self.radius = radius

        self.color = (30, 200, 20)
    
    def ability(self):
        self.vel = self.vel * 2
        self.acc = 0