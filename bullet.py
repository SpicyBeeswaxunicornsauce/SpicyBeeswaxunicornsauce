import pygame
from pygame.sprite import Sprite


# screen gsr-i-c-sr blit
# screen mr-c-gr- draw
class Bullet(Sprite):
    """A class for bullets"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.s = ai_game.s
        self.color = ai_game.s.bullet_color

        # Create a rect from scratch since we don't have an image for it
        self.rect = pygame.Rect(0, 0, ai_game.s.bullet_width, ai_game.s.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # New variable called y which is the float version of the actual y
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up to hit the aliens."""
        # Update the y variable
        self.y -= self.s.bullet_speed
        # self.s.bullet_speed += 0.01
        # Update the actual rect
        self.rect.y = self.y

    def draw_bullet(self):
        """Draws the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
