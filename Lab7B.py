# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 7

# Program Lab7B.py
import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (600, 600)
screen = pygame.display.set_mode(resolution)

surf1 = pygame.Surface((60, 60))
surf2 = pygame.Surface((60, 60))
surf3 = pygame.Surface((60, 60))
surf4 = pygame.Surface((60, 60))
surf5 = pygame.Surface((60, 60))

surf1.fill((255, 0, 0))
surf2.fill((255, 0, 0))
surf3.fill((255, 0, 0))
surf4.fill((255, 0, 0))
surf5.fill((255, 0, 0))

rect1 = pygame.Rect(0, 0, 60, 60)
rect2 = pygame.Rect(540, 0, 60, 60)
rect3 = pygame.Rect(0, 540, 60, 60)
rect4 = pygame.Rect(540, 540, 60, 60)
rect5 = pygame.Rect(270, 270, 60, 60)

clock = pygame.time.Clock()

while True :
    keys = pygame.key.get_pressed()

    for event in pygame.event.get() :
        if keys[pygame.K_ESCAPE] :
            sys.exit(0)

    screen.fill(color=((0,0,0)))

    screen.blit(surf1, (rect1.x, rect1.y))
    screen.blit(surf2, (rect2.x, rect2.y))
    screen.blit(surf3, (rect3.x, rect3.y))
    screen.blit(surf4, (rect4.x, rect4.y))
    screen.blit(surf5, (rect5.x, rect5.y))

    pygame.display.flip()

    clock.tick(60)

