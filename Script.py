import pygame
import random
import pickle  # pickle is used for high score saving

# Starts game 
pygame.init()

# Color definitions 
white = (255,255,255)
black = (0,0,0)

# Game property constants
display_width = 800
display_height = 600
blockSize = 20

# Game display window 
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Updates game
pygame.display.update()
pygame.display.set_caption('Snake Game V2 by Chaseyb')

gameExit = False

lead_x = 300
lead_y = 300

lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

# Main game loop
while not gameExit:
    # Defines snake movement 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0

    # Defines window boundary
    if lead_x >= 800 or lead_x < 0 or lead_y >= 600 or lead_y < 0:
        gameExit = True 
    
    lead_x += lead_x_change
    lead_y += lead_y_change
    # Defines game background
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
    # Updates game display
    pygame.display.update() 
    # Defines game FPS
    clock.tick(30)


pygame.quit()
quit()