# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 8

# Program Lab8C.py
import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (500, 500)
screen = pygame.display.set_mode(resolution)

surf1 = pygame.Surface((50, 50))

surf1.fill((0, 0, 255))

rect1 = pygame.Rect(225, 225, 50, 50)

clock = pygame.time.Clock()

while True :
    keys = pygame.key.get_pressed()

    for event in pygame.event.get() :
        if keys[K_ESCAPE] or event.type == QUIT :
            sys.exit(0)

        if event.type == KEYDOWN :
            if event.key == K_w :
                if rect1.top > 0 :
                    rect1 = rect1.move(0, -5)
            if event.key == K_s :
                if rect1.bottom < 500 :
                    rect1 = rect1.move(0, 5)
            if event.key == K_d :
                if rect1.right < 500 :
                    rect1 = rect1.move(5, 0)
            if event.key == K_a :
                if rect1.left > 0 :
                    rect1 = rect1.move(-5, 0)
            if event.key == K_r :
                rect1 = pygame.Rect(225, 225, 50, 50)

    screen.fill((0, 0, 0))

    screen.blit(surf1, rect1)

    pygame.display.flip()

    clock.tick(60)