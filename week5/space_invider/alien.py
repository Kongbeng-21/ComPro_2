import pygame
import math
from laser import Laser

class Alien(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill(color)
        
        if color == 'red':
            self.create_alien_graphic((255, 100, 100))
            self.score_value = 100
        elif color == 'green':
            self.create_alien_graphic((100, 255, 100))
            self.score_value = 200
        else:
            self.create_alien_graphic((255, 255, 100))
            self.score_value = 300

        self.rect = self.image.get_rect(topleft = (x, y))

    def create_alien_graphic(self, color):
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, (5, 10, 30, 20))
        pygame.draw.rect(self.image, color, (0, 15, 5, 5))
        pygame.draw.rect(self.image, color, (35, 15, 5, 5))
        pygame.draw.rect(self.image, color, (5, 30, 5, 5))
        pygame.draw.rect(self.image, color, (30, 30, 5, 5))
        pygame.draw.rect(self.image, (0, 0, 0), (10, 15, 5, 5))
        pygame.draw.rect(self.image, (0, 0, 0), (25, 15, 5, 5))

    def update(self, direction):
        self.rect.x += direction
        
    def shoot(self, player_pos):
        dx = player_pos[0] - self.rect.centerx
        dy = self.rect.centery - player_pos[1]

        angle = math.degrees(math.atan2(dy, dx))
        laser = Laser(self.rect.midbottom, angle)
        return laser

