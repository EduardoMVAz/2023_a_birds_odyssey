from abc import abstractmethod

class AbstractLevel():

    WIDTH = 800
    HEIGHT = 450

    @abstractmethod
    def process_events(self):
        pass

    @abstractmethod
    def update_entities(self):
        pass

    @abstractmethod
    def draw(self, screen):
        pass