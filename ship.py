import pygame


class Ship:
    """The class for the spaceship"""
# ScreenGetRectImgColorkeySetrectBlit
# Screen GRICS r blit
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        """Initialize the ship and set its starting position"""
        self.screen_rect = ai_game.screen.get_rect()
        self.s = ai_game.s

        # Load the ship image
        self.image = pygame.image.load('images/shipy.bmp').convert()
        self.image.set_colorkey((96, 96, 0))
        self.rect = self.image.get_rect()

        # Place the ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # hOI! tem stor decimal valu in variabl and make u PROUDS!
        self.x = float(self.rect.x)

        # Is it moving right?
        self.moving_right = False
        # Or perhaps it might be moving left?
        self.moving_left = False

    def update(self):
        if self.moving_right:
            # Add tu da x of da ship, movig it tu da right, only if it not at da edge
            if self.moving_right and self.rect.right < self.screen_rect.right:
                self.x += self.s.right_ship_speed
        elif self.moving_left:
            # Minus tu da x of da ship, movig it tu da left, only if it not at da edge
            if self.moving_left and self.rect.left > 0:
                self.x -= self.s.left_ship_speed

        # Update da rectangl
        self.rect.x = self.x

    def blitme(self):
        """Draws the ship at it's location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = self.rect.x
