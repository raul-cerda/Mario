import pygame


class Display():
    def __init__(self, screen, stats):
        self.font = pygame.font.SysFont("monospace", 35)
        self.white = (255, 255, 255)

        # SCORE
        self.score = self.font.render("SCORE", True, self.white)
        self.score_rect = self.score.get_rect()
        self.score_rect.centerx = screen.get_rect().centerx - 320
        self.score_rect.centery = screen.get_rect().top + 20

        # CURRENT SCORE
        self.current_score = self.font.render(str(stats.score), True, self.white)
        self.current_score_rect = self.current_score.get_rect()
        self.current_score_rect.centerx = screen.get_rect().centerx - 320
        self.current_score_rect.centery = screen.get_rect().top + 45

        # COINS
        self.coins = self.font.render("COINS", True, self.white)
        self.coins_rect = self.coins.get_rect()
        self.coins_rect.centerx = screen.get_rect().centerx - 160
        self.coins_rect.centery = screen.get_rect().top + 20

        # CURRENT COINS
        self.current_coins = self.font.render(str(stats.coins), True, self.white)
        self.current_coins_rect = self.current_coins.get_rect()
        self.current_coins_rect.centerx = screen.get_rect().centerx - 160
        self.current_coins_rect.centery = screen.get_rect().top + 45

        # WORLD
        self.world = self.font.render("WORLD", True, self.white)
        self.world_rect = self.world.get_rect()
        self.world_rect.centerx = screen.get_rect().centerx + 10
        self.world_rect.centery = screen.get_rect().top + 20

        # CURRENT WORLD
        self.current_world = self.font.render("1-1", True, self.white)
        self.current_world_rect = self.current_world.get_rect()
        self.current_world_rect.centerx = screen.get_rect().centerx + 10
        self.current_world_rect.centery = screen.get_rect().top + 45

        # TIME
        self.time = self.font.render("TIME", True, self.white)
        self.time_rect = self.time.get_rect()
        self.time_rect.centerx = screen.get_rect().centerx + 175
        self.time_rect.centery = screen.get_rect().top + 20

        # CURRENT TIME
        self.current_time = self.font.render(str(stats.time), True, self.white)
        self.current_time_rect = self.current_time.get_rect()
        self.current_time_rect.centerx = screen.get_rect().centerx + 175
        self.current_time_rect.centery = screen.get_rect().top + 45

        # LIVES
        self.lives = self.font.render("LIVES", True, self.white)
        self.lives_rect = self.lives.get_rect()
        self.lives_rect.centerx = screen.get_rect().centerx + 320
        self.lives_rect.centery = screen.get_rect().top + 20

        # CURRENT LIVES
        self.current_lives = self.font.render(str(stats.lives), True, self.white)
        self.current_lives_rect = self.current_lives.get_rect()
        self.current_lives_rect.centerx = screen.get_rect().centerx + 320
        self.current_lives_rect.centery = screen.get_rect().top + 45

    def score_blit(self, screen, stats):
        # Update current score numbers
        self.current_score = self.font.render(str(stats.score), True, self.white)
        self.current_coins = self.font.render(str(stats.coins), True, self.white)
        self.current_time = self.font.render(str(stats.time), True, self.white)
        self.current_lives = self.font.render(str(stats.lives), True, self.white)

        screen.blit(self.score, self.score_rect)
        screen.blit(self.current_score, self.current_score_rect)
        screen.blit(self.coins, self.coins_rect)
        screen.blit(self.current_coins, self.current_coins_rect)
        screen.blit(self.world, self.world_rect)
        screen.blit(self.current_world, self.current_world_rect)
        screen.blit(self.time, self.time_rect)
        screen.blit(self.current_time, self.current_time_rect)
        screen.blit(self.lives, self.lives_rect)
        screen.blit(self.current_lives, self.current_lives_rect)
