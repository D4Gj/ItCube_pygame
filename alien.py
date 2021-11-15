import pygame
import settings
from pygame.sprite import Sprite

class Alien(Sprite):
    """Пришелец"""

    def __init__(self,game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        #Загрузка картинки и назначение
        self.image = pygame.image.load("resources/good_alien.bmp")
        self.rect = self.image.get_rect()

        #Появление левый верхний угол
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Сохранение точной горизонтальной позиции
        self.x = float(self.rect.x)

    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True