from abc import abstractmethod

import pygame
import numpy as np

## Assim como as fases, os pássaros são todos classes que herdam de uma classe genérica, AbstractBird.

class AbstractBird():

    WIDTH = 800
    HEIGHT = 450

    BASIC_BIRD = "BasicBird"
    REDIRECT_BIRD = "RedirectBird"
    GUN_BIRD = "GunBird"

    def __init__(self, x, y, vx, vy, radius):
        '''
        O init genérico contém todas as informações genéricas aos três pássaros:
        '''
        self.s0 = np.array([x, y])
        self.pos = np.array([x, y])
        self.vel = np.array([vx, vy])
        self.acc = np.array([0, 0])
        self.radius = radius

        self.used_ability = False
        self.has_shot = False

        self.shoot_sound = pygame.mixer.Sound("audios/shot_bird.wav")

    def update(self):
        '''
        Update genérico atualiza os atributos de posição do pássaro
        '''
        self.vel = self.vel + self.acc * 0.1
        self.pos = self.pos + self.vel
        self.acc = np.array([0, 0])
    
    def crash(self, o):
        '''
        A função crash faz a checagem de contato entre objetos, para verificar se o pássaro atingiu algo.
        '''
        d = np.sqrt((self.pos[0] - o.pos[0])**2 + (self.pos[1] - o.pos[1])**2)
        if d < self.radius + o.radius:
            return True
        return False

    def crash_wall(self):
        '''
        A função crash wall verifica se o pássaro saiu da tela.
        '''
        if self.pos[0]<self.radius or self.pos[0]>self.WIDTH - self.radius or self.pos[1]<self.radius or self.pos[1]>self.HEIGHT - self.radius: # Se eu chegar ao limite da tela, reinicio a posição do personagem
            self.reset()
            return True
        return False

    def reset(self):
        '''
        A função reset serve para devolver o pássaro ao seu estado inicial.
        '''
        self.pos = self.s0
        self.vel = np.array([0, 0])
        self.acc = np.array([0, 0])

        self.has_shot = False
        self.used_ability = False
        
    
    def draw(self, screen):
        '''
        A função draw desenha o pássaro na tela.
        '''
        screen.blit(self.image, (self.pos[0] - self.radius, self.pos[1] - self.radius))
    
    def shoot(self):
        '''
        A função shoot faz o disparo do pássaro.
        '''
        d = pygame.mouse.get_pos() - self.pos
        self.vel = d/120

        self.has_shot = True

        self.shoot_sound.play()

    @abstractmethod
    def ability(self):
        '''
        A função ability é única de cada pássaro, portanto não tem conteúdo na classe pai.
        '''
        pass