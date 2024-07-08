# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 8

# Program Lab8B.py
import pygame, sys
from pygame.locals import *

pygame.init()

errorM = 0
errorT = 0
errorB = 0

resolution = (400, 400)
screen = pygame.display.set_mode(resolution)

midSurf = pygame.Surface((50, 400))
rectMSurf = pygame.Surface((50, 50))
rectTSurf = pygame.Surface((50, 50))
rectBSurf = pygame.Surface((50, 50))

midSurf.fill((0, 255, 0))
rectMSurf.fill((0, 0, 255))
rectTSurf.fill((0, 0, 255))
rectBSurf.fill((0, 0, 255))

midRect = pygame.Rect(175, 0, 50, 400)
rectM = pygame.Rect(150, 175, 50, 50)
rectT = pygame.Rect(150, 0, 50, 50)
rectB = pygame.Rect(150, 350, 50, 50)

clock = pygame.time.Clock()

while True :
        keys = pygame.key.get_pressed()

        for event in pygame.event.get() :
            if keys[K_ESCAPE] or event.type == QUIT:
                sys.exit(0)

        screen.fill((0, 0, 0))

        #Error M
        if errorM == 0:
            rectM = rectM.move(5, 0)
            if rectM.x == 350 :
                errorM = errorM + 1
        else :
            rectM = rectM.move(-5, 0)
            if rectM.x == 0 :
                errorM = errorM - 1

        #Error T
        if errorT == 0:
            rectT = rectT.move(10, 0)
            if rectT.x == 350 :
                errorT = errorT + 1
        else :
            rectT = rectT.move(-10, 0)
            if rectT.x == 0 :
                errorT = errorT - 1

        #Error B
        if errorB == 0:
            rectB = rectB.move(20, 0)
            if rectB.x == 350 :
                errorB = errorB + 1
        else :
            rectB = rectB.move(-20, 0)
            if rectB.x == -10 :
                errorB = errorB - 1

        rect_list = [rectM, rectB, rectT]
        collide = midRect.collidelist(rect_list)

        if collide != -1 :
            midSurf.fill((0, 255, 0))
        else :
            midSurf.fill((255, 0, 0))

        screen.blit(midSurf, (midRect.x, midRect.y))
        screen.blit(rectMSurf, (rectM.x, rectM.y))
        screen.blit(rectBSurf, (rectB.x, rectB.y))
        screen.blit(rectTSurf, (rectT.x, rectT.y))

        pygame.display.flip()

        clock.tick(60)