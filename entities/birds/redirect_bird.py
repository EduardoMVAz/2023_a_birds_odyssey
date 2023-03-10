import numpy as np
import pygame

from entities.birds.abstract_bird import AbstractBird


class RedirectBird(AbstractBird):

    def __init__(self, x, y, vx, vy, radius):
        super().__init__(x, y, vx, vy, radius)

        self.name = self.REDIRECT_BIRD
        self.image = pygame.image.load("assets/redirect_bird.png")
        self.ability_sound = pygame.mixer.Sound("audios/redirect_bird_ability.wav")
    
    def ability(self):
        '''
        A habilidade do pássaro redirecionado é realizar um segundo disparo, alterando seu sentido completamente.
        '''
        d = pygame.mouse.get_pos() - self.pos
        self.vel = d/np.linalg.norm(d) * 2.4
        self.used_ability = True

        self.ability_sound.play()