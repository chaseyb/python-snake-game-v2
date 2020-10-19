import pygame

# Starts game 
pygame.init()

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

# quits game 
pygame.quit()
quit()
