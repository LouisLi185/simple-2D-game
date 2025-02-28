import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        """set a bullet at the recent position of the ship"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        #set a rectangle at (0,0)
        self.rect = pygame.Rect(0, 0,
                                self.settings.bullet_width,
                                self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        #display the position of the bullet
        self.y = float(self.rect.y)

    def update(self):
        """move the bullet up"""
        #update the accurate position of the bullet
        self.y -= self.settings.bullet_speed
        #update the position of the rect.
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

