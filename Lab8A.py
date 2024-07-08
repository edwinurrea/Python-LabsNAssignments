# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 8

# Program Lab8A.py
import pygame, sys
from pygame.locals import *

pygame.init()

error = 0

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)

midSurf = pygame.Surface((50, 400))
rect1Surf = pygame.Surface((50, 50))

midSurf.fill((0, 255, 0))
rect1Surf.fill((0, 0, 255))

midRect = pygame.Rect(175, 0, 50, 400)
rect1 = pygame.Rect(150, 175, 50, 50)

clock = pygame.time.Clock()

while True :
    while (error == 0) :
        keys = pygame.key.get_pressed()

        for event in pygame.event.get() :
            if keys[K_ESCAPE] or event.type == QUIT:
                sys.exit(0)

        screen.fill((0, 0, 0))

        rect1 = rect1.move(5, 0)

        collide = rect1.colliderect(midRect)

        if collide == True :
            midSurf.fill((0, 255, 0))
        else :
            midSurf.fill((255, 0, 0))

        if rect1.x == 350 :
            error = error + 1

        screen.blit(midSurf, (midRect.x, midRect.y))
        screen.blit(rect1Surf, (rect1.x, rect1.y))

        pygame.display.flip()

        clock.tick(60)
    while (error == 1) :
        keys = pygame.key.get_pressed()

        for event in pygame.event.get() :
            if keys[K_ESCAPE] or event.type == QUIT:
                sys.exit(0)

        screen.fill((0, 0, 0))

        rect1 = rect1.move(-5, 0)

        collide = rect1.colliderect(midRect)

        if collide == True :
            midSurf.fill((0, 255, 0))
        else :
            midSurf.fill((255, 0, 0))

        if rect1.x == 0 :
            error = error - 1

        screen.blit(midSurf, (midRect.x, midRect.y))
        screen.blit(rect1Surf, (rect1.x, rect1.y))

        pygame.display.flip()

        clock.tick(60)