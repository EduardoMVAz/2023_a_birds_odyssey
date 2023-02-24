from abc import abstractmethod
import pygame
import numpy as np

class AbstractLevel():

    WIDTH = 800
    HEIGHT = 450

    MAIN_MENU = "MainMenu"
    LEVEL1 = "Level1"
    LEVEL2 = "Level2"
    lost_rects = {"EXIT": pygame.Rect(229, 259, 130, 45), "TRY AGAIN": pygame.Rect(448, 259, 130, 45)}

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

                if self.perdeu:
                    p = pygame.mouse.get_pos()
                    if self.lost_rects["TRY AGAIN"].collidepoint(p):
                        self.reset()
                    elif self.lost_rects["TRY AGAIN"].collidepoint(p):
                        return self.MAIN_MENU
                elif self.birds[self.current_bird].has_shot == False:
                    self.birds[self.current_bird].shoot()
                elif self.birds[self.current_bird].used_ability == False:
                    self.birds[self.current_bird].ability()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    self.birds[self.current_bird].reset()
                    if self.update_bird_count():
                        self.perdeu = True
        
        return self.update_entities()

    @abstractmethod
    def update_entities(self):
        for group in self.entities.values():
            for e in group:
                e.update()
        
        if not self.perdeu:
            if self.birds[self.current_bird].crash_wall():
                if self.update_bird_count():
                    self.perdeu = True

        if not self.perdeu:            
            self.birds[self.current_bird].update()

            for goals in self.entities["Goals"]:
                if self.birds[self.current_bird].crash(goals):
                    self.birds[self.current_bird].reset()
                    return self.next_level

            for celestial_body in self.entities["Celestial Bodies"]:
                if self.birds[self.current_bird].crash(celestial_body.gravity):
                    d = celestial_body.pos - self.birds[self.current_bird].pos
                    d1 = d/np.linalg.norm(d)
                    self.birds[self.current_bird].acc = d1 * celestial_body.gravity.gravity/np.linalg.norm(d)**2
                
                if self.birds[self.current_bird].name == "GunBird":
                    if self.birds[self.current_bird].bullet.crash(celestial_body):
                        self.birds[self.current_bird].bullet.reset()
                        del self.entities["Celestial Bodies"][self.entities["Celestial Bodies"].index(celestial_body)]
                
                if self.birds[self.current_bird].crash(celestial_body):
                    self.birds[self.current_bird].reset()
                    if self.update_bird_count():
                        self.perdeu = True
                        break

        return self.name

    @abstractmethod
    def draw(self, screen):
        # Desenhar fundo        
        screen.fill(self.colors["BLACK"])
        screen.blit(self.image, (0,0))

        # Desenhar personagem
        for group in self.entities.values():
            for entity in group:
                entity.draw(screen)
        
        # Desenhar passáro
        if self.current_bird < len(self.birds):
            self.birds[self.current_bird].draw(screen)

            if not self.birds[self.current_bird].has_shot:
                self.draw_line_dashed(screen, color=(255, 255, 255), start_pos=pygame.mouse.get_pos(), end_pos=self.birds[self.current_bird].s0 + np.array([self.birds[self.current_bird].radius, self.birds[self.current_bird].radius]))
        
        
        if self.perdeu:
            screen.blit(pygame.image.load("GameOver.png"), (200, 125))
            
        # Update!
        pygame.display.update()

    
    def draw_line_dashed(self, surface, color, start_pos, end_pos, width = 1, dash_length = 10, exclude_corners = True):

        # convert tuples to numpy arrays
        start_pos = np.array(start_pos)
        end_pos   = np.array(end_pos)

        # get euclidian distance between start_pos and end_pos
        length = np.linalg.norm(end_pos - start_pos)

        # get amount of pieces that line will be split up in (half of it are amount of dashes)
        dash_amount = int(length / dash_length)

        # x-y-value-pairs of where dashes start (and on next, will end)
        dash_knots = np.array([np.linspace(start_pos[i], end_pos[i], dash_amount) for i in range(2)]).transpose()

        return [pygame.draw.line(surface, color, tuple(dash_knots[n]), tuple(dash_knots[n+1]), width)
                for n in range(int(exclude_corners), dash_amount - int(exclude_corners), 2)]