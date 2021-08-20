import pygame
from pygame.sprite import Sprite


# Screen Gsrics rect blit
# or
# Screen Mrcgr draw

class Alien(Sprite):
    """This class represents a single alien and it's properties."""
    def __init__(self, ai_game):
        super().__init__()
        self.s = ai_game.s
        self.screen = ai_game.screen

        # Get the alien rect and image
        self.image = pygame.image.load('alien.png').convert()
        self.rect = self.image.get_rect()
        self.image.set_colorkey((0, 0, 0))

        # Place the alien at the top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # make a variable thing called self.x
        self.x = float(self.rect.x)

    def check_edges(self):
        """Checks if the alien is at the edge, returns True if so."""
        screen_rect = self.screen.get_rect()

        if self.rect.right == screen_rect.right or self.rect.left == 0:
            return True

    def update(self):
        """Move the alien left or right."""
        self.x += (self.s.alien_speed * self.s.fleet_direction)
        self.rect.x = self.x
