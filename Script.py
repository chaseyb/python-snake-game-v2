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
centerDisplayWidth = displayWidth / 2
centerDisplayHeight = displayHeight / 2

# Game speed
FPS = 13

# Game variables
randAppleX, randAppleY = (0,) * 2
goldenApple = random.randint(1, 10) == 10

# Importing images
snakeHeadImage = pygame.image.load("images/SnakeHead.png")
snakeBodyImage = pygame.image.load("images/SnakeBody.png")
appleImage = pygame.image.load("images/Apple.png")
goldenAppleImage = pygame.image.load("images/GoldenApple.png")
icon = pygame.image.load("images/Icon.png")

# Importing font
bodyFont = pygame.font.SysFont("comicsansms", 50)
buttonFont = pygame.font.SysFont("comicsansms", 25)

# Game display window 
gameDisplay = pygame.display.set_mode((displayWidth, displayHeight))
pygame.display.set_caption("Snake")
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

startButton = Button.button(green, lightGreen, gameDisplay, "START", centerDisplayWidth - (buttonWidth / 2),
                            centerDisplayHeight - 30, buttonWidth, buttonHeight, white, -30, centerDisplayWidth,
                            centerDisplayHeight, buttonFont)

quitButton = Button.button(red, lightRed, gameDisplay, "QUIT", centerDisplayWidth - (buttonWidth / 2),
                           centerDisplayHeight + 50, buttonWidth, buttonHeight, white, 50, centerDisplayWidth,
                           centerDisplayHeight, buttonFont)

# High score loading
try:
    with open('score.dat', 'rb') as file:
        highScore = pickle.load(file)
except:
    highScore = 0
    with open('score.dat', 'wb') as file:
        pickle.dump(highScore, file)

def startScreen():
    """
    This function loads the start screen of the game.
    :return:
    """
    while True:
        fillBackground(True)
        put_message_custom("Welcome to Snake!", green, -80)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                quitProgram()

        startButton.showButton()
        quitButton.showButton()

        if startButton.isHovered(getCursorPos()) and isLeftMouseClicked():
            reset()
            return
        elif quitButton.isHovered(getCursorPos()) and isLeftMouseClicked():
            quitProgram()

        pygame.display.update()


def showScores(score, new):
    """
    This function displays the scores on the display.
    :param score:
    :param new:
    :return:
    """
    screen_text = pygame.font.SysFont("comicsansms", 15).render("Score: " + str(score), True, black)
    gameDisplay.blit(screen_text, (displayWidth - scoreOffsetX, scoreOffsetY + 20))

    high_score = pygame.font.SysFont("comicsansms", 15).render("High Score: " + str(highScore), True, black)

    if new:
        high_score = pygame.font.SysFont("comicsansms", 13).render("New High Score!", True, red)

    gameDisplay.blit(high_score, (displayWidth - scoreOffsetX, scoreOffsetY))

def randomApple():
    """
    This function handles the random apple generation.
    :return:
    """
    global randAppleX
    global randAppleY
    global goldenApple

    lastAppleX = randAppleX
    lastAppleY = randAppleY

    goldenApple = generateGoldenApple()

    randAppleX = round(random.randint(blockSize * 2, boundX - (blockSize * 4)) / blockSize) * blockSize
    randAppleY = round(random.randint(blockSize * 2, boundY - (blockSize * 4)) / blockSize) * blockSize

    while [randAppleX, randAppleY] in snakeList or randAppleX == lastAppleX or randAppleY == lastAppleY or \
            (randAppleX >= scoreBoundWidth and randAppleY <= scoreBoundHeight):
        # if the apple generates under the snake or within the high score box, regenerate it
        randAppleX = round(random.randint(blockSize * 2, boundX - scoreBoundWidth - (blockSize * 4)) / blockSize) * \
                     blockSize
        randAppleY = round(random.randint(blockSize * 2, boundY - scoreBoundHeight - (blockSize * 4)) / blockSize) * \
                     blockSize

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