import pygame

# Starts game 
pygame.init()

white = (255,255,255)
black = (0,0,0)

# Game display window 
gameDisplay = pygame.display.set_mode((800,600))

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

    
    lead_x += lead_x_change
    lead_y += lead_y_change
    # Defines game background
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
    # Updates game display
    pygame.display.update() 
    # Defines game FPS
    clock.tick(15)


pygame.quit()
quit()