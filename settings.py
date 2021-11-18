class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.ship_limit = 3
        # параметры пули
        self.bullet_speed = 1
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = (255, 15, 15)
        self.bullets_allowed = 100
        # Параметры пришельцев
        self.alien_speed = 1
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.fleet_direction = 1
        # Темп ускорения игры
        self.speedup_scale = 2
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Изменение настроек динамическое"""
        self.bullet_speed = 1.5
        self.ship_speed = 3.0
        self.alien_speed = 1.0

        self.alien_points = 50
        # fleet_direction = 1 обозначает движение вправо, а -1 - влево
        self.fleet_direction = 1

    def increase_speed(self):
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
