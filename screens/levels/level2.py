import pygame

from screens.abstract_level import AbstractLevel

from entities.celestial import CelestialBody
from entities.birds.basic_bird import BasicBird
from entities.birds.redirect_bird import RedirectBird
from entities.goal import Goal

class Level2(AbstractLevel):

    def __init__(self):
        self.birds = [
            BasicBird(50, 200, 0, 0, 8),
            RedirectBird(50, 200, 0, 0, 8),
        ]

        self.entities = {
            "Celestial Bodies" : [
                CelestialBody(x=400, y=80, radius=48, gravity=5000, gravity_radius=150, planet=0),
                CelestialBody(x=400, y=320, radius=48, gravity=5000, gravity_radius=150, planet=1),
            ],
            "Goals" : [
                Goal(750, 200, 20)
            ],
            "Meteors": []
        }
        self.colors = {"RED": (255, 0, 0), "GREEN": (0, 255, 0), "BLUE": (0, 0, 255), "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}
        self.image = pygame.image.load("assets/SpaceBackground2.png")
        self.name = self.LEVEL2
        self.next_level = self.LEVEL3
        self.perdeu = False

        self.current_bird = 0

        self.hit_sound = pygame.mixer.Sound("audios/hit_something.wav")
        self.complete_sound = pygame.mixer.Sound("audios/level_complete.wav")