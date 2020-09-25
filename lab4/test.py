
import pygame

from pygame.draw import *

FPS = 30

pygame.init()

screen = pygame.display.set_mode((300,200))

pygame.display.update()

while True:
    clock = pygame.time.Clock()
    clock.tick(FPS)
    
    for event in pygame.event.get():
        if event.type() == pygame.QUIT:
            pygame.quit()
