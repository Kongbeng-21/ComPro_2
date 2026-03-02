import pygame
import math

class Laser(pygame.sprite.Sprite):
    def __init__(self, pos, angle, speed=8):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill("white")
        self.rect = self.image.get_rect(center=pos)

        rad = math.radians(angle)
        self.dx = speed * math.cos(rad)
        self.dy = -speed * math.sin(rad)

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        if self.rect.bottom < 0 or self.rect.top > 900:
            self.kill()
            
class TargetedLaser(pygame.sprite.Sprite):
    def __init__(self, pos, target_pos, speed, screen_height, color=(255, 0, 0)):
        super().__init__()
        self.image = pygame.Surface((4, 20))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=pos)

        self.screen_height = screen_height

        # 🔥 คำนวณ vector ยิงเข้าหา player
        dx = target_pos[0] - pos[0]
        dy = target_pos[1] - pos[1]

        distance = math.sqrt(dx**2 + dy**2)

        if distance != 0:
            self.dx = (dx / distance) * speed
            self.dy = (dy / distance) * speed
        else:
            self.dx = 0
            self.dy = speed

    def update(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # ลบเมื่อออกจอ
        if (
            self.rect.top > self.screen_height + 50 or
            self.rect.bottom < -50 or
            self.rect.left < -50 or
            self.rect.right > 850
        ):
            self.kill()

