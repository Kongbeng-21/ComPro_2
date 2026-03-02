from snake_config import Config
import pygame as pg
import random
import time

class Board:
    def __init__(self):
        self.__width = Config.get('BS') * Config.get('COLS')
        self.__height = Config.get('BS') * Config.get('ROWS')
        self.__left = (Config.get('PS_W') - self.__width) // 2
        self.__top = (Config.get('PS_H') - self.__height) // 2

    @property
    def bpos(self):
        return (self.__left, self.__top)

    def draw(self, screen):
        bs = 2
        borderBK = pg.Rect(self.__left-bs, self.__top-bs,
                            self.__width+(bs*2), self.__height+(bs*2))
        borderWH = pg.Rect(self.__left, self.__top,
                            self.__width, self.__height)
        pg.draw.rect(screen, Config.get_color('BK'), borderBK)
        pg.draw.rect(screen, Config.get_color('WH'), borderWH)

# ---------- Food ----------
class Food:
    def __init__(self):
        self.__pos = None

    @property
    def pos(self):
        return self.__pos

    def randomstart(self, forbidden):
        while True:
            x = random.randint(0, Config.get('COLS')-1)
            y = random.randint(0, Config.get('ROWS')-1)
            if (x, y) not in forbidden:
                self.__pos = (x, y)
                break

    def draw(self, screen, board):
        sx = board.bpos[0] + self.__pos[0] * Config.get('BS')
        sy = board.bpos[1] + self.__pos[1] * Config.get('BS')
        reg = pg.Rect(sx+1, sy+1,
                      Config.get('BS')-2, Config.get('BS')-2)
        pg.draw.rect(screen, Config.get_color('R'), reg)

class Snake:
    def __init__(self):
        self.__body = None
        self.__direction = (0, 0)
        self.__die = False
        self.randomstart()
        self.__scoretext = "Score: 0"

    @property
    def die(self):
        return self.__die

    @property
    def score_text(self):
        return self.__scoretext

    @property
    def body(self):
        return self.__body

    def randomstart(self):
        x = random.randint(0, Config.get('COLS')-1)
        y = random.randint(0, Config.get('ROWS')-1)
        self.__body = [(x, y)]

    def set_direction(self, d):
        vector = {'U': (0,-1), 'D': (0,1), 'L': (-1,0), 'R': (1,0)}
        self.__direction = vector[d]

    def move(self):
        if self.__die:
            return

        head = self.__body[0]
        new_head = (head[0] + self.__direction[0],
                    head[1] + self.__direction[1])

        if (new_head[0] < 0 or new_head[1] < 0 or
            new_head[0] >= Config.get('COLS') or
            new_head[1] >= Config.get('ROWS')):
            self.__die = True
            return

        self.__body.insert(0, new_head)
        self.__body.pop()

    def hit_self(self):
        head = self.__body[0]
        if head in self.__body[1:]:
            self.__die = True

    def hit_foods(self, foods):
        for food in foods:
            if self.__body[0] == food.pos:
                self.__body.append(self.__body[-1])
                food.randomstart(self.__body)
                self.__scoretext = f"Score: {len(self.__body)-1}"

    def draw(self, screen, board):
        for b in self.__body:
            sx = board.bpos[0] + b[0] * Config.get('BS')
            sy = board.bpos[1] + b[1] * Config.get('BS')
            reg = pg.Rect(sx+1, sy+1,
                          Config.get('BS')-2, Config.get('BS')-2)
            pg.draw.rect(screen, Config.get_color('BK'), reg)

class Game:
    def __init__(self):
        pg.init()
        self.__screen = pg.display.set_mode(Config.get_window_size())
        pg.display.set_caption("Snake Week 5")
        self.__clock = pg.time.Clock()

        self.__board = Board()
        self.__snake = Snake()

        self.__foods = [Food() for _ in range(5)]
        for f in self.__foods:
            f.randomstart(self.__snake.body)

        self.__keys = {pg.K_UP:'U', pg.K_DOWN:'D',
                       pg.K_LEFT:'L', pg.K_RIGHT:'R'}

        self.__font = pg.font.Font(None, 40)
        self.__font_big = pg.font.Font(None, 64)
        self.__game_over = False

        self.__player_name = "Krittitee Chaisang 6810545441"

    def drawUI(self):
        score = self.__font.render(self.__snake.score_text, True,
                                   Config.get_color('BK'))
        name = self.__font.render(f"Player: {self.__player_name}", True,
                                  Config.get_color('BK'))

        self.__screen.blit(score, (30, 30))
        self.__screen.blit(name, (30, 70))

        if self.__game_over:
            over = self.__font_big.render("Game Over! Press SPACE BAR to restart!", True,
                                          Config.get_color('BK'))
            rect = over.get_rect(center=(Config.get('PS_W')//2,
                                          Config.get('PS_H')//2))
            self.__screen.blit(over, rect)

    def gameloop(self):
        last_move = time.time()

        while True:
            for ev in pg.event.get():
                if ev.type == pg.QUIT:
                    pg.quit()
                    return
                elif ev.type == pg.KEYDOWN:
                    if ev.key in self.__keys:
                        self.__snake.set_direction(self.__keys[ev.key])
                    elif self.__game_over and ev.key == pg.K_SPACE:
                        self.__init__()

            if time.time() - last_move > 0.2 and not self.__game_over:
                last_move = time.time()
                self.__snake.move()
                self.__snake.hit_self()
                self.__snake.hit_foods(self.__foods)
                if self.__snake.die:
                    self.__game_over = True

            self.__screen.fill(Config.get_color('WH'))
            self.__board.draw(self.__screen)
            self.__snake.draw(self.__screen, self.__board)
            for f in self.__foods:
                f.draw(self.__screen, self.__board)
            self.drawUI()

            pg.display.update()
            self.__clock.tick(60)

if __name__ == '__main__':
    Game().gameloop()
