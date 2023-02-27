import numpy as np
import pygame

class Meteor:
    '''
    A classe Meteor serve somente como obstáculo aos pássaros, sem possuir campo gravitacional.
    '''
    def __init__(self, x, y, radius):
        self.pos = np.array([x, y])
        self.radius = radius
        self.image = pygame.image.load("assets/meteoro1.png")
    
    def draw(self, screen):
        screen.blit(self.image, (self.pos[0] - self.radius, self.pos[1] - self.radius))

    def update(self):
        return