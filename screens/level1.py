import pygame
import numpy as np

from entities.celestial import CelestialBody
from entities.bird import Bird
from entities.goal import Goal

from screens.main_menu import MainMenu


class Level1:

    WIDTH = 800
    HEIGHT = 450

    def __init__(self):
        self.entities = {
            "Bird" : Bird(50, 200, 0, 0, 5),
            "Celestial Body" : CelestialBody(x=600, y=200, radius=10, gravity=2500, gravity_radius=100),
            "Goal" : Goal(750, 200, 20)
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.entities["Bird"].shoot()
        
        return self.update_entities()
    

    def update_entities(self):
        for e in self.entities.values():
            e.update()
        
        if self.entities["Bird"].crash(self.entities["Celestial Body"].gravity):
            d = self.entities["Celestial Body"].pos - self.entities["Bird"].pos
            d1 = d/np.linalg.norm(d)
            self.entities["Bird"].acc = d1 * self.entities["Celestial Body"].gravity.gravity/np.linalg.norm(d)**2
        
        if self.entities["Bird"].crash(self.entities["Celestial Body"]):
            self.entities["Bird"].reset()
        
        if self.entities["Bird"].crash(self.entities["Goal"]):
            return MainMenu()

        return self


    def draw(self, screen):
        # Desenhar fundo        
        screen.fill(self.colors["BLACK"])

        # Desenhar personagem
        for e in self.entities.values():
            e.draw(screen, e.color)
        
        # Update!
        pygame.display.update()