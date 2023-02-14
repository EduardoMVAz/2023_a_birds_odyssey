import pygame
import numpy as np

class MainMenu:
    def __init__(self):
        self.entities = {}
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}

    @classmethod 
    def process_events(self):
        pygame.window.rect()
