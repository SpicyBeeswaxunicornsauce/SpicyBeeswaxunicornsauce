import pygame
class Settings:
    """Class to store all the settings and variables for the game."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = pygame.image.load('starfield.png').convert()
        self.bg_img_rect = self.bg_image.get_rect()
        self.caption = 'Alien Invasion'
        # Bullet Settings
        self.bullet_width, self.bullet_height = 5, 20
        self.bullet_color = (182, 182, 182)
        self.bullets_allowed = 3
        # Alien settings
        self.fleet_drop_speed = 20
        self.ship_limit = 2

    def initialize_dynamic_settings(self):
        """Initialize settings that change during the game."""
        self.ship_speed = 1.5
        self.bullet_speed = 1
        self.alien_speed = 0.6

        self.fleet_direction = 1
        # self.fleet_direction is which way the aliens are going.
        # 1 means right; -1 means left.

    def increase_speed(self):
        """Increase speed settings."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
