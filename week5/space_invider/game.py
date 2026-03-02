import pygame, sys
from spaceship import Spaceship
from obstacle import Block
from alien import Alien
from laser import Laser,TargetedLaser
import random

class Game:
    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.offset = 50
        self.spaceship_group = pygame.sprite.GroupSingle()
        self.spaceship = Spaceship(self.screen_width, self.screen_height, self.offset)
        self.spaceship_group.add(self.spaceship)
        self.obstacles = self.create_obstacles()
        self.aliens_group = pygame.sprite.Group()
        self.alien_lasers_group = pygame.sprite.Group()
        self.create_aliens()
        self.alien_direction = 1
        self.alien_lasers_cooldown = 1000
        self.last_alien_laser_time = 0
        self.score = 0
        self.lives = 3
        self.run = True
        self.level = 1
        self.font = pygame.font.Font(None, 40)
        self.game_over_surface = self.font.render("GAME OVER", False, (255, 255, 255))
        self.restart_surface = self.font.render("Press SPACE to Restart", False, (255, 255, 255))
        self.explosion_sound = pygame.mixer.Sound(buffer=self._generate_explosion_sound())
        self.explosion_sound.set_volume(0.2)
        
    def _generate_explosion_sound(self):
        sample_rate = 44100
        duration = 0.1
        n_samples = int(sample_rate * duration)
        import random
        buf = bytearray([random.randint(0, 255) for _ in range(n_samples)])
        return buf

    def create_obstacles(self):
        obstacle_width = len(grid[0]) * 3
        gap = (self.screen_width + 2 * self.offset - (4 * obstacle_width)) // 5
        obstacles = pygame.sprite.Group()
        for i in range(4):
            offset_x = (i + 1) * gap + i * obstacle_width
            for row_index, row in enumerate(grid):
                for col_index, col in enumerate(row):
                    if col == 'x':
                        x = 25 + col_index * 3 + offset_x
                        y = self.screen_height - 100 + row_index * 3
                        block = Block(3, (241, 79, 79), x, y)
                        obstacles.add(block)
        return obstacles

    def create_aliens(self):
        for row in range(5):
            for col in range(11):
                x = 75 + col * 55
                y = 100 + row * 55
                
                if row == 0:
                    alien_type = 'yellow'
                elif row in (1,2):
                    alien_type = 'green'
                else:
                    alien_type = 'red'
                
                alien = Alien(alien_type, x + self.offset / 2, y)
                self.aliens_group.add(alien)

    def move_aliens(self):
        self.aliens_group.update(self.alien_direction)
        alien_sprites = self.aliens_group.sprites()
        for alien in alien_sprites:
            if alien.rect.right >= self.screen_width + self.offset / 2:
                self.alien_direction = -1
                self.alien_move_down(2)
            elif alien.rect.left <= self.offset / 2:
                self.alien_direction = 1
                self.alien_move_down(2)

    def alien_move_down(self, distance):
        if self.aliens_group:
            for alien in self.aliens_group.sprites():
                alien.rect.y += distance

    def alien_shoot(self):
        if self.aliens_group:
            current_time = pygame.time.get_ticks()

            if current_time - self.last_alien_laser_time >= self.alien_lasers_cooldown:

                random_alien = random.choice(self.aliens_group.sprites())

                laser_sprite = TargetedLaser(
                    pos=random_alien.rect.midbottom,
                    target_pos=self.spaceship_group.sprite.rect.center,
                    speed=5,
                    screen_height=self.screen_height,
                    color=(255, 0, 0)
                )

                self.alien_lasers_group.add(laser_sprite)
                self.last_alien_laser_time = current_time

    def check_collisions(self):
        if self.spaceship_group.sprite.lasers_group:
            for laser in self.spaceship_group.sprite.lasers_group:
                if pygame.sprite.spritecollide(laser, self.aliens_group, True):
                    self.explosion_sound.play()
                    laser.kill()
                    self.score += 100
                if pygame.sprite.spritecollide(laser, self.obstacles, True):
                    laser.kill()
                if pygame.sprite.spritecollide(laser, self.alien_lasers_group, True):
                    laser.kill()
        
        if not self.aliens_group:
            self.next_level()
        
        if self.alien_lasers_group:
            for laser in self.alien_lasers_group:
                if pygame.sprite.spritecollide(laser, self.spaceship_group, False):
                    self.explosion_sound.play()
                    laser.kill()
                    self.lives -= 1
                    if self.lives <= 0:
                        self.run = False
                if pygame.sprite.spritecollide(laser, self.obstacles, True):
                    laser.kill()

        if self.aliens_group:
            for alien in self.aliens_group:
                pygame.sprite.spritecollide(alien, self.obstacles, True)
                if pygame.sprite.spritecollide(alien, self.spaceship_group, False):
                    self.lives = 0
                    self.run = False

    def display_ui(self, screen):
        score_surface = self.font.render(f'SCORE: {self.score}', False, (255, 255, 255))
        lives_surface = self.font.render(f'LIVES: {self.lives}', False, (255, 255, 255))
        level_surface = self.font.render(f'LEVEL: {self.level}', False, (255, 255, 255))
        
        screen.blit(score_surface, (50, 20))
        screen.blit(lives_surface, (self.screen_width - 150, 20))
        screen.blit(level_surface, (self.screen_width - 350, 20))
        
        pygame.draw.line(screen, (255, 255, 255), (0, self.screen_height - 50), (self.screen_width, self.screen_height - 50), 3)

        if not self.run:
            screen_rect = screen.get_rect()
            
            game_over_rect = self.game_over_surface.get_rect(center = screen_rect.center)
            screen.blit(self.game_over_surface, game_over_rect)

            restart_rect = self.restart_surface.get_rect(center = (screen_rect.centerx, screen_rect.centery + 60))
            screen.blit(self.restart_surface, restart_rect)

    def reset_game(self):
        self.run = True
        self.lives = 3
        self.score = 0
        self.level = 1
        self.alien_lasers_cooldown = 1000
        self.spaceship_group.sprite.reset()
        self.aliens_group.empty()
        self.alien_lasers_group.empty()
        self.create_aliens()
        self.obstacles.empty()
        self.obstacles = self.create_obstacles()

    def update(self):
        if self.run:
            self.spaceship_group.update()
            self.move_aliens()
            self.alien_shoot()
            self.alien_lasers_group.update()
            self.check_collisions()


    def draw(self, screen):
        self.spaceship_group.draw(screen)
        self.spaceship_group.sprite.lasers_group.draw(screen)
        self.aliens_group.draw(screen)
        self.alien_lasers_group.draw(screen)
        self.obstacles.draw(screen)
        self.display_ui(screen)

    def next_level(self):
        self.level += 1
        self.aliens_group.empty()
        self.alien_lasers_group.empty()
        self.create_aliens()
        if self.alien_lasers_cooldown > 200:
            self.alien_lasers_cooldown -= 100
            
    def alien_shoot(self):
        if self.aliens_group:
            current_time = pygame.time.get_ticks()
            if current_time - self.last_alien_laser_time >= self.alien_lasers_cooldown:

                random_alien = random.choice(self.aliens_group.sprites())

                laser_sprite = TargetedLaser(
                    pos=random_alien.rect.midbottom,
                    target_pos=self.spaceship_group.sprite.rect.center,
                    speed=5,
                    screen_height=self.screen_height,
                    color=(255, 0, 0)  # ยิงสีแดง
                )

                self.alien_lasers_group.add(laser_sprite)
                self.last_alien_laser_time = current_time




grid = [
    '  xxxxxxx',
    ' xxxxxxxxx',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxxxxxxxxxx',
    'xxx     xxx',
    'xx       xx']
