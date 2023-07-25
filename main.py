import pygame
from pygame.locals import *


pygame.init()
run = True

while run:
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

pygame.quit()


def main():
    pass


if __name__ == "__main__":
    pass
