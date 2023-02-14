import pygame
import numpy as np

class MainMenu:
    def __init__(self):
        self.entities = {
            "START": pygame.Rect(100, 50, 200, 75), "OPTIONS": pygame.Rect(100, 200, 200, 75), "CREDITS": pygame.Rect(100, 350, 200, 75)
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}

    def draw(self, screen):
        pygame.draw.rect(screen, self.colors["RED"], self.entities["START"])
        pygame.draw.rect(screen, self.colors["BLUE"], self.entities["OPTIONS"])
        pygame.draw.rect(screen, self.colors["GREEN"], self.entities["CREDITS"])

    def process_events():
        

    def update_entities():
        pass
