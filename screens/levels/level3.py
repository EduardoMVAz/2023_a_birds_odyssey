import pygame

from screens.abstract_level import AbstractLevel

from entities.celestial import CelestialBody
from entities.birds.basic_bird import BasicBird
from entities.birds.redirect_bird import RedirectBird
from entities.goal import Goal

class Level3(AbstractLevel):

    def __init__(self):
        self.birds = [
            BasicBird(50, 400, 0, 0, 8),
            RedirectBird(50, 400, 0, 0, 8),
            BasicBird(50, 400, 0, 0, 8),
            RedirectBird(50, 400, 0, 0, 8)
        ]

        self.entities = {
            "Celestial Bodies" : [
                CelestialBody(x=250, y=300, radius=48, gravity=5000, gravity_radius=150, planet=2),
                CelestialBody(x=550, y=150, radius=48, gravity=5000, gravity_radius=150, planet=3),
            ],
            "Goals" : [
                Goal(750, 50, 20)
            ],
            "Meteors": []
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}
        self.image = pygame.image.load("SpaceBackground1.png")
        self.name = self.LEVEL3
        self.next_level = self.LEVEL4
        self.perdeu = False

        self.current_bird = 0