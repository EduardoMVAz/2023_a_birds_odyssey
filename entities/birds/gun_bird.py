import numpy as np
import pygame

from entities.birds.abstract_bird import AbstractBird
from entities.birds.bullet import Bullet


class GunBird(AbstractBird):

    def __init__(self, x, y, vx, vy, radius):
        super().__init__(x, y, vx, vy, radius)

        self.name = self.GUN_BIRD
        self.image = pygame.image.load("gun_bird.png")
        self.bullet = Bullet(self.pos[0], self.pos[1], self.vel[0], self.vel[1], 2)

        self.shoot_sound = pygame.mixer.Sound("audios/shot_bullet.wav")

    def update(self):
        super().update()
        self.bullet.update()

    def draw(self, screen):
        super().draw(screen)
        if self.used_ability and not self.bullet.hit:
            self.bullet.draw(screen)

    def ability(self):
        self.bullet.pos = self.pos
        d = pygame.mouse.get_pos() - self.bullet.pos
        self.bullet.vel = d/80
        self.used_ability = True

        self.shoot_sound.play()