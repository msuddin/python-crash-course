import pygame

class Ship:

    def __init__(self, ai_game):
        # Initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = self.screen.get_rect()

        # Load the ship and get its rect
        self.image = pygame.image.load('chapter_12_alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Start the ship at the bottom of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store the ships x co-ordinate
        self.x = float(self.rect.x)

        # Set flags for moving right and left
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        # Draw the ship in the rect location
        self.screen.blit(self.image, self.rect)

    def update(self):
        # Set x co-ordinate based on movement flags
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # Set the rect x to x
        self.rect.x = self.x
