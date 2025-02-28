import sys
import pygame
from settings import  Settings
from ship import Ship
from bullet import Bullet
from alien import Alien


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        #screen settings
        self.screen = pygame.display.set_mode(
            (0,0),pygame.FULLSCREEN )
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')

        #import ship class
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()



        #set background colour
        self.bg_color = (230, 230, 230)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(60)

    def _check_events(self):
        for event in pygame.event.get():
            if (event.type == pygame.K_ESCAPE or
                    event.type == pygame.QUIT):
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self,event):
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif (event.key == pygame.K_ESCAPE or
              event.type == pygame.QUIT):
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self,event):
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False

    def _fire_bullet(self):
        """make a bullet and add it to the bullets group"""
        new_bullet = Bullet(self)
        self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()

        # delete the missed bullets
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _create_fleet(self):
        """create a team of aliens"""
        #create an alien
        alien = Alien(self)
        alien_width = alien.rect.width/3

        current_x = alien_width/3
        while current_x < (self.settings.screen_width - 2*alien_width):
            self._create_alien(current_x)
            current_x += 2*alien_width

    def _create_alien(self,x_position):
        """create an alien and put it into current line"""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        self.aliens.add(new_alien)

    def _update_screen(self):
         self.screen.fill(self.settings.bg_color)
         for bullet in self.bullets.sprites():
             bullet.draw_bullet()
         self.ship.blitme()
         self.aliens.draw(self.screen)

         pygame.display.flip()


if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
