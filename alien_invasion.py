import pygame
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button


class AlienInvasion:
    """Pretty much the game itself"""

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1200, 800))
        self.s = Settings(self)
        pygame.display.set_caption(self.s.caption)

        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # make a fleet of aliens
        self._create_fleet()

        self.button = Button(self, "Play")

        self.powerful_bullet = True

    def _check_events(self):
        """Watches for events and respond to them."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if not self.stats.game_active:
                    mouse_pos = pygame.mouse.get_pos()
                    self._check_button_clicked(mouse_pos)
                else:
                    self._fire_bullet()

    def _check_button_clicked(self, mouse_pos):
        """Check if the mouse is touching the button."""
        if self.button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_x:
            raise SystemExit
        elif event.key == pygame.K_SPACE:
            if self.stats.game_active:
                self._fire_bullet()
        self._check_testing_stuffs(event)

    def _check_testing_stuffs(self, event):
        if event.key == pygame.K_F1:
            if self.powerful_bullet:
                self.powerful_bullet = False
            else:
                self.powerful_bullet = True
        if event.key == pygame.K_CAPSLOCK:
            self.s.bullet_width = 1150
        if event.key == pygame.K_EQUALS:
            self.s.bullet_width = 5

    def _check_keyup_events(self, event):
        """Respond to keypresses."""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """Make a new bullet and add it the the bullets group"""
        if len(self.bullets) < self.s.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Delete the bullets that take up too much memory and processing power
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check__bullet_alien_collisions()

    def _check__bullet_alien_collisions(self):
        """React to bullet-alien collisions."""
        # Check if the bullets have collided, and if so, delete the bullet and the alien.
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, self.powerful_bullet, True)

        if not self.aliens:
            # Get rid of existing bullets and make a new fleet.
            self.bullets.empty()
            self._create_fleet()

        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

    def _create_fleet(self):
        """Create a fleet of aliens"""
        # Calculate how many aliens will fit in a row.
        # Spacing between each alien is equal to one alien width.
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.s.screen_width - (2 * alien_width)
        number_aliens = available_space_x // (2 * alien_width)

        # Calculate how many rows will fit in the screen.
        ship_height = self.ship.rect.height
        available_space_y = self.s.screen_height - (4 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        # Create the full fleet.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        """Make an alien and add it the the row"""
        alien = Alien(self)  # Make an actual alien
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.y = alien.rect.height + 2 * alien_height * row_number
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.aliens.add(alien)

    def _check_fleet_edges(self):
        """Respond appropriately when the fleet hits the edge"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the fleet down and move it in the other direction."""
        for alien in self.aliens:
            alien.rect.y += self.s.fleet_drop_speed
        self.s.fleet_direction *= -1

    def _update_aliens(self):
        """
        Check if the fleet is at the edge,
        then update the positions of all the aliens.
        """
        self._check_fleet_edges()
        self.aliens.update()

        # Check for aliens reaching the bottom.
        self._check_aliens_bottom()

    def _ship_hit(self):
        """Respond to the ship getting hit by an alien."""
        if self.stats.ships_left > 0:
            # Subtract one from the number of ships left.
            self.stats.ships_left -= 1

            # Destroy all aliens and bullets.
            self.aliens.empty()
            self.bullets.empty()

            # Make a new fleet and center the ship on the screen.
            self._create_fleet()
            self.ship.center_ship()

            # Pause.
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _check_aliens_bottom(self):
        """Check for aliens at the bottom of the screen."""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # React as if the ship got hit.
                self._ship_hit()
                break

    def _update_screen(self):
        """Updates the images on the screen and flips it to the most recent one."""
        # Paints the background color
        self.screen.blit(self.s.bg_image, self.s.bg_img_rect)
        # Draws the ship at it's location
        self.ship.blitme()
        # Moves the bullets
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        if not self.stats.game_active:
            self.button.draw_button()
        # Gets the most up-to-date drawn screen and makes it visible.
        pygame.display.flip()

    def run_game(self):
        """This is the main loop part for the game."""
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_aliens()
                self._update_bullets()
            self._update_screen()


if __name__ == '__main__':
    # Create an instance to represent the game, and run it.
    ai = AlienInvasion()
    ai.run_game()

# com('6-29-2021', "Line 6 to Line 28. Only typed the words. Didn't analyse it yet.")
# com('6-30-2021', 'Analysed the stuffs.')

# class MyPrint:
#     def __int__(self):
#         self.print = print('hello')
#
#
# printy = MyPrint()
# printy.print
pygame.quit()
