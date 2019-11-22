#Pygame template -- template for final project
import pygame
import random

pygame.init()

                #----------PICTURES FOR GAME---------------#



                #----------SOUND FOR GAME---------------#

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (224,1,34)
GREEN = (0,255,0)
BLUE = (0,0,255)

#set size of pygame screen
WIDTH = 1150
HEIGHT = 700


framesPerSecond = 50

#font

#Function which allows for multiline text wrapping with pygame
def blit_text(surface, text, pos, font, color=RED):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

#function to display game menu
def gameMenu():
    intro = True
    while intro:
        screen.fill(RED)
        pygame.display.update()
        clock.tick(framesPerSecond)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                intro = False

text = "It's December 5, 2009 and your beloved University of Cincinnati Bearcats are taking on the University of Pittsburgh Panthers.\n\nThe winner clinches the conference championship.\n\nThe Bearcats have a shot at playing inthe national championship with a win.\n\nHowever, the game starts out rough and the Bearcats are down 31-17 at haltime.\n\nAfter making some halftime adjustments, you come out strong in the second half and manage to tie the game up 38-38 at halftime.\n\nUnfortunately, Pittsburgh scores a touchdown late and manages to take the lead.\n\nBUT THEY MISS THE TWO POINT CONVERSION!\n...................................................................................................................................................\nThere's 1:30 left in the game and you have the ball on your own 39 yard line with 2 timeouts left.\n\nCan you drive down the field and score the game winning touchdown and give the Bearcats a chance to play in the national championship game?"
instructionFont = pygame.font.SysFont('Times New Roman', 18)
instructionFont.set_bold(True)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((50,50))
        self.image.fill(RED)
        self.rect =  self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT/2)

    def update(self):
        self.rect.x += 10
        if self.rect.x > WIDTH:
            self.rect.right = 0

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect =  self.image.get_rect()
        self.rect.left, self.rect.top = location

#initialize game and display the window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game Winning Drive")
clock = pygame.time.Clock()

allSprites = pygame.sprite.Group()
playerObject = Player()
allSprites.add(playerObject)

#variable to keep game running
gameRunning = True

gameMenu()


#game loop
while gameRunning:
    #keep the game running at the right speed
    clock.tick(framesPerSecond)
    screen.fill(BLACK)
    blit_text(screen, text, (20,100), instructionFont)
    for event in pygame.event.get():
        #check for close window
        if event.type == pygame.QUIT:
            gameRunning = False
    
    #allSprites.update()
    #allSprites.draw(screen)
    pygame.display.flip()

#close the game
pygame.quit()