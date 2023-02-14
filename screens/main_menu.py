import pygame
import numpy as np

class MainMenu:
    def __init__(self):
        
        self.entities = {
            "START": pygame.Rect(100, 50, 200, 75), 
            "OPTIONS": pygame.Rect(100, 200, 200, 75), 
            "CREDITS": pygame.Rect(100, 350, 200, 75)
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}

        self.name = "MainMenu"

    def draw(self, screen):

        screen.fill(self.colors["BLACK"])

        pygame.draw.rect(screen, self.colors["RED"], self.entities["START"])
        pygame.draw.rect(screen, self.colors["BLUE"], self.entities["OPTIONS"])
        pygame.draw.rect(screen, self.colors["GREEN"], self.entities["CREDITS"])

        pygame.display.update()
        
    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
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

