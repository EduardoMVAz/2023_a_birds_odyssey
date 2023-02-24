from abc import abstractmethod

import pygame
import numpy as np


class AbstractBird():

    WIDTH = 800
    HEIGHT = 450

    BASIC_BIRD = "BasicBird"
    REDIRECT_BIRD = "RedirectBird"
    GUN_BIRD = "GunBird"

    def __init__(self, x, y, vx, vy, radius):
        self.s0 = np.array([x, y])
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])
        self.acc = np.array([0, 0])
        self.radius = radius

        self.used_ability = False
        self.has_shot = False

    def update(self):
        self.vel = self.vel + self.acc * 0.1
        self.pos = self.pos + self.vel
        self.acc = np.array([0, 0])
    
    def crash(self, o):
        d = np.sqrt((self.pos[0] - o.pos[0])**2 + (self.pos[1] - o.pos[1])**2)
        if d < self.radius + o.radius:
            return True
        return False

    def crash_wall(self):
        if self.pos[0]<self.radius or self.pos[0]>self.WIDTH - self.radius or self.pos[1]<self.radius or self.pos[1]>self.HEIGHT - self.radius: # Se eu chegar ao limite da tela, reinicio a posição do personagem
            self.reset()
            return True
        return False

    def reset(self):
        self.pos = self.s0
        self.vel = np.array([0, 0])
        self.acc = np.array([0, 0])

        self.has_shot = False
        self.used_ability = False
        
    
    def draw(self, screen):
        screen.blit(self.image, (self.pos[0] - self.radius, self.pos[1] - self.radius))
    
    def shoot(self):
        d = pygame.mouse.get_pos() - self.pos
        self.vel = d/120

        self.has_shot = True

    @abstractmethod
    def ability(self):
        pass