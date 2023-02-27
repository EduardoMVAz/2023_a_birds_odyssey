import pygame
import numpy as np

from screens.abstract_level import AbstractLevel

class MainMenu(AbstractLevel):
    '''
    A tela MainMenu é muito mais simples que as fases em sí, portanto seu código não herda de AbstractLevel,
    em vez disso, ele é todo único. As únicas verificações necessárias são de elementos visuais (cometa) e 
    os botões de START, CREDITS e EXIT.
    '''

    def __init__(self):
        
        self.entities = {
            "START": pygame.Rect(260, 225, 280, 125), 
            "CREDITS": pygame.Rect(260, 378, 120, 54), 
            "EXIT": pygame.Rect(419, 378, 120, 54)
        }
        self.comet = {"POS_0": np.array([-10, 225]), "POS": np.array([-10, 225]), "VEL": np.array([5,-5]), "IMG": pygame.image.load("assets/comet.png")}
        self.image = pygame.image.load("assets/MainMenu.png")

        self.name = "MainMenu"

    def draw(self, screen):

        screen.fill((0,0,0))
        screen.blit(self.image, (0,0))
        screen.blit(self.comet["IMG"], self.comet["POS"])
        
        self.comet["POS"] += self.comet["VEL"]
        if self.comet["POS"][1] < -100:
            self.comet["POS"] = self.comet["POS_0"]

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
            return self.LEVEL1
        elif self.entities["EXIT"].collidepoint(p):
            return "Quit"
        elif self.entities["CREDITS"].collidepoint(p):
            return "Credits"
        return self.name

