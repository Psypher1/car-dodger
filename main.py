import pygame
from pygame.locals import *
import random

size = width, height = (800, 750)
road_w = int(width / 1.6)
roadmark_w = int(width / 80)
left_lane = width / 2 - road_w / 4
right_lane = width / 2 + road_w / 4

# initialise pygame
pygame.init()
run = True
# set window size
screen = pygame.display.set_mode(size)
# set title of window
pygame.display.set_caption("Dante Car Dodger")
# set background colour
screen.fill((60, 220, 0))

# apply changes
pygame.display.update()

# load  images
## player car
car = pygame.image.load("./assets/car.png")
car_loc = car.get_rect()
car_loc.center = left_lane, height * 0.8

## enemy car
enemy = pygame.image.load("./assets/enemy.png")
enemy_loc = enemy.get_rect()
enemy_loc.center = right_lane, height * 0.2

# game loop
while run:
    # animate ememy car
    enemy_loc[1] += 1
    if enemy_loc[1] > height:
        # enemy_loc[1] = -200
        if random.randint(0, 1) == 0:
            enemy_loc.center = left_lane, -200
        else:
            enemy_loc.center = right_lane, -200

    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
        if event.type == KEYDOWN:
            if event.key in [K_a, K_LEFT]:
                car_loc = car_loc.move([-int(road_w / 2), 0])
            if event.key in [K_d, K_RIGHT]:
                car_loc = car_loc.move([int(road_w / 2), 0])

    # display graphics
    ## road
    pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))

    ## center line
    pygame.draw.rect(
        screen, (255, 255, 255), (width / 2 - roadmark_w / 2, 0, roadmark_w, height)
    )

    pygame.draw.rect(
        screen,
        (255, 245, 40),
        (width / 2 - road_w / 2 + roadmark_w * 2, 0, roadmark_w, height),
    )
    pygame.draw.rect(
        screen,
        (255, 245, 40),
        (width / 2 + road_w / 2 - roadmark_w * 3, 0, roadmark_w, height),
    )

    screen.blit(car, car_loc)
    screen.blit(enemy, enemy_loc)
    pygame.display.update()

pygame.quit()


def main():
    pass


if __name__ == "__main__":
    pass
