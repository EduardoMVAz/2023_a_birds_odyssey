import numpy as np
import pygame

class Goal:
    def __init__(self, x, y, radius):
        self.pos = np.array([x,y])
        self.radius = radius
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.pos[0], self.pos[1]), self.radius)