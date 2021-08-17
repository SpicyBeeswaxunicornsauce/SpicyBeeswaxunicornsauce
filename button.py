import pygame.font


class Button:
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the button's properties and dimensions.
        self.width, self.height = 150, 75
        self.button_color = (17, 166, 255)
        self.text_color = (225, 225, 225)
        self.font = pygame.font.SysFont('microsoftyaheimicrosoftyaheiuilight', 38)

        # Make the rect object and center the button.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The message only needs to be prepared one time.
        self._prep_message(msg)

    def _prep_message(self, message):
        """Turn the message into a rendered image and center the text on the button"""
        self.text_image = self.font.render(message, True, self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.screen_rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
