# fonts and colors and clocks!

import sys
import pygame

pygame.init()

# setup speed
size = width, height = 640, 480
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
clock = pygame.time.Clock()

dark_green = (0, 128, 0)
dark_red = (128, 0, 0)

font = pygame.font.SysFont("comicsansms", 144)
# text = font.render("Juliaaaaaa", True, (0, 128, 0))


# ball = pygame.image.load("intro_ball.gif")
# ballrect = ball.get_rect()

frame = 0
while 1:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT or
            (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
            pygame.quit()
            sys.exit()

    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
        # speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
        # speed[1] = -speed[1]

    color = None
    if frame % 2 == 0:
        color = dark_red
    else:
        color = dark_green

    screen.fill(black)
    text = font.render("Juliaaaaaa", True, color)
    # screen.blit(ball, ballrect)
    screen.blit(text,
	    (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.flip()

    frame += 1
    clock.tick(30)
