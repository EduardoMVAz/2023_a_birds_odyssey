from abc import abstractmethod
import pygame
import numpy as np

class AbstractLevel():

    WIDTH = 800
    HEIGHT = 450

    MAIN_MENU = "MainMenu"
    LEVEL1 = "Level1"
    LEVEL2 = "Level2"

    def update_bird_count(self):
        self.current_bird += 1
        return self.current_bird == len(self.birds)    

    @abstractmethod
    def reset(self):
        self.__init__()

    @abstractmethod
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
                    if self.update_bird_count():
                        return "MainMenu"
        
        return self.update_entities()

    @abstractmethod
    def update_entities(self):
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
                if self.update_bird_count():
                    return self.MAIN_MENU
        
        for goals in self.entities["Goals"]:
            if self.birds[self.current_bird].crash(goals):
                self.birds[self.current_bird].reset()
                return self.next_level
        
        if self.birds[self.current_bird].crash_wall():
            if self.update_bird_count():
                return self.MAIN_MENU
        
        return self.name

    @abstractmethod
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