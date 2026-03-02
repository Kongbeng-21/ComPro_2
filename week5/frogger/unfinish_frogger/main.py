import pygame
import time
import os
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

BASE_DIR = os.path.dirname(__file__)

pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Frogger GenAI Edition")
clock = pygame.time.Clock()

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

start_pad_img = pygame.image.load(os.path.join(BASE_DIR, "start_pad.png")).convert_alpha()
start_pad_img = pygame.transform.scale(start_pad_img, (100, 100))
start_pad_rect = start_pad_img.get_rect(center=player.rect.center)

game_is_on = True

while True:
    time.sleep(0.08)

    if scoreboard.level % 2 == 1:
        bg_name = "background_odd_level.png"
    else:
        bg_name = "background_even_level.png"

    background_img = pygame.image.load(os.path.join(BASE_DIR, bg_name)).convert()
    background_img = pygame.transform.scale(background_img, (600, 600))
    screen.blit(background_img, (0, 0))
    screen.blit(start_pad_img, start_pad_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and game_is_on:
            if event.key == pygame.K_UP:
                player.move_up()
            elif event.key == pygame.K_DOWN:
                player.move_down()
            elif event.key == pygame.K_LEFT:
                player.move_left()
            elif event.key == pygame.K_RIGHT:
                player.move_right()
        if event.type == pygame.KEYDOWN and not game_is_on:
            if event.key == pygame.K_SPACE:
                game_is_on = True
                player.go_to_start()
                car_manager.reset()
                scoreboard.reset()

    if game_is_on:
        car_manager.create_car()
        car_manager.move_cars()

        for car in car_manager.all_cars:
            if pygame.sprite.collide_mask(player, car):
                game_is_on = False

        if player.is_at_finish_line():
            player.go_to_start()
            car_manager.level_up()
            scoreboard.increase_level()

    sprites = car_manager.all_cars + [player]
    sprites.sort(key=lambda s: s.rect.bottom)
    for s in sprites:
        screen.blit(s.image, s.rect)

    scoreboard.draw(screen)

    if not game_is_on:
        scoreboard.game_over(screen)

    pygame.display.flip()
    clock.tick(60)
