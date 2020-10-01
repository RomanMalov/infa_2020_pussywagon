import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((500, 400))

rect(screen, (0, 255, 0), (0, 200, 500, 200))
rect(screen, (0, 0, 128), (0, 0, 500, 200))

circle(screen, (255, 255, 0), (30, 30), 30)
line(screen, (255, 255, 0), (30, 30), (80, 50), 5)
line(screen, (255, 255, 0), (30, 30), (70, 80), 5)
line(screen, (255, 255, 0), (30, 30), (55, 88), 5)
line(screen, (255, 255, 0), (30, 30), (40, 87), 5)
line(screen, (255, 255, 0), (25, 30), (15, 80), 5)
line(screen, (255, 255, 0), (30, 30), (87, 30), 5)

ellipse(screen, (0, 0, 0), (100, 130, 70, 180))
line(screen, (0, 0, 0), (135, 130), (135, 310), 4)
polygon(screen, (255, 255, 255), [(120, 140), (150, 140), (135, 230)])
polygon(screen, (255, 150, 100), [(135, 166), (120, 159), (120, 173)])
polygon(screen, (255, 150, 100), [(135, 166), (150, 159), (150, 173)])
polygon(screen, (0, 0, 0), [(135, 166), (120, 159), (120, 173)], 2)
polygon(screen, (0, 0, 0), [(135, 166), (150, 159), (150, 173)], 2)
circle(screen, (0, 0, 0), (135, 180), 3)
circle(screen, (0, 0, 0), (135, 205), 3)
line(screen, (0, 0, 0), (120, 300), (80, 350), 5)
line(screen, (0, 0, 0), (150, 300), (190, 350), 5)
line(screen, (0, 0, 0), (110, 170), (60, 250), 5)
line(screen, (0, 0, 0), (160, 170), (225, 250), 5)
circle(screen, (255, 165, 0), (135, 130), 30)
circle(screen, (0, 0, 0), (145, 117), 3)
circle(screen, (0, 0, 0), (125, 117), 3)
circle(screen, (0, 0, 0), (135, 130), 3)
arc(screen, (0, 0, 0), (125, 132, 20, 15), 4, 6)

polygon(screen, (128, 0, 0), [(60, 250), (60, 220), (20, 235)])
circle(screen, (255, 0, 0), (30, 230), 10)
circle(screen, (0, 0, 0), (35, 225), 10)
circle(screen, (255, 255, 255), (50, 220), 10)

polygon(screen, (128, 0, 0), [(230, 300), (400, 300), (315, 130)])
line(screen, (0, 0, 0), (300, 300), (250, 350), 5)
line(screen, (0, 0, 0), (340, 300), (390, 350), 5)
line(screen, (0, 0, 0), (300, 170), (225, 250), 5)
line(screen, (0, 0, 0), (330, 170), (370, 210), 5)
line(screen, (0, 0, 0), (370, 210), (410, 210), 5)
circle(screen, (255, 165, 0), (315, 130), 30)
circle(screen, (0, 0, 0), (325, 117), 3)
circle(screen, (0, 0, 0), (305, 117), 3)
circle(screen, (0, 0, 0), (315, 130), 3)
arc(screen, (0, 0, 0), (305, 132, 20, 15), 4, 6)
arc(screen, (0, 0, 0), (275, 102, 60, 55), 1.6, 4, 6)
arc(screen, (0, 0, 0), (290, 97, 60, 65), 1.6, 4, 6)
arc(screen, (0, 0, 0), (290, 97, 60, 65), 0, 1.6, 6)
arc(screen, (0, 0, 0), (290, 100, 60, 60), -0.3, 1.6, 6)

line(screen, (128, 128, 128), (410, 210), (470, 100), 2)
ellipse(screen, (255, 0, 0), (460, 50, 40, 50))
line(screen, (128, 128, 128), (410, 210), (455, 85), 2)
ellipse(screen, (155, 0, 100), (440, 40, 40, 50))
line(screen, (128, 128, 128), (410, 210), (435, 75), 2)
ellipse(screen, (0, 255, 0), (420, 30, 40, 50))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
