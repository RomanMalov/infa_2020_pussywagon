import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (176,196,222), (0,0,400,400)) # Заливка экрана

circle(screen, (255,255,0), (200, 200), 100) # Рожица

circle(screen, (220,20,60), (170, 170), 20) # Левый глаз
circle(screen, (0,0,0), (170, 170), 10)

circle(screen, (220,20,60), (230, 170), 20) # Правый глаз
circle(screen, (0,0,0), (230, 170), 10)

line(screen, (0,0,0), (150,150),(200,160), 10) #Брови
line(screen, (0,0,0), (210,150),(250,130), 10)

rect(screen, (0,0,0), (150,230,100,20)) #Рот

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
