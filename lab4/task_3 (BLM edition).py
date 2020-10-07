import pygame
from pygame.draw import *

'''kids, left right hands up'''
pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 400))
GREEN = (0, 255, 0)
BLUE = (50, 100, 128)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BROWN = (255, 150, 100)
DARK_BROWN = (128, 75, 50)

SKIN_COLOR = DARK_BROWN
DARK_RED = (128, 0, 0)
LIGHT_BLUE = (0, 200, 200)
GRAY = (128, 128, 128)
MAGENTA = (155, 0, 100)
RED = (255, 0, 0)

rect(screen, GREEN, (0, 200, 900, 200))
rect(screen, BLUE, (0, 0, 900, 200))


def draw_sun(color, x, y):
    """drawing sun with center on x, y and color of color
    """
    circle(screen, color, (x + 30, y + 30), 30)
    line(screen, color, (x + 30, y + 30), (80, 50), 5)
    line(screen, color, (x + 30, y + 30), (70, 80), 5)
    line(screen, color, (x + 30, y + 30), (55, 88), 5)
    line(screen, color, (x + 30, y + 30), (40, 87), 5)
    line(screen, color, (x + 25, y + 30), (15, 80), 5)
    line(screen, color, (x + 30, y + 30), (87, 30), 5)


def draw_men(skin_color, tie_color, chiral, scale, hand_height, x, y):
    """draw men with left up angle in x, y, skin color is skin_color and bowtie is tie_color
        just don't touch
    """
    x -= 135
    y -= 130
    # body
    if chiral == 'left':
        ellipse(screen, BLACK, (int(scale * (x + 100)), int(scale * (y + 130)), int(scale * (70)), int(scale * 180)))

        # shirt
        polygon(screen, WHITE,
                [(int(scale * (x + 120)), int(scale * (y + 140))), (int(scale * (x + 150)), int(scale * (y + 140))),
                 (int(scale * (x + 135)), int(scale * (y + 230)))])

        # bowtie
        polygon(screen, tie_color,
                [(int(scale * (x + 135)), int(scale * (y + 166))), (int(scale * (x + 120)), int(scale * (y + 159))),
                 (int(scale * (x + 120)), int(scale * (y + 173)))])
        polygon(screen, tie_color,
                [(int(scale * (x + 135)), int(scale * (y + 166))), (int(scale * (x + 150)), int(scale * (y + 159))),
                 (int(scale * (x + 150)), int(scale * (y + 173)))])

        polygon(screen, BLACK,
                [(int(scale * (x + 135)), int(scale * (y + 166))), (int(scale * (x + 120)), int(scale * (y + 159))),
                 (int(scale * (x + 120)), int(scale * (y + 173)))], 2)
        polygon(screen, BLACK,
                [(int(scale * (x + 135)), int(scale * (y + 166))), (int(scale * (x + 150)), int(scale * (y + 159))),
                 (int(scale * (x + 150)), int(scale * (y + 173)))], 2)
        circle(screen, BLACK, (int(scale * (x + 135)), int(scale * (y + 180))), int(scale * (3)))
        circle(screen, BLACK, (int(scale * (x + 135)), int(scale * (y + 205))), int(scale * (3)))
        line(screen, BLACK, (int(scale * (x + 120)), int(scale * (y + 300))),
             (int(scale * (x + 80)), int(scale * (y + 350))), int(scale * (5)))
        line(screen, BLACK, (int(scale * (x + 150)), int(scale * (y + 300))),
             (int(scale * (x + 190)), int(scale * (y + 350))), int(scale * (5)))
        line(screen, BLACK, (int(scale * (x + 110)), int(scale * (y + 170))),
             (int(scale * (x + 60)), int(scale * (y + 250))), int(scale * (5)))
        line(screen, BLACK, (int(scale * (x + 160)), int(scale * (y + 170))),
             (int(scale * (x + 225)), int(scale * (y + hand_height))), int(scale * (5)))

        # head
        circle(screen, skin_color, (int(scale * (x + 135)), int(scale * (y + 130))), int(scale * (30)))
        # eyes
        circle(screen, BLACK, (int(scale * (x + 145)), int(scale * (y + 117))), int(scale * (3)))
        circle(screen, BLACK, (int(scale * (x + 125)), int(scale * (y + 117))), int(scale * (3)))
        # nose
        circle(screen, BLACK, (int(scale * (x + 135)), int(scale * (y + 130))), int(scale * (3)))
        # mouth
        arc(screen, BLACK, (int(scale * (x + 125)), int(scale * (y + 132)), int(scale * (20)), int(scale * (15))), 4, 6)
    if chiral == 'right':
        ellipse(screen, BLACK, (int(scale * (x + 100)), int(scale * (y + 130)), int(scale * (70)), int(scale * 180)))

        # shirt
        polygon(screen, WHITE,
                [(int(scale * (x + 120)), int(scale * (y + 140))), (int(scale * (x + 150)), int(scale * (y + 140))),
                 (int(scale * (x + 135)), int(scale * (y + 230)))])

        # bowtie
        polygon(screen, tie_color,
                [(int(scale * (x + 135)), int(scale * (y + 166))), (int(scale * (x + 120)), int(scale * (y + 159))),
                 (int(scale * (x + 120)), int(scale * (y + 173)))])
        polygon(screen, tie_color,
                [(int(scale * (x + 135)), int(scale * (y + 166))), (int(scale * (x + 150)), int(scale * (y + 159))),
                 (int(scale * (x + 150)), int(scale * (y + 173)))])

        polygon(screen, BLACK,
                [(int(scale * (x + 135)), int(scale * (y + 166))), (int(scale * (x + 120)), int(scale * (y + 159))),
                 (int(scale * (x + 120)), int(scale * (y + 173)))], 2)
        polygon(screen, BLACK,
                [(int(scale * (x + 135)), int(scale * (y + 166))), (int(scale * (x + 150)), int(scale * (y + 159))),
                 (int(scale * (x + 150)), int(scale * (y + 173)))], 2)
        circle(screen, BLACK, (int(scale * (x + 135)), int(scale * (y + 180))), int(scale * (3)))
        circle(screen, BLACK, (int(scale * (x + 135)), int(scale * (y + 205))), int(scale * (3)))
        line(screen, BLACK, (int(scale * (x + 120)), int(scale * (y + 300))),
             (int(scale * (x + 80)), int(scale * (y + 350))), int(scale * (5)))
        line(screen, BLACK, (int(scale * (x + 150)), int(scale * (y + 300))),
             (int(scale * (x + 190)), int(scale * (y + 350))), int(scale * (5)))
        line(screen, BLACK, (int(scale * (x + 110)), int(scale * (y + 170))),
             (int(scale * (x + 60)), int(scale * (y + hand_height))), int(scale * (5)))
        line(screen, BLACK, (int(scale * (x + 160)), int(scale * (y + 170))),
             (int(scale * (x + 225)), int(scale * (y + 250))), int(scale * (5)))

        # head
        circle(screen, skin_color, (int(scale * (x + 135)), int(scale * (y + 130))), int(scale * (30)))
        # eyes
        circle(screen, BLACK, (int(scale * (x + 145)), int(scale * (y + 117))), int(scale * (3)))
        circle(screen, BLACK, (int(scale * (x + 125)), int(scale * (y + 117))), int(scale * (3)))
        # nose
        circle(screen, BLACK, (int(scale * (x + 135)), int(scale * (y + 130))), int(scale * (3)))
        # mouth
        arc(screen, BLACK, (int(scale * (x + 125)), int(scale * (y + 132)), int(scale * (20)), int(scale * (15))), 4, 6)


