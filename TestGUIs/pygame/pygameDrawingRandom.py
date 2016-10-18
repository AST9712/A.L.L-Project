import pygame, sys
from pygame.locals import *

pygame.init()

# set up the window
DISPLAYSURF = pygame.display.set_mode((600, 600), 0, 32)
pygame.display.set_caption('Drawing')

# set up the colors
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)

# font
myfont = pygame.font.SysFont("monospace", 200)

# draw on the surface object
DISPLAYSURF.fill(BLACK)

pygame.draw.line(DISPLAYSURF, WHITE, (1, 0), (1, 600), 3)  # left
pygame.draw.line(DISPLAYSURF, WHITE, (0, 1), (600, 1), 3)  # top
pygame.draw.line(DISPLAYSURF, WHITE, (598, 0), (598, 600), 3)  # right
pygame.draw.line(DISPLAYSURF, WHITE, (0, 598), (598, 598), 3)  # bottom

pygame.draw.line(DISPLAYSURF, WHITE, (0, 197), (600, 197), 3)  # H1
pygame.draw.line(DISPLAYSURF, WHITE, (0, 397), (600, 397), 3)  # H2

pygame.draw.line(DISPLAYSURF, WHITE, (197, 0), (197, 600), 3)  # V1
pygame.draw.line(DISPLAYSURF, WHITE, (397, 0), (397, 600), 3)  # V2

label = myfont.render("X", 1, WHITE)
DISPLAYSURF.blit(label, (40, -10))

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
