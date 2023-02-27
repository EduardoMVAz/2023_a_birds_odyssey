from abc import abstractmethod
import pygame
import numpy as np

# As fases principais são todas heranças da classe AbstractLevel, portanto todo procedimento genérico é realizado nessa classe.

class AbstractLevel():

    WIDTH = 800
    HEIGHT = 450

    MAIN_MENU = "MainMenu"
    LEVEL1 = "Level1"
    LEVEL2 = "Level2"
    LEVEL3 = "Level3"
    LEVEL4 = "Level4"
    LEVEL5 = "Level5"
    CREDITS = "Credits"
    lost_rects = {"EXIT": pygame.Rect(229, 259, 130, 45), "TRY AGAIN": pygame.Rect(448, 259, 130, 45)}


    def update_bird_count(self):
        # A função update_bird_count aumenta o contador current_bird, informando que ouve uma troca de pássaros.
        self.current_bird += 1
        return self.current_bird == len(self.birds)    

    @abstractmethod
    def reset(self):
        # função para resetar a fase.
        self.__init__()

    @abstractmethod
    def process_events(self):
        # A função process_events verifica os eventos do pygame, fazendo as checagens necessárias do tiro e da abilidade dos
        # pássaros, de acordo com clicks do mouse.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:

                if self.perdeu:
                    p = pygame.mouse.get_pos()
                    if self.lost_rects["TRY AGAIN"].collidepoint(p):
                        self.reset()
                    elif self.lost_rects["EXIT"].collidepoint(p):
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
        '''
        A função update entities faz todos os processos da fase, verificando as interações entre objetos,
        e atualizando o estado do jogo. É nela que verificamos se o jogador ganhou a fase ou perdeu.
        '''
        for group in self.entities.values():
            for e in group:
                e.update()
        
        if not self.perdeu:
            if self.birds[self.current_bird].crash_wall():
                self.hit_sound.play()
                if self.update_bird_count():
                    self.perdeu = True

        if not self.perdeu:            
            self.birds[self.current_bird].update()

            for goals in self.entities["Goals"]:
                if self.birds[self.current_bird].crash(goals):
                    self.complete_sound.play()
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
                    self.hit_sound.play()

                    self.birds[self.current_bird].reset()
                    if self.update_bird_count():
                        self.perdeu = True
                        break

            if not self.perdeu:
                for meteor in self.entities["Meteors"]:
                    if self.birds[self.current_bird].name == "GunBird":
                        if self.birds[self.current_bird].bullet.crash(meteor):
                            self.birds[self.current_bird].bullet.reset()
                            del self.entities["Meteors"][self.entities["Meteors"].index(meteor)]

                    if self.birds[self.current_bird].crash(meteor):
                        self.hit_sound.play()
                        
                        self.birds[self.current_bird].reset()
                        if self.update_bird_count():
                            self.perdeu = True
                            break

        return self.name

    @abstractmethod
    def draw(self, screen):
        '''
        A função draw desenha todos os elementos na tela e atualiza o display.
        '''
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
            screen.blit(pygame.image.load("assets/GameOver.png"), (200, 125))
            
        # Update!
        pygame.display.update()

    
    def draw_line_dashed(self, surface, color, start_pos, end_pos, width = 1, dash_length = 10, exclude_corners = True):
        '''
        A função draw_line_dashed desenha uma linha pontilhada que auxilia o jogador na hora de atirar o pássaro,
        mostrando o sentido do tiro.
        '''

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