import pygame

class Credits:

    def __init__(self):
        
        self.entities = {
            "BACK": pygame.Rect(19, 368, 135, 60)
        }
        self.image = pygame.image.load("assets/Ending.png")
        self.name = "Credits"

    def reset(self):
        self.__init__()

    def draw(self, screen):

        screen.fill((0,0,0))
        screen.blit(self.image, (0,0))

        pygame.display.update()

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "Quit"
            if event.type == pygame.MOUSEBUTTONDOWN:
                return self.update_entities()
        return self.name

    def update_entities(self):
        p = pygame.mouse.get_pos()
        if self.entities["BACK"].collidepoint(p):
            return "MainMenu"
        return self.name