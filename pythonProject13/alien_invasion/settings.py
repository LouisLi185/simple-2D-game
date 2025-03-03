class Settings:
    """store all the game settings"""
    def __init__(self):
        """initialize the ship settings"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5

        """bullet settings"""
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)

