import pygame

from screens.abstract_level import AbstractLevel

from entities.celestial import CelestialBody
from entities.birds.basic_bird import BasicBird
from entities.birds.redirect_bird import RedirectBird
from entities.birds.gun_bird import GunBird
from entities.goal import Goal

class Level1(AbstractLevel):

    def __init__(self):
        self.birds = [
            BasicBird(50, 200, 0, 0, 8),
            BasicBird(50, 200, 0, 0, 8),
            BasicBird(50, 200, 0, 0, 8)
        ]

        self.entities = {
            "Celestial Bodies" : [
                CelestialBody(x=600, y=200, radius=48, gravity=9000, gravity_radius=200, planet=0)
            ],
            "Goals" : [
                Goal(750, 200, 20)
            ],
            "Meteors": []
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}
        self.image = pygame.image.load("SpaceBackground1.png")
        self.name = self.LEVEL1
        self.next_level = self.LEVEL2
        self.perdeu = False

        self.current_bird = 0

        self.hit_sound = pygame.mixer.Sound("audios/hit_something.wav")
        self.complete_sound = pygame.mixer.Sound("audios/level_complete.wav")