import pygame, sys, checkValid, checkWin
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

WINNING_HORIZ = 0

class board: # make this its own file later
    
    boardMatrix = [[0 for x in range(3)] for y in range(3)]

"""

"""
def makeWindow():    
    pygame.display.set_caption('TIC-TAC-TOE')
    drawBoard()
    
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

    gameStart()

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
def drawWinLine(line):    
    if line == 0:
        if PLYR_X == True:
            pygame.draw.line(WINDOW, WHITE, (50, 100), (550, 100), 3)
        elif PLYR_X == False:
            pygame.draw.line(WINDOW, WHITE, (25, 100), (575, 100), 3)
    

"""

"""
def onWin():    
    drawWinLine(WINNING_HORIZ)
    if PLYR_X == True:
        print("X win")
        
    else:
        print("O win")

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
