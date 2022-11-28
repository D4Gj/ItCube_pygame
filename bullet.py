import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color

        self.image = pygame.image.load('images/bullet.png')
        # self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
        #                        self.settings.bullet_height)
        self.rect = self.image.get_rect()
        self.rect.midtop = game.ship.rect.midtop

        self.y = float(self.rect.y)
        self.x = float(self.rect.x)

    def update(self):
        self.y -= self.settings.bullet_speed
        if self.game.ship.moving_left:
            self.x -= self.settings.bullet_speed
        elif self.game.ship.moving_right:
            self.x += self.settings.bullet_speed

        self.rect.y = self.y
        self.rect.x = self.x

    def draw_bullet(self):
        # pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)
