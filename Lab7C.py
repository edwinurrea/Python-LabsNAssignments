# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 7

# Program Lab7C.py
import pygame, sys
from pygame.locals import *

pygame.init()

error = 0

resolution = (1000, 500)
screen = pygame.display.set_mode(resolution)

surf1 = pygame.Surface((100, 100))
surf2 = pygame.Surface((100, 100))

surf1.fill((0, 255, 0))
surf2.fill((0, 0, 255))

rect1 = pygame.Rect(0, 0, 100, 100)
rect2 = pygame.Rect(0, 400, 100, 100)

clock = pygame.time.Clock()

while True :
    while (error == 0) :
        keys = pygame.key.get_pressed()

        for event in pygame.event.get() :
            if keys[pygame.K_ESCAPE] :
                sys.exit(0)

        screen.fill(color=((0,0,0)))

        rect1 = rect1.move(5, 0)
        rect2 = rect2.move(5, 0)

        if (rect1.x >= 900 and rect2.x >= 900) :
            error = error + 1

        screen.blit(surf1, (rect1.x, rect1.y))
        screen.blit(surf2, (rect2.x, rect2.y))

        pygame.display.flip()

        clock.tick(60)
    while (error == 1) :
        keys = pygame.key.get_pressed()

        for event in pygame.event.get() :
            if keys[pygame.K_ESCAPE] :
                sys.exit(0)

        screen.fill(color=((0, 0, 0)))

        rect1 = rect1.move(-5, 0)
        rect2 = rect2.move(-5, 0)

        if (rect1.x <= 1 and rect2.x <= 1) :
            error = error - 1

        screen.blit(surf1, (rect1.x, rect1.y))
        screen.blit(surf2, (rect2.x, rect2.y))

        pygame.display.flip()

        clock.tick(60)
