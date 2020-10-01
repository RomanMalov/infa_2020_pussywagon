import pygame
from pygame.draw import *

pygame.init()


WIDTH = 1032
HEIGHT = 768
FPS = 30
screen = pygame.display.set_mode((WIDTH, HEIGHT))

rect(screen, (175, 238, 238), (0, 0, WIDTH, HEIGHT / 2))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
