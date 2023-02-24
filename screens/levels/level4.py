import pygame

from screens.abstract_level import AbstractLevel

from entities.celestial import CelestialBody
from entities.meteor import Meteor

from entities.birds.gun_bird import GunBird
from entities.birds.redirect_bird import RedirectBird
from entities.goal import Goal

class Level4(AbstractLevel):

    def __init__(self):
        self.birds = [
            GunBird(50, 380, 0, 0, 8),
            RedirectBird(50, 380, 0, 0, 8),
            RedirectBird(50, 380, 0, 0, 8)
        ]

        self.entities = {
            "Celestial Bodies" : [
                CelestialBody(x=400, y=390, radius=48, gravity=5000, gravity_radius=300, planet=0),
            ],
            "Goals" : [
                Goal(750, 380, 20)
            ],
            "Meteors": [
                Meteor(x=500, y=310, radius=50),
                Meteor(x=590, y=240, radius=50),
                Meteor(x=600, y=390, radius=50),
                Meteor(x=700, y=200, radius=50)
            ]
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}
        self.image = pygame.image.load("SpaceBackground1.png")
        self.name = self.LEVEL4
        self.next_level = self.LEVEL5
        self.perdeu = False

        self.current_bird = 0