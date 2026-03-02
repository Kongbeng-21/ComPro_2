import pygame
from laser import Laser

class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, offset):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = offset
        self.image = pygame.Surface((60, 20), pygame.SRCALPHA)
        pygame.draw.rect(self.image, (0, 255, 0), (0, 10, 60, 10)) 
        pygame.draw.rect(self.image, (0, 255, 0), (28, 0, 4, 10))  
        
        self.rect = self.image.get_rect(midbottom = (self.screen_width // 2, self.screen_height - 10 - offset))
        self.speed = 6
        self.lasers_group = pygame.sprite.Group()
        self.laser_ready = True
        self.laser_time = 0
        self.laser_delay = 300
        
        self.laser_sound = pygame.mixer.Sound(buffer=self._generate_laser_sound())
        self.laser_sound.set_volume(0.1)

    def _generate_laser_sound(self):
        sample_rate = 44100
        duration = 0.1
        n_samples = int(sample_rate * duration)
        buf = bytearray([int(127 * (i % 50) / 50) for i in range(n_samples)])
        return buf

    def get_user_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed

        if keys[pygame.K_SPACE] and self.laser_ready:
            self.laser_ready = False
            self.laser_time = pygame.time.get_ticks()
            self.shoot()

    def update(self):
        self.get_user_input()
        self.constrain_movement()
        self.lasers_group.update()
        self.recharge_laser()

    def constrain_movement(self):
        if self.rect.right > self.screen_width - self.offset:
             self.rect.right = self.screen_width - self.offset
        if self.rect.left < self.offset:
            self.rect.left = self.offset

    def recharge_laser(self):
        if not self.laser_ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.laser_time >= self.laser_delay:
                self.laser_ready = True

    def fire_laser(self):
        self.laser_sound.play()
        laser = Laser(self.rect.center, -8, self.screen_height)
        self.lasers_group.add(laser)

    def reset(self):
        self.rect.midbottom = (self.screen_width // 2, self.screen_height - 10)
        self.lasers_group.empty()
        
    def shoot(self):
        center = self.rect.midtop

        # ยิงตรง
        laser_center = Laser(center, 90)

        # ยิงเฉียงซ้าย
        laser_left = Laser(center, 110)

        # ยิงเฉียงขวา
        laser_right = Laser(center, 70)

        self.lasers_group.add(laser_center, laser_left, laser_right)


