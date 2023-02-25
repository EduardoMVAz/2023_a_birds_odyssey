import pygame

from screens.additional.main_menu import MainMenu
from screens.additional.credits import Credits
from screens.levels.level1 import Level1
from screens.levels.level2 import Level2
from screens.levels.level3 import Level3
from screens.levels.level4 import Level4
from screens.levels.level5 import Level5

pygame.init()

class Game():
    # Tamanho da tela e definição do FPS
    WIDTH = 800
    HEIGHT = 450

    FPS = 60  # Frames per Second

    def __init__(self):
        
        pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        self.telas = {
            "MainMenu" : MainMenu(),
            "Level1" : Level1(),
            "Level2" : Level2(),
            "Level3" : Level3(),
            "Level4" : Level4(),
            "Level5" : Level5(),
            "Credits": Credits()
        }


    def play(self):

        # Inicializa o Mixer
        pygame.mixer.init()

        # Carrega a Soundtrack
        pygame.mixer.music.load("audios/possible_soundtrack.mp3")

        # Loop da soundtrack
        pygame.mixer.music.set_volume(0.7) # Volume
        pygame.mixer.music.play(loops=-1)

        
        tela = self.telas["MainMenu"]

        rodando = True
        while rodando:
            # Capturar eventos
            strtela = tela.process_events()

            if strtela != "Quit":
                if strtela != tela.name:
                    tela.reset()

                tela = self.telas[strtela]

                # Controlar frame rate
                self.clock.tick(self.FPS)

                tela.draw(self.screen)
            else:
                rodando = False

        # Terminar tela
        quit()
   
   
    def quit():
        pygame.quit()


if __name__ == '__main__':
    game = Game()
    game.play()