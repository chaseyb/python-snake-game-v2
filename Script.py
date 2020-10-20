import pygame
import time 
import random
import os
import pickle

# Starts game 
pygame.init()
# Centers the game window 
os.envirson['SDL_VIDEO_CENTERED'] = '1' 

# Color definitions 
white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
lightRed = (249, 52, 52)
green = (0, 155, 0)
lightGreen = (74, 196, 74)

# Game property constants
display_width = 800
display_height = 600
blockSize = 20
FPS = 30
font = pygame.font.SysFont(None, 25)

# Importing images
snakeHeadImage = pygame.image.load("images/SnakeHead.png")
snakeBodyImage = pygame.image.load("images/SnakeBody.png")
appleImage = pygame.image.load("images/Apple.png")
goldenAppleImage = pygame.image.load("images/GoldenApple.png")
icon = pygame.image.load("images/Icon.png")

# Game display window 
gameDisplay = pygame.display.set_mode((display_width,display_height))

# Updates game
pygame.display.update()
pygame.display.set_caption('Snake Game')

gameExit = False

lead_x = display_height/2
lead_y = display_width/2

lead_x_change = 0
lead_y_change = 0

clock = pygame.time.Clock()

# Game Over message 
def message_to_screen (msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])

# Main game loop
def gameLoop():
while not gameExit:
    # Defines snake movement 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -blockSize
                lead_y_change = 0
            elif event.key == pygame.K_RIGHT:
                lead_x_change = blockSize
                lead_y_change = 0
            elif event.key == pygame.K_UP:
                lead_y_change = -blockSize
                lead_x_change = 0
            elif event.key == pygame.K_DOWN:
                lead_y_change = blockSize
                lead_x_change = 0

    # Defines window boundary
    if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
        gameExit = True 
    
    lead_x += lead_x_change
    lead_y += lead_y_change
    # Defines game background
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,blockSize,blockSize])
    # Updates game display
    pygame.display.update() 
    # Defines game FPS
    clock.tick(FPS)

message_to_screen("You Lose", red)
pygame.display.update() 
time.sleep(2)
pygame.quit()
quit()