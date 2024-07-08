# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Lab: 9

# Program Lab9.py
import pygame, sys
from pygame.locals import *

pygame.init()

status = "Off"
charging = False
ready = False
shooting = False
discharging = False

resolution = (500, 500)
screen = pygame.display.set_mode(resolution)

clock = pygame.time.Clock()

laser = pygame.image.load("Lab 9/laser-98735_640.png").convert_alpha()
on = pygame.image.load("Lab 9/button-7086658_640_on.png").convert_alpha()
off = pygame.image.load("Lab 9/button-7086658_640_off.png").convert_alpha()

scaledLaser = pygame.transform.scale(laser, (100, 100))
scaledOn = pygame.transform.scale(on, (100, 100))
scaledOff = pygame.transform.scale(off, (100, 100))

laserRect = pygame.Rect(200, 200, 100, 100)
onRect = pygame.Rect(laserRect.left - 120, 200, 100, 100)
offRect = pygame.Rect(laserRect.right + 20, 200, 100, 100)

font32 = pygame.font.Font(None, 32)
font64 = pygame.font.Font(None, 64)

shootSound = pygame.mixer.Sound("Lab 9/blaster-2-81267.mp3")
powerUpSound = pygame.mixer.Sound("Lab 9/power-up-7103.mp3")
powerDownSound = pygame.mixer.Sound("Lab 9/power-down-7103.mp3")

while True :
    keys = pygame.key.get_pressed()

    for event in pygame.event.get() :
        if keys[K_ESCAPE] or event.type == QUIT :
            sys.exit(0)
        elif event.type == MOUSEBUTTONDOWN :
            if status == "Off" and onRect.collidepoint(event.pos) :
                status = "Charging"
                charging = True
                powerUpSound.play()
            elif status == "Ready" and offRect.collidepoint(event.pos) :
                status = "Discharging"
                discharging = True
                powerDownSound.play()
            elif status == "Ready" and laserRect.collidepoint(event.pos) :
                status = "Shooting"
                charging = True
                shootSound.play()

    if charging and pygame.mixer.get_busy() :
        status = "Ready"
        charging = False
    elif discharging and not pygame.mixer.get_busy() :
        status = "Off"
        discharging = False
    elif shooting and not pygame.mixer.get_busy() :
        status = "Ready"
        shooting = False

    screen.fill((255, 255, 255))

    statusText = font64.render(status, True, (0, 0, 0))
    shootText = font32.render("Shoot", True, (0, 0, 0))
    powerUpText = font32.render("Power Up", True, (0, 0, 0))
    powerDownText = font32.render("Power Down", True, (0, 0, 0))

    statusRect = statusText.get_rect(center=(250, 170))
    shootRect = shootText.get_rect(midtop=laserRect.midbottom)
    powerUpRect = powerUpText.get_rect(midtop=onRect.midbottom)
    powerDownRect = powerDownText.get_rect(midtop=offRect.midbottom)

    screen.blit(statusText, statusRect)
    screen.blit(shootText, shootRect)
    screen.blit(powerUpText, powerUpRect)
    screen.blit(powerDownText, powerDownRect)

    screen.blit(scaledLaser, laserRect.topleft)
    screen.blit(scaledOn, onRect.topleft)
    screen.blit(scaledOff, offRect.topleft)

    pygame.display.flip()

    clock.tick(60)