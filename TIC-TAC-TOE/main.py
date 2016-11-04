import pygame, sys, checkValid, checkWin, time 
from pygame.locals import *

pygame.init()

"""

"""

WIN_H = 700
WIN_W = 600
PLYR_X = True

VALID_CLICKS = 0

X_WINS = 0
O_WINS = 0

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)

WINDOW = pygame.display.set_mode((WIN_W, WIN_H), 0, 32)
CHAR_FONT_X = pygame.font.SysFont("monospace", 200)
CHAR_FONT_O = pygame.font.SysFont("monospace", 275)
TEXT_FONT = pygame.font.SysFont("monospace", 12)

WINNING = 0
WIN_TYPE = 0

boardMatrix = [[0 for x in range(3)] for y in range(3)]

def newBoard():
    global boardMatrix    
    boardMatrix = [[0 for x in range(3)] for y in range(3)]
    

"""

"""
def makeWindow():    
    pygame.display.set_caption('TIC-TAC-TOE')
    newBoard()
    drawBoard()
    gameStart()
    
"""
This function draws the main screen, fills the background black:
"""
def drawBoard():
    
    WINDOW.fill(BLACK)
    
    pygame.draw.line(WINDOW, WHITE, (1, 0), (1, 699), 3)  # left
    pygame.draw.line(WINDOW, WHITE, (0, 1), (600, 1), 3)  # top
    pygame.draw.line(WINDOW, WHITE, (598, 0), (598, 699), 3)  # right
    pygame.draw.line(WINDOW, WHITE, (0, 598), (598, 598), 3)  # bottom

    pygame.draw.line(WINDOW, WHITE, (0, 197), (600, 197), 3)  # H1
    pygame.draw.line(WINDOW, WHITE, (0, 397), (600, 397), 3)  # H2
    pygame.draw.line(WINDOW, WHITE, (0, 698), (600, 698), 3)  # H3

    pygame.draw.line(WINDOW, WHITE, (197, 0), (197, 599), 3)  # V1
    pygame.draw.line(WINDOW, WHITE, (397, 0), (397, 599), 3)  # V2

"""

"""
def drawX(a, b):
    drawXCHAR = CHAR_FONT_X.render("X", True, WHITE)
    WINDOW.blit(drawXCHAR, (a, b))

"""

"""
def drawO(a, b):
    drawOCHAR = CHAR_FONT_O.render("o", True, WHITE)
    WINDOW.blit(drawOCHAR, (a, b))

"""

"""
def drawWinLine():
    x = (int(WINNING)*200)
        
    if PLYR_X == True:
        if WIN_TYPE == 0:
            pygame.draw.line(WINDOW, WHITE, (25, 25), (575, 575), 3)
        elif WIN_TYPE == 1:
            pygame.draw.line(WINDOW, WHITE, (575, 25), (25, 575), 3)            
        elif WIN_TYPE == 2:
            pygame.draw.line(WINDOW, WHITE, (50, 100+x), (550, 100+x), 3)
        elif WIN_TYPE == 3:
            pygame.draw.line(WINDOW, WHITE, (100+x, 50), (100+x, 550), 3)

    elif PLYR_X == False:
        if WIN_TYPE == 0:
            pygame.draw.line(WINDOW, WHITE, (25, 25), (575, 575), 3)
        elif WIN_TYPE == 1:
            pygame.draw.line(WINDOW, WHITE, (575, 25), (25, 575), 3)
        elif WIN_TYPE == 2:
            pygame.draw.line(WINDOW, WHITE, (25, 100+x), (575, 100+x), 3)
        elif WIN_TYPE == 3:
            pygame.draw.line(WINDOW, WHITE, (100+x, 25), (100+x, 575), 3)        
        
    pygame.display.update()
    
"""

"""
def onWin():
    drawWinLine()
    pauseGame(2)
    gameReset()
    
"""
This function uses PyGame's in-built delay function to cause a delay when needed.
In the context of the game it's used to pause the game on a win to let the player
see who won and gives a little break between rounds.
"""
def pauseGame(x):
    pygame.time.delay(x*1000)

"""
This function swaps the player between X and O every time it is called. Also the
amount of valid clicks increments by 1 when it's called as to swap a player it
must have been a valid move to start with. (Used for the draw condition)
"""
def swapPlayer():
    global PLYR_X, VALID_CLICKS
    PLYR_X = not PLYR_X
    VALID_CLICKS += 1

"""
This function resets all the variables that need to be reset when the game runs again.
For example the 
"""
def resetVars():
    global WINNING, WIN_TYPE, VALID_CLICKS
    WINNING = 0
    WIN_TYPE = 0
    VALID_CLICKS = 0

"""
This function is called when a win or draw has occured. It then runs all the functions
in main that handle the resetting of the game in order for it to work again as if it
has never been run before.
"""
def gameReset():
    swapPlayer()
    drawBoard()
    resetVars()
    newBoard()   
    gameStart()
    
"""

"""
def gameStart():
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    checkValid.checkValidClick(pygame.mouse.get_pos())
                    
        pygame.display.update()

################################################################################

makeWindow()
