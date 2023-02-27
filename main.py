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

    '''
    A classe Game é a principal classe do jogo, e representa o loop principal. Ela funciona baseado em nomes de telas,
    trocando entre as telas do dicionário "telas" e executando de forma genérica as funções de cada tela.
    '''

    # Tamanho da tela e definição do FPS
    WIDTH = 800
    HEIGHT = 450

    FPS = 60  # Frames per Second

    def __init__(self):
        
        pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.screen = pygame.display.get_surface()
        self.clock = pygame.time.Clock()

        # Dicionário com as telas do jogo
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

        # Define a primeira tela
        tela = self.telas["MainMenu"]

        # Inicia O loop principal
        rodando = True
        while rodando:

            '''
            O loop inicia rodando a função process_events de cada tela, que realiza toda checagem da tela. Dentro da fase,
            a função chama update_entites, que determina se a fase acabou ou não.
            Quando uma fase acaba, seja perdendo ou ganhando, a classe da fase retorna ao loop principal o nome da próxima tela,
            e o loop atualiza a variável "tela" selecionando a chave no dicionário utilizando o nome retornado.
            Quando o jogo acaba, o loop principal se encerra e o jogo fecha.
            '''

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