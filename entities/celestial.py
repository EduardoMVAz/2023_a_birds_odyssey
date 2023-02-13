import numpy as np

class CelestialBody:
    def __init__(self, x, y, radius, gravity, gravity_radius):
        self.pos = np.array([x, y])
        self.vel = np.array([0, 0])
        self.acc = np.array([0, 0])
        self.radius = radius
        self.gravity = Gravity(x, y, gravity_radius, gravity)



class Gravity:
    def __init__(self, x, y, radius, gravity):
        self.pos = np.array([x, y])
        self.radius = radius
        self.gravity = gravity