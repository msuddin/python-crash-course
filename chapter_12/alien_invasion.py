import sys
import pygame

from ship import Ship
from bullet import Bullet
from settings import Settings

class AlienInvasion:

    def __init__(self):
        # Initialize the game and set any resources
        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        # Set display
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        # Set display window title
        pygame.display.set_caption('Alien Invasion')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        while True:
            # Check for events in the pygame instance
            self._check_events()
            self._update_screen()
            self._update_bullets()
            self.ship.update()

    def _check_events(self):
        for event in pygame.event.get():
            # Check if the window has been closed
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        if event.key == pygame.K_SPACE:
            self._fire_bullet()
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        # Check length of bullets to see if it is less than allowed number of bullets
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        # Set background color
        self.screen.fill(self.settings.bg_color)

        # Draw bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Draw the ship
        self.ship.blitme()

        # Make the most recent draw screen
        pygame.display.flip()

        # Set to run 60 frames per while loop pass
        self.clock.tick(60)

    def _update_bullets(self):
        self.bullets.update()

        # Remove bullets from Bullets group that are not on the screen anymore
        for bullet in self.bullets.copy():
            if bullet.rect.bottom < 0:
                self.bullets.remove(bullet)

# Still not sure what this actually does, need to double check
if __name__ == '__main__':
    # Make an instance of the game and run it
    ai = AlienInvasion()
    ai.run_game()