import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("2474215.jpg")

#icon
icon = pygame.image.load('outer-space-alien.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("space invaders")

#player
playerIMG = pygame.image.load('aircraft.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy

enemyIMG = pygame.image.load('ufo.png')
enemyX = random.randint (0, 736)
enemyY = random.randint (50, 150)
enemyX_change = 0.3
enemyY_change = 40

def player(x,y):
    screen.blit(playerIMG, (playerX, playerY))

def enemy(x, y):
    screen.blit(enemyIMG, (enemyX, enemyY))

#event
running = True
while running:
    screen.fill((255, 255, 255))

    screen.blit(background, (0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    #if key is pressed
    if event.type == pygame.KEYDOWN:
        print('a keystroke is pressed')
        if event.key == pygame.K_LEFT:
           playerX_change = -0.4
        if event.key == pygame.K_RIGHT:
            playerX_change = 0.4

    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0

    # player bounder

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # enemy bounder
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change

    player(playerX,playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
