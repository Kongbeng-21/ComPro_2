import pygame
import sys
from game import Game

pygame.init()
pygame.mixer.init()

SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700
OFFSET = 50

GREY = (29, 29, 27)

screen = pygame.display.set_mode((SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET))
pygame.display.set_caption("Space Invaders OOP")

clock = pygame.time.Clock()
game = Game(SCREEN_WIDTH + OFFSET, SCREEN_HEIGHT + 2 * OFFSET)

font = pygame.font.Font(None, 30)
name_text = font.render("Player: Krittitee Chaisang", True, (255,255,255))

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 🔥 ยิงกระสุน player
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if game.run:
                    game.spaceship.shoot()
                else:
                    game.reset_game()

    screen.fill(GREY)

    screen.blit(name_text, (10, 50))

    game.update()
    game.draw(screen)

    pygame.draw.line(screen, (255, 255, 255), (0, 750), (800, 750), 2)
    pygame.display.flip()
    clock.tick(60)
