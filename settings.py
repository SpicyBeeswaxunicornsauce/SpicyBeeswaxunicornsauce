import pygame
class Settings:
    """Class to store all the settings and variables for the game."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_image = pygame.image.load('images/starfield.png').convert()
        self.bg_img_rect = self.bg_image.get_rect()
        self.caption = 'Alien Invasion'
        self.right_ship_speed = 1
        # self.left_ship_speed = self.right_ship_speed + ((self.right_ship_speed - 1) - .4)
        self.left_ship_speed = 1
        # Bullet Settings
        self.bullet_speed = 1
        self.bullet_width, self.bullet_height = 5, 20
        self.bullet_color = (182, 182, 182)
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed = 0.6
        self.fleet_drop_speed = 20
        self.fleet_direction = 1
        # self.fleet_direction is which way the aliens are going.
        # 1 means right; -1 means left.
        self.ship_limit = 2
