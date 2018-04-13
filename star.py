import pygame
WHITE = (255,255,255)
class Star(pygame.sprite.Sprite):

    def __init__(self, color, width, height):

        super().__init__()

        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        pygame.draw.ellipse(self.image,color,[20,20,200,200])

        self.rect = self.image.get_rect()

        
