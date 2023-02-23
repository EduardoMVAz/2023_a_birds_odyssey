import pygame
import numpy as np

from screens.abstract_level import AbstractLevel

class MainMenu(AbstractLevel):

    def __init__(self):
        
        self.entities = {
            "START": pygame.Rect(260, 225, 280, 125), 
            "OPTIONS": pygame.Rect(260, 378, 120, 54), 
            "CREDITS": pygame.Rect(419, 378, 120, 54)
        }
        self.meteor = {"POS_0": np.array([-10, 225]), "POS": np.array([-10, 225]), "VEL": np.array([5,-5]), "IMG": pygame.image.load("comet.png")}
        self.image = pygame.image.load("MainMenu.png")

        self.name = "MainMenu"

    def draw(self, screen):

        screen.fill((0,0,0))
        screen.blit(self.image, (0,0))
        screen.blit(self.meteor["IMG"], self.meteor["POS"])
        
        self.meteor["POS"] += self.meteor["VEL"]
        if self.meteor["POS"][1] < -100:
            self.meteor["POS"] = self.meteor["POS_0"]

        pygame.display.update()
        
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.update_entities()
        return self.name

    def update_entities(self):
        p = pygame.mouse.get_pos()
        if self.entities["START"].collidepoint(p):
            return "Level1"
        elif self.entities["OPTIONS"].collidepoint(p):
            return "placeholder_options"
        elif self.entities["CREDITS"].collidepoint(p):
            return "placeholder_credits"
        return self.name

