import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen

        #load the image of the aliens
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width/3
        self.rect.y = self.rect.height/6

        #restore the accurate horizontal position of the alien
        self.x = float(self.rect.x)