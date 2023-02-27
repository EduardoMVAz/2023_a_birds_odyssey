import numpy as np
import pygame

class Goal:
    '''
    A classe Goal é uma classe simples, sendo o objeto que deve ser acertado pelo jogador com o pássaro.
    '''
    def __init__(self, x, y, radius):
        self.pos = np.array([x,y])
        self.radius = radius

        self.color = (20, 30, 200)
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.pos[0], self.pos[1]), self.radius)
    
    def update(self):
        return