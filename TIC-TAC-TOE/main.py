import pygame, sys
from pygame.locals import *

pygame.init()

#defining some constants

WIN_H = 600
WIN_W = 700

BLACK = (0,   0,   0)
WHITE = (255, 255, 255)

WINDOW = pygame.display.set_mode((WIN_H, WIN_W), 0, 32)
CHAR_FONT = pygame.font.SysFont("monospace", 200)
TEXT_FONT = pygame.font.SysFont("monospace", 12)

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

def drawX(COORD):
    X = CHAR_FONT.render("X", True, WHITE)
    WINDOW.blit(X, COORD)

def gameStart():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONUP:
                drawX(pygame.mouse.get_pos())
                    
        pygame.display.update()

################################################################################

makeWindow()
