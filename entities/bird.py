import numpy as np
import pygame

class Bird:

    WIDTH = 800
    HEIGHT = 450

    def __init__(self, x, y, vx, vy, radius):
        self.s0 = np.array([x, y])
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])
        self.acc = np.array([0, 0])
        self.radius = radius

        self.color = (30, 200, 20)
    
    def update(self):
        self.vel = self.vel + self.acc * 0.1
        self.pos = self.pos + self.vel
        self.acc = 0

        if self.pos[0]<self.radius or self.pos[0]>self.WIDTH - self.radius or self.pos[1]<self.radius or self.pos[1]>self.HEIGHT - self.radius: # Se eu chegar ao limite da tela, reinicio a posição do personagem
            self.reset()
    
    def crash(self, o):
        d = np.sqrt((self.pos[0] - o.pos[0])**2 + (self.pos[1] - o.pos[1])**2)
        if d < self.radius + o.radius:
            return True
        return False

    def reset(self):
        self.pos = self.s0
        self.vel = 0
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.pos[0], self.pos[1]), self.radius)
    
    def shoot(self):
        d = pygame.mouse.get_pos() - self.pos
        self.vel = d/np.linalg.norm(d) * 2