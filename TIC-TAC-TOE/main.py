import pygame, sys, checkValid, checkWin, time
from pygame.locals import *

pygame.init()

"""

"""

WIN_H = 700
WIN_W = 600
PLYR_X = True

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
    boardMatrix = [[0 for x in range(3)] for y in range(3)]
    for i in range(0, 3):
        print(boardMatrix[i][0])

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
    x = 0
    if WINNING == 1:
        x = 200
    elif WINNING == 2:
        x = 400
        
    if PLYR_X == True:
        if WIN_TYPE == 0:
            pygame.draw.line(WINDOW, WHITE, (25, 25), (575, 575), 3)
        elif WIN_TYPE == 1:
            pygame.draw.line(WINDOW, WHITE, (575, 25), (25, 575), 3)            
        elif WIN_TYPE == 2:
            pygame.draw.line(WINDOW, WHITE, (50, 100+x), (550, 100+x), 3)
        else:
            pygame.draw.line(WINDOW, WHITE, (100+x, 50), (100+x, 550), 3)

    elif PLYR_X == False:
        if WIN_TYPE == 0:
            pygame.draw.line(WINDOW, WHITE, (25, 25), (575, 575), 3)
        elif WIN_TYPE == 2:
            pygame.draw.line(WINDOW, WHITE, (25, 100+x), (575, 100+x), 3)
        else:
            pygame.draw.line(WINDOW, WHITE, (100+x, 25), (100+x, 575), 3)   
        
    pygame.display.update()
    
"""

"""
def onWin():    
    drawWinLine()
    pauseGame(2)
    print("hello")
    gameReset()
    
"""

"""
def pauseGame(x):
    pygame.time.delay(x*1000)
    

def gameReset():
    print("yo")
    drawBoard()
    newBoard()
    WINNING = 0
    WIN_TYPE = 0    
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
                    print(str(pygame.mouse.get_pos()))
                    checkValid.checkValidClick(pygame.mouse.get_pos())
                    
        pygame.display.update()

################################################################################

makeWindow()
