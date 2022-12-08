import pygame


class Ship:
    """Класс для управления кораблём"""

    def __init__(self, screen, settings):
        """Инициализация корабля"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.image = pygame.image.load('resources/spaceship.jpg')
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.x = float(self.rect.x)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def blitme(self):
        """Рисует в текущей позиции"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
