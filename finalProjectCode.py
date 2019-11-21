#Pygame template -- template for final project
import pygame
import random


#set size of pygame screen
WIDTH = 500
HEIGHT = 500

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

framesPerSecond = 50

#initialize pygame and display the window
pygame.init()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Final Project")
clock = pygame.time.Clock()

#Game loop
gameRunning = True

while gameRunning:

    for event in pygame.event.get():
        #check for close window
        if event.type == pygame.QUIT:
            gameRunning = False
    screen.fill(RED)
    pygame.display.flip()

#close the game
pygame.quit()