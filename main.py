import pygame
from pygame.locals import *


pygame.init()
run = True
screen = pygame.display.set_mode((800, 750))
# set title of window
pygame.display.set_caption("Dante Car Dodger")
# set background colour
screen.fill((60, 220, 0))
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
