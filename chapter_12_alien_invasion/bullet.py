import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        # Call Sprite class constructor
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet at the rect position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullets Y position as a float
        self.y = float(self.rect.y)

    def update(self):
        # Move the bullet up the screen
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        # Draw the bullet
        pygame.draw.rect(self.screen, self.color, self.rect)