import pygame
from pygame.locals import *

size = width, height = (800, 800)
road_w = int(width / 1.6)

# initialis e pygame
pygame.init()
run = True
# set window size
screen = pygame.display.set_mode(size)
# set title of window
pygame.display.set_caption("Dante Car Dodger")
# set background colour
screen.fill((60, 220, 0))

# display graphics
pygame.draw.rect(screen, (50, 50, 50), (width / 2 - road_w / 2, 0, road_w, height))

# apply changes
pygame.display.update()

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

pygame.quit()


def main():
    pass


if __name__ == "__main__":
    pass
