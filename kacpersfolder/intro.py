"""
Intro for the TIC-TAC-TOE game for our ALL Project 
"""
import pygame, sys
from pygame.locals import *

#variables
screenWidth = 480
screenHeight = 380
centerW = (screenWidth/2) - 80

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        screen.blit(self.rend, self.rect)
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, 1, self.textcol())
        
    def textcol(self):
        if self.hovered:
            return (255, 255, 255)
        else:
            return (100, 100, 100)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos

pygame.init()
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption('TIC-TAC-TOE')
menu_font = pygame.font.Font(None, 40)
options = [Option("Single-Player", (centerW, 110)), Option("Multi-Player", (centerW, 160)), Option("VS Computer", (centerW, 210))]

while True:
    pygame.event.pump()
    screen.fill((0, 0, 0))
    for option in options:
        if option.rect.collidepoint(pygame.mouse.get_pos()):
            option.hovered = True
        else:
            option.hovered = False
        option.draw()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()   
    pygame.display.update()