def draw_woman(dress_color, skin_color, chiral, hand_height, scale,x, y):
    x -= 315
    y -= 130
    surface1 = pygame.Surface((500, 500), pygame.SRCALPHA)  # per-pixel alpha
    surface1.fill((255, 255, 255, 0))
    if chiral == 'right':
        # dress
        polygon(surface1, dress_color, [(x + 230, y + 300), (x + 400, y + 300), (x + 315, y + 130)])
        # hands
        line(surface1, BLACK, (x + 300, y + 300), (x + 250, y + 350), 5)
        line(surface1, BLACK, (x + 340, y + 300), (x + 390, y + 350), 5)

        line(surface1, BLACK, (x + 300, y + 170), (x + 225, y + hand_height), 5)

        line(surface1, BLACK, (x + 330, y + 170), (x + 370, y + 210), 5)
        line(surface1, BLACK, (x + 370, y + 210), (x + 410, y + 210), 5)
        circle(surface1, skin_color, (x + 315, y + 130), 30)
        circle(surface1, BLACK, (x + 325, y + 117), 3)
        circle(surface1, BLACK, (x + 305, y + 117), 3)
        circle(surface1, BLACK, (x + 315, y + 130), 3)
        # hair
        arc(surface1, BLACK, (x + 305, y + 132, 20, 15), 4, 6)
        arc(surface1, BLACK, (x + 275, y + 102, 60, 55), 1.6, 4, 6)
        arc(surface1, BLACK, (x + 290, y + 97, 60, 65), 1.6, 4, 6)
        arc(surface1, BLACK, (x + 290, y + 97, 60, 65), 0, 1.6, 6)
        arc(surface1, BLACK, (x + 290, y + 100, 60, 60), -0.3, 1.6, 6)
    if chiral == 'left':
        x0 = 625
        # dress
        polygon(surface1, dress_color,
                [(x0 - (-x + 230), y + 300), (x0 - (-x + 400), y + 300), (x0 - (-x + 315), y + 130)])
        # hands
        line(surface1, BLACK, (x0 - (-x + 300), y + 300), (x0 - (-x + 250), y + 350), 5)
        line(surface1, BLACK, (x0 - (-x + 340), y + 300), (x0 - (-x + 390), y + 350), 5)

        line(surface1, BLACK, (x0 - (-x + 300), y + 170), (x0 - (-x + 225), y + hand_height), 5)

        line(surface1, BLACK, (x0 - (-x + 330), y + 170), (x0 - (-x + 370), y + 210), 5)
        line(surface1, BLACK, (x0 - (-x + 370), y + 210), (x0 - (-x + 410), y + 210), 5)
        circle(surface1, skin_color, (x0 - (-x + 315), y + 130), 30)
        circle(surface1, BLACK, (x0 - (-x + 325), y + 117), 3)
        circle(surface1, BLACK, (x0 - (-x + 305), y + 117), 3)
        circle(surface1, BLACK, (x0 - (-x + 315), y + 130), 3)
        # hair
        arc(surface1, BLACK, (x0 - (-x + 305) - 20, y + 132, 20, 15), 4, 6)
        arc(surface1, BLACK, (x0 - (-x + 275) - 60, y + 102, 60, 55), 1.6, 4, 6)
        arc(surface1, BLACK, (x0 - (-x + 290) - 60, y + 97, 60, 65), 1.6, 4, 6)
        arc(surface1, BLACK, (x0 - (-x + 290) - 60, y + 97, 60, 65), 0, 1.6, 6)
        arc(surface1, BLACK, (x0 - (-x + 290) - 60, y + 100, 60, 60), -0.3, 1.6, 6)
    surface2 =pygame.transform.scale(surface1, (int(scale*500), int(scale*500)))
    return surface2

