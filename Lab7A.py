# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 7

# Program Lab7A.py
import pygame, sys
from pygame.locals import *

pygame.init()

error = 0

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)

surf1 = pygame.Surface((400, 400))

x = 0
y = 0
z = 0

surf1.fill((x, y, z))

rect1 = pygame.Rect(0, 0, 50, 50)

clock = pygame.time.Clock()

while True :
    while (error == 0) :
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

        screen.fill(color=(0, 0, 0))

        x = x + 1
        y = y + 1
        z = z + 1

        if (x >= 254 and y >= 254 and z >= 254):
           error = error + 1

        surf1.fill((x, y, z))
        screen.blit(surf1, (rect1.x, rect1.y))

        pygame.display.flip()

        clock.tick(60)
    while (error == 1) :
        keys = pygame.key.get_pressed()

        for event in pygame.event.get():
            if keys[pygame.K_ESCAPE]:
                sys.exit(0)

        screen.fill(color=(0, 0, 0))

        x = x - 1
        y = x - 1
        z = z - 1

        if (x <= 1 and y <= 1 and z <= 1):
            error = error - 1

        surf1.fill((x, y, z))
        screen.blit(surf1, (rect1.x, rect1.y))

        pygame.display.flip()

        clock.tick(60)


