class Settings():
    def __init__(self):
        self.screen_height = 540
        self.screen_width = 960
        self.background = (255, 255, 255)

        # Bullet settings
        self.bullet_speed_factor = 6
        self.bullet_width = 3
        self.bullet_height = 30
        self.bullet_color = 60, 60, 60
        self.bullet_limit = 8

        # alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 7

        # fleet direction: 1 = right, -1 = left
        self.fleet_direction = 1

        self.ship_limit = 3

        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()        

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 3

        self.fleet_direction = 1 # right; left = -1
        self.alien_points = int(50)

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points *= self.score_scale
