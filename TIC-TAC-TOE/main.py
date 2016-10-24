import pygame, sys
from pygame.locals import *

pygame.init()

#defining some constants

WIN_H = 600
WIN_W = 700
CURRENT_PLYR = 'X'

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)

WINDOW = pygame.display.set_mode((WIN_H, WIN_W), 0, 32)
CHAR_FONT = pygame.font.SysFont("monospace", 200)
TEXT_FONT = pygame.font.SysFont("monospace", 12)

class board: # make this its own file later
    
    boardMatrix = [[0 for x in range(3)] for y in range(3)]


def makeWindow():    
    pygame.display.set_caption('TIC-TAC-TOE')
    drawBoard()

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

def checkValidClick():
    
    x, y = pygame.mouse.get_pos()
    
    if x < 200 and y < 200:       
        if board.boardMatrix[0][0] == 0:            
            drawX(40, -10)
            board.boardMatrix[0][0] = 1        
        
    elif x < 400 and y < 200:
        if board.boardMatrix[1][0] == 0: 
            drawX(240, -10)
            board.boardMatrix[1][0] = 1
        
    elif x < 600 and y < 200:
        if board.boardMatrix[2][0] == 0: 
            drawX(440, -10)
            board.boardMatrix[2][0] = 1

    elif x < 200 and y < 400:
        if board.boardMatrix[0][1] == 0: 
            drawX(40, 190)
            board.boardMatrix[0][1] = 1

    elif x < 400 and y < 400:
        if board.boardMatrix[1][1] == 0: 
            drawX(240, 190)
            board.boardMatrix[1][1] = 1

    elif x < 600 and y < 400:
        if board.boardMatrix[2][1] == 0: 
            drawX(440, 190)
            board.boardMatrix[2][1] = 1

    elif x < 200 and y < 600:
        if board.boardMatrix[0][2] == 0: 
            drawX(40, 390)
            board.boardMatrix[0][2] = 1

    elif x < 400 and y < 600:
        if board.boardMatrix[1][2] == 0: 
            drawX(240, 390)
            board.boardMatrix[1][2] = 1

    elif x < 600 and y < 600:
        if board.boardMatrix[2][2] == 0: 
            drawX(440, 390)
            board.boardMatrix[2][2] = 1
        
    

def drawX(a, b):
    
    drawXCHAR = CHAR_FONT.render("X", True, WHITE) 
    WINDOW.blit(drawXCHAR, (a, b))       

def gameStart():
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONUP:
                checkValidClick()
                    
        pygame.display.update()

################################################################################

makeWindow()
