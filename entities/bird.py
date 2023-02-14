import numpy as np
import pygame

class Bird:
    def __init__(self, x, y, vx, vy, radius):
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])
        self.acc = np.array([0, 0])
        self.radius = radius
    
    def update(self):
        self.vel = self.vel + self.acc * 0.1
        self.pos = self.pos + self.vel
    
    def crash(self, o):
        d = np.sqrt((self.pos[0] - o.pos[0])**2 + (self.pos[1] - o.pos[1])**2)
        if d < self.radius + o.radius:
            return True
        return False
    
    def draw(self, screen, color):
        pygame.draw.circle(screen, color, (self.pos[0], self.pos[1]), self.radius)