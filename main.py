import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

# title icon
icon = pygame.image.load('outer-space-alien.png')
pygame.display.set_icon(icon)
pygame.display.set_caption("space invaders")

#player
playerIMG = pygame.image.load('aircraft.png')
playerX = 370
playerY = 480
playerX_change = 0

def player(x,y):
    screen.blit(playerIMG, (playerX, playerY))

#event
running = True
while running:
    screen.fill((255, 255, 255))

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


    playerX += playerX_change
    player(playerX,playerY)
    pygame.display.update()



