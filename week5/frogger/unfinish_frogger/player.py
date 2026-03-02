import pygame
import os

BASE_DIR = os.path.dirname(__file__)

STARTING_POSITION = (300, 560)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 40

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load(os.path.join(BASE_DIR, "frog.png")).convert_alpha()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect(center=STARTING_POSITION)
        self.mask = pygame.mask.from_surface(self.image)

    def move_up(self):
        self.rect.y -= MOVE_DISTANCE

    def move_down(self):
        if self.rect.y < STARTING_POSITION[1]:
            self.rect.y += MOVE_DISTANCE

    def move_left(self):
        if self.rect.x > 0:
            self.rect.x -= MOVE_DISTANCE

    def move_right(self):
        if self.rect.x < 550:
            self.rect.x += MOVE_DISTANCE

    def go_to_start(self):
        self.rect.center = STARTING_POSITION

    def is_at_finish_line(self):
        return self.rect.y < FINISH_LINE_Y
