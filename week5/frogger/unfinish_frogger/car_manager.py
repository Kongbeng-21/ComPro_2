import pygame
import random
import os

BASE_DIR = os.path.dirname(__file__)

CAR_IMAGES = ["car_red.png", "car_blue.png", "car_yellow.png", "car_orange.png"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 5
CAR_WIDTH = 60
CAR_HEIGHT = 60

LANES_SIX = [125, 195, 265, 355, 415, 485]
directions_SIX = [1, 1, 1, -1, -1, -1]

LANES_FOUR = [165, 245, 365, 435]
directions_FOUR = [1, 1, -1, -1]


class CarManager:
    def __init__(self):
        self.level = 1
        self.all_cars = []
        self.lanes_set = {
            0: [LANES_SIX, directions_SIX],
            1: [LANES_FOUR, directions_FOUR]
        }
        self.car_speed = STARTING_MOVE_DISTANCE

        # 🔥 Spawn control
        self.last_spawn_time = 0
        self.spawn_cooldown = 800  # milliseconds

        self.reset()

    def assign_lane_directions(self):
        directions = self.lanes_set[self.level % 2][1][:]
        random.shuffle(directions)

        lanes = self.lanes_set[self.level % 2][0]
        self.lane_directions = {
            lane: directions[i]
            for i, lane in enumerate(lanes)
        }

    def create_car(self):

        current_time = pygame.time.get_ticks()
        if current_time - self.last_spawn_time < self.spawn_cooldown:
            return

        random_chance = random.randint(1, len(self.lanes_set[self.level % 2][0]))
        if random_chance != 1:
            return

        random_y = random.choice(self.lanes_set[self.level % 2][0])
        direction = self.lane_directions[random_y]
        spawn_x = 650 if direction == 1 else -50

        # 🔥 กันรถซ้อนในเลนเดียวกัน
        for car in self.all_cars:
            if abs(car.rect.centery - random_y) < 10:
                if abs(car.rect.centerx - spawn_x) < CAR_WIDTH * 3:
                    return

        new_car = pygame.sprite.Sprite()
        new_car.direction = direction

        image_name = random.choice(CAR_IMAGES)

        # ✅ โหลดรูปแบบถูก path
        original_image = pygame.image.load(
            os.path.join(BASE_DIR, image_name)
        ).convert_alpha()

        new_car.image = pygame.transform.scale(
            original_image, (CAR_WIDTH, CAR_HEIGHT)
        )

        rotation_angle = 90 if direction == 1 else 270
        new_car.image = pygame.transform.rotate(
            new_car.image, rotation_angle
        )

        new_car.image = new_car.image.subsurface(
            new_car.image.get_bounding_rect()
        )

        new_car.mask = pygame.mask.from_surface(new_car.image)
        new_car.rect = new_car.image.get_rect(center=(spawn_x, random_y))

        self.all_cars.append(new_car)
        self.last_spawn_time = current_time

    def move_cars(self):
        for car in self.all_cars:
            car.rect.x -= self.car_speed * car.direction

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        self.level += 1

        # 🔥 ทำให้ spawn เร็วขึ้นตาม level
        self.spawn_cooldown = max(300, self.spawn_cooldown - 100)

        self.reset_levelup()

    def reset_levelup(self):
        self.all_cars = []
        self.assign_lane_directions()

    def reset(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.spawn_cooldown = 800
        self.assign_lane_directions()
