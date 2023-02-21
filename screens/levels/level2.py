import pygame
import numpy as np

from screens.abstract_level import AbstractLevel

from entities.celestial import CelestialBody
from entities.birds.basic_bird import BasicBird
from entities.goal import Goal

class Level2(AbstractLevel):

    def __init__(self):
        self.birds = [
            BasicBird(50, 200, 0, 0, 5),
        ]

        self.entities = {
            "Celestial Bodies" : [
                CelestialBody(x=400, y=110, radius=10, gravity=2500, gravity_radius=100),
                CelestialBody(x=400, y=290, radius=10, gravity=2500, gravity_radius=100),
            ],
            "Goals" : [
                Goal(750, 200, 20)
            ]
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}

        self.name = "Level2"

        self.current_bird = 0


    def reset(self):
        self.__init__()


    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.birds[self.current_bird].has_shot == False:
                    self.birds[self.current_bird].shoot()
                elif self.birds[self.current_bird].used_ability == False:
                    self.birds[self.current_bird].ability()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.birds[self.current_bird].reset()
                    self.current_bird += 1
        
        return self.update_entities()
    

    def update_entities(self):
        if self.current_bird == len(self.birds):
            return "MainMenu"

        for group in self.entities.values():
            for e in group:
                e.update()

        self.birds[self.current_bird].update()
        
        for celestial_body in self.entities["Celestial Bodies"]:
            if self.birds[self.current_bird].crash(celestial_body.gravity):
                d = celestial_body.pos - self.birds[self.current_bird].pos
                d1 = d/np.linalg.norm(d)
                self.birds[self.current_bird].acc = d1 * celestial_body.gravity.gravity/np.linalg.norm(d)**2
            
            if self.birds[self.current_bird].crash(celestial_body):
                self.birds[self.current_bird].reset()

                self.current_bird += 1
        
        for goals in self.entities["Goals"]:
            if self.birds[self.current_bird].crash(goals):
                self.birds[self.current_bird].reset()
                return "MainMenu"
        
        if self.birds[self.current_bird].crash_wall():
            self.current_bird += 1
        
        return self.name


    def draw(self, screen):
        # Desenhar fundo        
        screen.fill(self.colors["BLACK"])

        # Desenhar personagem
        for group in self.entities.values():
            for entity in group:
                entity.draw(screen, entity.color)
        
        # Desenhar passáro
        if self.current_bird < len(self.birds):
            self.birds[self.current_bird].draw(screen)
        
        # Update!
        pygame.display.update()