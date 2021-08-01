# Sprite ball mouse movement / made with the Rect object

import pygame, sys, time
from pygame.locals import *

pygame.init()

SIZE = WIDTH = HEIGHT = (800, 600)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Mouse Moving Ball')
pygame.mouse.set_visible(False)

player = pygame.Rect(400, 400, 50, 50)

def terminate():
    pygame.quit()
    sys.exit()

background = pygame.image.load('sky.jpg').convert()
ball = pygame.image.load('ball.png').convert_alpha()
ball = pygame.transform.scale(ball, (50, 50))


clock = pygame.time.Clock()
FPS = 30






# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and (event.key == K_ESCAPE):
            running = False
            terminate()

        
    if event.type == MOUSEMOTION:
        player.centerx = event.pos[0]
        player.centery = event.pos[1]

    screen.fill((255, 255, 255))

    screen.blit(background, (0, 0))
    screen.blit(ball, player)
    pygame.display.update()
    clock.tick(FPS)
