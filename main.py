import pygame
import numpy as np

from screens.main_menu import MainMenu
from screens.level1 import Level1

pygame.init()

class Game():
    # Tamanho da tela e definição do FPS
    WIDTH = 800
    HEIGHT = 450

    FPS = 60  # Frames per Second

    def __init__(self):
        
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pygame.time.Clock()


    def play(self):
        
        tela = Level1()

        rodando = True
        while rodando:
            # Capturar eventos
            tela = tela.process_events()

            # Controlar frame rate
            self.clock.tick(self.FPS)

            tela.draw(self.screen)

        # Terminar tela
        quit()
    

    def quit():
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.play()