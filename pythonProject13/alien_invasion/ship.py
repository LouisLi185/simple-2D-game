import pygame

class Ship:
    def __init__(self, ai_game):
        """initialise the ship"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #get the image of ship and the rectangle outside
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        #put the ship at the middle of the screen
        self.rect.midbottom  = self.screen_rect.midbottom

        #store a float in the x
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        #the ship doesn't move at first
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.fire = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        #update the aim of the rect. based on the self.x
        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        self.screen.blit(self.image, self.rect)