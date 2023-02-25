import pygame

from screens.abstract_level import AbstractLevel

from entities.celestial import CelestialBody
from entities.meteor import Meteor
from entities.birds.gun_bird import GunBird
from entities.goal import Goal

class Level5(AbstractLevel):

    def __init__(self):
        self.birds = [
            GunBird(50, 200, 0, 0, 8),
            GunBird(50, 200, 0, 0, 8)
        ]

        self.entities = {
            "Celestial Bodies" : [
                CelestialBody(x=600, y=200, radius=48, gravity=9000, gravity_radius=200, planet=0)
            ],
            "Goals" : [
                Goal(750, 200, 20)
            ],
            "Meteors": [
                Meteor(x=300, y=25, radius=50),
                Meteor(x=300, y=125, radius=50),
                Meteor(x=300, y=225, radius=50),
                Meteor(x=300, y=325, radius=50),
                Meteor(x=300, y=425, radius=50),
                Meteor(x=600, y=80, radius=50),
                Meteor(x=600, y=320, radius=50)
            ]
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}
        self.image = pygame.image.load("assets/SpaceBackground1.png")
        self.name = self.LEVEL5
        self.next_level = self.CREDITS
        self.perdeu = False
        self.current_bird = 0

        self.hit_sound = pygame.mixer.Sound("audios/hit_something.wav")
        self.complete_sound = pygame.mixer.Sound("audios/level_complete.wav")