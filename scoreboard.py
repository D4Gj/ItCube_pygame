import pygame.font


class Scoreboard():

    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.stats = game.stats

        # Шрифт
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()

    def prep_score(self):
        """текущий счёт"""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)  # 1000000 1,000,000
        self.score_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def show_score(self):
        """Вывод счёта на экрон"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.hightscore_image, self.high_score_rect)

    def prep_high_score(self):
        high_score = round(self.stats.high_score, -1)
        score_str = "{:,}".format(high_score)  # 1000000 1,000,000
        self.hightscore_image = self.font.render(score_str, True, self.text_color, self.settings.bg_color)

        self.high_score_rect = self.hightscore_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
