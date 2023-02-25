import numpy as np
import pygame

class Bullet:

    def __init__(self, x, y, vx, vy, radius):
        self.s0 = np.array([x, y])
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])
        self.radius = radius
        self.hit = False

        self.image = pygame.image.load("assets/bullet.png")
    
    def update(self):
        self.pos = self.pos + self.vel * 2

    def crash(self, o):
        d = np.sqrt((self.pos[0] - o.pos[0])**2 + (self.pos[1] - o.pos[1])**2)
        if d < self.radius + o.radius:
            return True
        return False
    
    def reset(self):
        self.vel = np.array([0,0])
        self.hit = True
    
    def draw(self, screen):
        screen.blit(self.image, (self.pos[0], self.pos[1]))