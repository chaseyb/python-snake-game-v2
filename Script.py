import pygame

# Starts game 
pygame.init()

white = (255,255,255)
black = (0,0,0)

# Game display window 
gameDisplay = pygame.display.set_mode((800,600))

#updates game
pygame.display.update()
pygame.display.set_caption('Snake Game V2 by Chaseyb')

gameExit = False

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [400, 300, 10, 10])

    pygame.display.update() 


