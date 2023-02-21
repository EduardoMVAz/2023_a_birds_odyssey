from abc import abstractmethod

import pygame
import numpy as np


class AbstractBird():

    WIDTH = 800
    HEIGHT = 450

    def update(self):
        self.vel = self.vel + self.acc * 0.1
        self.pos = self.pos + self.vel
        self.acc = np.array([0, 0])

        if self.pos[0]<self.radius or self.pos[0]>self.WIDTH - self.radius or self.pos[1]<self.radius or self.pos[1]>self.HEIGHT - self.radius: # Se eu chegar ao limite da tela, reinicio a posição do personagem
            self.reset()
    
    def crash(self, o):
        d = np.sqrt((self.pos[0] - o.pos[0])**2 + (self.pos[1] - o.pos[1])**2)
        if d < self.radius + o.radius:
            return True
        return False

    def reset(self):
        self.pos = self.s0
        self.vel = np.array([0, 0])
        self.acc = np.array([0, 0])
        
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.pos[0], self.pos[1]), self.radius)
    
    def shoot(self):
        d = pygame.mouse.get_pos() - self.pos
        self.vel = d/np.linalg.norm(d) * 2

    @abstractmethod
    def ability(self):
        pass