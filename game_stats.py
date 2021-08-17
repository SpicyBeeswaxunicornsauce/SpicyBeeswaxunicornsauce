class GameStats:
    """Tracks statistics for the game."""

    def __init__(self, alien_invasion):
        """Initialize all the statistics."""
        self.s = alien_invasion.s
        self.game_active = False
        self.reset_stats()

    def reset_stats(self):
        """Initialize all the stats that change during the game."""
        self.ships_left = self.s.ship_limit
