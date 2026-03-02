import pygame

class Scoreboard:
    def __init__(self):
        self.level = 1
        self.font = pygame.font.SysFont("Courier", 28)
        self.player_name = "Krittitee Chaisang"

    def draw(self, screen):
        level_text = self.font.render(f"Level: {self.level}", True, (0, 0, 0))
        name_text = self.font.render(f"Player: {self.player_name}", True, (0, 0, 0))
        screen.blit(level_text, (20, 20))
        screen.blit(name_text, (20, 55))

    def increase_level(self):
        self.level += 1

    def game_over(self, screen):
        text = self.font.render("GAME OVER", True, (0, 0, 0))
        hint = self.font.render("Press SPACE to Restart", True, (0, 0, 0))
        screen.blit(text, (210, 300))
        screen.blit(hint, (160, 340))

    def reset(self):
        self.level = 1