def draw_icecream(col1, col2, col3, waffle_color, chiral, x, y):
    x -= 30
    y -= 230
    if chiral == 'right':
        polygon(screen, waffle_color, [(x + 60, y + 250), (x + 60, y + 220), (x + 20, y + 235)])
        circle(screen, col1, (x + 30, y + 230), 10)
        circle(screen, col2, (x + 35, y + 225), 10)
        circle(screen, col3, (x + 50, y + 220), 10)
    if chiral == 'left':
        x0 = 1000
        polygon(screen, waffle_color, [(x0 - (-x + 60), y + 250), (x0 - (-x + 60), y + 220), (x0 - (-x + 20), y + 235)])
        circle(screen, col1, (x0 - (-x + 30), y + 230), 10)
        circle(screen, col2, (x0 - (-x + 35), y + 225), 10)
        circle(screen, col3, (x0 - (-x + 50), y + 220), 10)


def draw_balls(col1, col2, col3, thread_color, x, y):
    x -= 400
    y -= 210
    # threads

    line(screen, thread_color, (x + 410, y + 210), (x + 470, y + 100), 2)
    line(screen, thread_color, (x + 410, y + 210), (x + 455, y + 85), 2)
    line(screen, thread_color, (x + 410, y + 210), (x + 435, y + 75), 2)
    # balls
    ellipse(screen, col1, (x + 460, y + 50, 40, 50))
    ellipse(screen, col2, (x + 440, y + 40, 40, 50))
    ellipse(screen, col3, (x + 420, y + 30, 40, 50))


draw_sun(YELLOW, 0, 0)
draw_men(SKIN_COLOR, BLUE, 'left', 1, 250, 100, 150)
screen.blit(draw_woman(RED, SKIN_COLOR, 'right',250, 1, 80,  50), (200, 100))
screen.blit(draw_woman(RED, SKIN_COLOR, 'left', 50, 0.5, 80,  50), (130, 250))
screen.blit(draw_woman(RED, SKIN_COLOR, 'left',250, 1, 80,  50), (400, 100))
draw_men(SKIN_COLOR, BLUE, 'left', 1, 250, 650, 150)
draw_men(SKIN_COLOR, BLUE, 'right', 0.5, 50, 1200, 600)

draw_balls(RED, GREEN, SKIN_COLOR, GRAY, 390, 230)
draw_icecream(RED, BLACK, SKIN_COLOR, BLUE, 'right', 710, 250)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
