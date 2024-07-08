# Class: CSE 1321L
# Section: WJ2
# Term: Summer 2024
# Instructor: Milo Wilson
# Name: Edwin Urrea
# Assignment: 5

# Program Assignment5.py
import pygame, sys
from pygame.locals import *

pygame.init()

resolution = (800, 600)
screen = pygame.display.set_mode(resolution)

collection = 0
collected = False
timeLeft = 30
timerStart = False
win = False

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

mazeWidth = len(maze[0])
mazeHeight = len(maze)
mazeSizeX = mazeWidth * 50
mazeSizeY = mazeHeight * 50
mazeOffsetX = (800 - mazeSizeX) // 2
mazeOffsetY = (600 - mazeSizeY + 50) // 2

playerPos = [1, 0]
playerRect = pygame.Rect(playerPos[1] * 50 + mazeOffsetX, playerPos[0] * 50 + mazeOffsetY, 50, 50)
treasurePos = [9, 1]
treasureRect = pygame.Rect(treasurePos[1] * 50 + mazeOffsetX, playerPos[0] * 50 + mazeOffsetY, 50, 50)

clock = pygame.time.Clock()

playerImage = pygame.image.load('files/player.png').convert()
treasureImage = pygame.image.load('files/treasure.png').convert_alpha()
player = pygame.transform.scale(playerImage, (50, 50))
treasure = pygame.transform.scale(treasureImage, (50, 50))

treasureCollected = pygame.mixer.Sound("files/treasureCollected.wav")

def drawMaze():
    for row in range(len(maze)) :
        for col in range(len(maze[row])) :
            if maze[row][col] == 1 :
                pygame.draw.rect(screen, (255,255,255), (col * 50 + mazeOffsetX, row * 50 + mazeOffsetY, 50, 50))
            elif maze[row][col] == 0 :
                pygame.draw.rect(screen, (0,0,0), (col * 50 + mazeOffsetX, row * 50 + mazeOffsetY, 50, 50))
            if [row, col] == treasurePos :
                screen.blit(treasure, (col * 50 + mazeOffsetX, row * 50 + mazeOffsetY))

def movePlayer(dx, dy) :
    global playerPos, playerRect
    new_x = playerPos[0] + dy
    new_y = playerPos[1] + dx
    if 0 <= new_x < len(maze) and 0 <= new_y < len(maze[0]) and maze[new_x][new_y] == 0 :
        playerPos = [new_x, new_y]
        playerRect.center = (new_y * 50 + 25 + mazeOffsetX, new_x * 50 + 25 + mazeOffsetY)

def checkCollected() :
    global collected, collection, treasurePos, treasureRect
    if playerPos == treasurePos and collection == 0 :
        collected = True
        collection = collection + 1
        treasureCollected.play()
        treasurePos = [0]
    return collection

def timer() :
    global timeLeft
    font = pygame.font.Font(None, 31)
    text = font.render("Timer: " + str(int(timeLeft)), True, (255, 180, 255))
    screen.blit(text, (680, 10))
    timeLeft -= clock.get_time() / 1000

def reset() :
    global collection, collected, timeLeft, win
    collection = 0
    collected = False
    timeLeft = 30
    win = False
    playerPos[:] = [1, 0]
    playerRect = pygame.Rect(playerPos[1] * 50 + mazeOffsetX, playerPos[0] * 50 + mazeOffsetY, 50, 50)

def keys() :
    keys = pygame.key.get_pressed()

    for event in pygame.event.get() :
        if keys[K_ESCAPE] or event.type == QUIT :
            sys.exit(0)

        if event.type == KEYDOWN :
            if event.key == K_w :
                movePlayer(0, -1)
            if event.key == K_s :
                movePlayer(0, 1)
            if event.key == K_d :
                movePlayer(1, 0)
            if event.key == K_a :
                movePlayer(-1, 0)
            if event.key == K_r :
                if collected == 0 :
                    reset()

def checkPlayerWin() :
    global win
    if playerPos == [1, 0] :
        font = pygame.font.Font(None, 150)
        text = font.render("You Win!", True, (255, 0, 0))
        screen.blit(text, (200, 300))
        win = True
    return win

while not win :
    while collection == 0 :
        keys()

        screen.fill((0, 0, 0))

        drawMaze()
        screen.blit(player, (playerPos[1] * 50 + mazeOffsetX, playerPos[0] * 50 + mazeOffsetY))

        collection = checkCollected()

        pygame.display.flip()

        clock.tick(60)
    while timeLeft > 0 and collection >= 1 and not win :
        keys()

        screen.fill((0, 0, 0))

        drawMaze()
        screen.blit(player, (playerPos[1] * 50 + mazeOffsetX, playerPos[0] * 50 + mazeOffsetY))

        maze[8][3] = 1
        maze[9][11] = 0
        maze[6][9] = 0
        maze[2][1] = 1

        win = checkPlayerWin()

        timer()

        pygame.display.flip()

        clock.tick(60)