#Pygame template -- template for final project
import pygame
import random
import time

pygame.init()

                #----------PICTURES FOR GAME---------------#
menuPic = pygame.image.load(r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\Binns.jpg")
bearcatLogo = pygame.image.load(r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\BearcatLogo.png")


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

DownNum = 1
ToGo = 10
BallOn = 37
TimeLeft = 90
midfield = 50
yardsGained = 0


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


#function to display text
def displayText(message, font, color, fontSize, locationX, locationY):
    text = pygame.font.SysFont('Limonata', fontSize)
    text.set_bold(True)
    text.set_italic(True)
    textSurf = text.render(message, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (locationX/2,locationY/2)
    screen.blit(textSurf,textRect)

#function to implement use of buttons in pygame
def buttons(msg, btnX, btnY, buttonWidth, buttonHeight, inactiveColor, activeColor, activeTextColor, action=None):
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()

        buttonFont = pygame.font.SysFont('Limonata', 35)
        buttonFont.set_bold(True)
        buttonText = buttonFont.render(msg, True, WHITE)
        buttonTextRect = buttonText.get_rect()
        buttonTextRect.center = ((btnX+(buttonWidth/2)),(btnY+(buttonHeight/2)))
        screen.blit(buttonText,buttonTextRect)

        if btnX+buttonWidth > mouse [0] > btnX and btnY+buttonHeight > mouse[1] > btnY:
              pygame.draw.rect(screen, activeColor, (btnX,btnY,buttonWidth,buttonHeight))
              buttonText = buttonFont.render(msg, True, activeTextColor)
              screen.blit(buttonText,buttonTextRect)
              if mouseClick[0] == 1 and action != None:
                  action()
        else:
            pygame.draw.rect(screen, inactiveColor, (btnX,btnY,buttonWidth,buttonHeight))
            screen.blit(buttonText,buttonTextRect)

#takes list as argument and returns a random list element
def Results(lst):
    return random.choice(lst)

#If the user selects run
def runOption():

    global ToGo
    global DownNum
    global BallOn
    global TimeLeft
    global yardsGained

    x = True
    outcome1 = "Not sure why you're running right now but you gained 4 yards."
    outcome2 = "You got lucky and gained 10 yards!"
    outcome3 = "You fool! Pass the stinking ball! You lost 3 yards!"
    outcome4 = "You got back to the line of scrimmage. No gain"
    
    possibleOutcomes = [outcome1, outcome2, outcome3, outcome4]
    result = Results(possibleOutcomes)

    if result == outcome1:
        DownNum += 1
        ToGo -= 4
        BallOn += 4
        yardsGained += 4


        if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
            DownNum = 1
            ToGo = 10
        elif DownNum > 4 and ToGo > 0:
           TurnoverScreen()
    if result == outcome2:
        DownNum += 1
        ToGo -= 10
        BallOn += 10
        yardsGained += 10
        if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
            DownNum = 1
            ToGo = 10
        elif DownNum > 4 and ToGo > 0:
            TurnoverScreen()
    if result == outcome3:
        DownNum += 1
        ToGo += 3
        BallOn -= 3
        yardsGained -= 3
        if DownNum > 4:
           TurnoverScreen()
    if result == outcome4:
        DownNum += 1
        if DownNum > 4:
            TurnoverScreen()

    while x:
        screen.fill(BLACK)
        if result == outcome1:
            screen.fill(RED)
            displayText(outcome1,'Limonata', BLACK, 35,WIDTH, HEIGHT)
            buttons("NEXT PLAY", 415,470,350,50, BLACK,WHITE,BLACK, screen1)
        if result == outcome2:
            screen.fill(RED)
            displayText(outcome2,'Limonata', BLACK, 35, WIDTH, HEIGHT)
            buttons("NEXT PLAY", 415,470,350,50, BLACK,WHITE,BLACK, screen1)
        if result == outcome3:
            screen.fill(RED)
            displayText(outcome3,'Limonata', BLACK, 35, WIDTH, HEIGHT)
            buttons("NEXT PLAY", 415,470,350,50, BLACK,WHITE,BLACK, screen1)
        if result == outcome4:
            screen.fill(RED)
            displayText(outcome4,'Limonata', BLACK, 35, WIDTH, HEIGHT)
            buttons("NEXT PLAY", 415,470,350,50, BLACK,WHITE,BLACK, screen1)
        pygame.display.update()
        clock.tick(framesPerSecond)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

#if the user selects pass
def passOption():

    global ToGo
    global DownNum
    global BallOn
    global TimeLeft

    x = True
    outcome1 = "You threw a deep pass and it fell incomplete. No gain."
    outcome2 = "You found an open receiver for a gain of 5 yards!"
    outcome3 = "You got sacked! Loss of 5 yards!"
    outcome4 = "You threw a deep bomb and connected for a gain of 20 yards"
    possibleOutcomes = [outcome1, outcome2, outcome3, outcome4]
    result = Results(possibleOutcomes)

    if result == outcome1:
        ToGo -= 4
    if result == outcome2:
        ToGo -= 4
    if result == outcome3:
        ToGo -= 4
    if result == outcome4:
        ToGo -= 4

    while x:
        screen.fill(BLACK)
        if result == outcome1:
            screen.fill(RED)
            displayText(outcome1,'Limonata', BLACK, 35, WIDTH, HEIGHT)
            buttons("NEXT PLAY", 415,470,350,50, BLACK,WHITE,BLACK, screen1)
        if result == outcome2:
            screen.fill(RED)
            displayText(outcome2,'Limonata', BLACK, 35, WIDTH, HEIGHT)
            buttons("NEXT PLAY", 415,470,350,50, BLACK,WHITE,BLACK, screen1)
        if result == outcome3:
            screen.fill(RED)
            displayText(outcome3,'Limonata', BLACK, 35, WIDTH, HEIGHT)
            buttons("NEXT PLAY", 415,470,350,50, BLACK,WHITE,BLACK, screen1)
        if result == outcome4:
            screen.fill(RED)
            displayText(outcome4,'Limonata', BLACK, 35, WIDTH, HEIGHT)
            buttons("NEXT PLAY", 415,470,350,50, BLACK,WHITE,BLACK, screen1)
        pygame.display.update()
        clock.tick(framesPerSecond)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

def screen1():
    x = True
    if yardsGained < 13:
        message = "Down: " + str(DownNum) + "st and " + str(ToGo) + "               " + "Ball on: CIN " + str(BallOn) + "               " + "Time left: " + str(TimeLeft) + " seconds"
    elif yardsGained == 13:
        message = "Down: " + str(DownNum) + "st and " + str(ToGo) + "               " + "Ball on: " + str(BallOn) + "               " + "Time left: " + str(TimeLeft) + " seconds"
    else:
        message = "Down: " + str(DownNum) + "st and " + str(ToGo) + "               " + "Ball on: PIT " + str(BallOn) + "               " + "Time left: " + str(TimeLeft) + " seconds"
    while x:
        screen.fill(RED)
        displayText(message,'Limonata',BLACK,35,1155,225)
        buttons("PASS", 150,250,150,150,BLACK,WHITE,BLACK, passOption)
        buttons("RUN", 850,250,150,150,BLACK,WHITE,BLACK, runOption)
        pygame.display.update()
        clock.tick(framesPerSecond)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit


def TurnoverScreen():
    x = True
    message = "YOU TURNED THE BALL OVER ON DOWNS! YOU LOST THE GAME!    "
    while x:
        screen.fill(RED)
        displayText(message,'Limonata',BLACK,35,1155,225)
        buttons("PLAY AGAIN", 150,250,250,150,BLACK,WHITE,BLACK, gameMenu)
        buttons("QUIT", 550,150,150,150,BLACK,WHITE,BLACK, quit)
        pygame.display.update()
        clock.tick(framesPerSecond)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
                print("PENIS")

#function to display game menu
def gameMenu():
    intro = True

    font = pygame.font.SysFont('Limonata', 50)
    font.set_bold(True)
    font.set_italic(True)
    menuText = font.render("BEARCATS",True, RED)
    menuText.get_rect()
    menuTextRect = menuText.get_rect()
    menuTextRect.center = (WIDTH/2,HEIGHT/8)

    while intro:
        screen.fill(BLACK)
        buttons("ONWARDS TO VICTORY!", 415,470,350,50, RED, WHITE, RED, gameLoop)
        screen.blit(menuText,menuTextRect)
        screen.blit(menuPic, (325,130))
        screen.blit(bearcatLogo, (40,170))
        screen.blit(bearcatLogo, (870,170))
        pygame.display.update()
        clock.tick(framesPerSecond)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

#initialize game and display the window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game Winning Drive")
clock = pygame.time.Clock()

def resetGame():
    global DownNum
    global ToGo 
    global BallOn
    global TimeLeft
    global yardsGained
    DownNum = 1
    ToGo = 10
    BallOn = 37
    TimeLeft = 90
    yardsGained = 0

def gameLoop():
    resetGame()
#game loop
    text = "It's December 5, 2009 and your beloved University of Cincinnati Bearcats are taking on the University of Pittsburgh Panthers.\n\nThe winner clinches the conference championship.\n\nThe Bearcats have a shot at playing inthe national championship with a win.\n\nHowever, the game starts out rough and the Bearcats are down 31-17 at haltime.\n\nAfter making some halftime adjustments, you come out strong in the second half and manage to tie the game up 38-38 at halftime.\n\nUnfortunately, Pittsburgh scores a touchdown late and manages to take the lead.\n\nBUT THEY MISS THE TWO POINT CONVERSION!\n...................................................................................................................................................\nThere's 1:30 left in the game and you have the ball on your own 39 yard line with 2 timeouts left.\n\nCan you drive down the field and score the game winning touchdown and give the Bearcats a chance to play in the national championship game?"
    instructionFont = pygame.font.SysFont('Times New Roman', 18)
    instructionFont.set_bold(True)

    #variable to keep game running
    gameRunning = True
    while gameRunning:
        #keep the game running at the right speed
        screen.fill(BLACK)
        blit_text(screen, text, (20,100), instructionFont)
        buttons("GOT IT! LET'S GO!",385,570,350,50, RED, WHITE, RED, screen1)
        pygame.display.update()
        clock.tick(framesPerSecond)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

    #close the game
    pygame.quit()
    quit

gameMenu()
#TurnoverScreen()