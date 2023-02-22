from screens.abstract_level import AbstractLevel

from entities.celestial import CelestialBody
from entities.birds.basic_bird import BasicBird
from entities.birds.redirect_bird import RedirectBird
from entities.birds.gun_bird import GunBird
from entities.goal import Goal

class Level1(AbstractLevel):

    def __init__(self):
        self.birds = [
            BasicBird(50, 200, 0, 0, 7.5),
            RedirectBird(50, 200, 0, 0, 7.5),
            GunBird(50, 200, 0, 0, 7.5)
        ]

        self.entities = {
            "Celestial Bodies" : [
                CelestialBody(x=600, y=200, radius=48, gravity=2500, gravity_radius=100, planet=0)
            ],
            "Goals" : [
                Goal(750, 200, 20)
            ]
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}

        self.name = self.LEVEL1
        self.next_level = self.LEVEL2

        self.current_bird = 0