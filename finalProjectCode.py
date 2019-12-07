#Pygame template -- template for final project
import pygame
import random

pygame.init()

                #----------PICTURES FOR GAME---------------#

menuPicPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\Binns.jpg"
bearcatLogoPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\BearcatLogo.png"
peadPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\Pead.jpg"
pikePath =r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\Pike.jpg"
gameWinPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\GameWin.jpg"
playCall1Path = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\kelly1.jpg"
playCall2Path = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\kelly2.jpg"
PikeToBinnsPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\PikeToBinns.jpg"


menuPic = pygame.image.load(menuPicPath)
bearcatLogo = pygame.image.load(bearcatLogoPath)
peadPic = pygame.image.load(peadPath)
pikePic = pygame.image.load(pikePath)
gameWinPic = pygame.image.load(gameWinPath)
playCall1Pic = pygame.image.load(playCall1Path)
playCall2Pic = pygame.image.load(playCall2Path)
PikeToBinsPic = pygame.image.load(PikeToBinnsPath)


                #----------SOUND FOR GAME---------------#
gameWinningAudioPath = r"C:\\Users\\justi\\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GameWinningAudio.mp3"
fightSongAudioPath = r"C:\\Users\\justi\\Documents\\Python Programming\\Final Project\\Python-Final-Project\\FightSong.mp3"


#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (224,1,34)

#set size of pygame screen
WIDTH = 1150
HEIGHT = 700

framesPerSecond = 50

DownNum = 1
ToGo = 10
BallOn = 37
TimeLeft = 90
midfield = 50
SideOfField = "CIN"
timeoutsLeft = 2
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
    global SideOfField

    x = True
    outcome1 = "Not sure why you're running right now but you gained 4 yards."
    outcome2 = "You got lucky and gained 7 yards!"
    outcome3 = "You fool! Pass the stinking ball! You don't play for the Bengals!"
    outcome4 = "You got back to the line of scrimmage. No gain"
    outcome5 = "You got tripped up and only gained 3 yards. Maybe try passing the ball"
    outcome6 = "Defense wasn't expecting run and you gained 10 yards"
    outcome7 = "You got tackled in the backfield. You lost 3 yards"
    
    possibleOutcomes = [outcome1, outcome2, outcome3, outcome4, outcome5, outcome6, outcome7]
    result = Results(possibleOutcomes)

    if (TimeLeft <= 30 or yardsGained >= 43):
        PikeToBinnsIntro()
    else:
        if result == outcome1:
            DownNum += 1
            ToGo -= 4
            yardsGained += 4
            TimeLeft -= 7

            if BallOn+4 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+4) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 4
            else:
                BallOn += 4


            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        elif result == outcome2:
            DownNum += 1
            ToGo -= 7
            yardsGained += 7
            TimeLeft -= 7

            if BallOn+7 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+7) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 7
            else:
                BallOn += 7


            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        elif result == outcome4:
            DownNum += 1
            TimeLeft -= 3
            if DownNum > 4:
                TurnoverScreen()

        elif result == outcome5:
            DownNum += 1
            ToGo -= 3
            yardsGained += 3
            TimeLeft -= 7

            if BallOn+3 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+3) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 3
            else:
                BallOn += 3


            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        elif result == outcome6:
            DownNum += 1
            ToGo -= 10
            yardsGained += 10
            TimeLeft -= 7

            if BallOn+10 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+10) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 10
            else:
                BallOn += 10

            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        elif result == outcome7:
            DownNum += 1
            ToGo += 3
            yardsGained -= 3
            TimeLeft -= 7

            if BallOn+3 > 50 and SideOfField == "PIT":
                yardsRemaining = (BallOn+3) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "CIN"
            elif yardsGained > 13:
                BallOn += 3
            else:
                BallOn -= 3


            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit


        while x:
            screen.fill(RED)
            screen.blit(peadPic, (325,180))
            if result == outcome1:
                displayText(outcome1,'Limonata', BLACK, 35,WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            elif result == outcome2:
                displayText(outcome2,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            elif result == outcome3:
                displayText(outcome3,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("PASS THE BALL!", 415,115,350,50, BLACK,WHITE,BLACK, passOption)
            elif result == outcome4:
                displayText(outcome4,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            elif result == outcome5:
                displayText(outcome5,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            elif result == outcome6:
                displayText(outcome6,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            else:
                displayText(outcome7,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
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
    global yardsGained
    global SideOfField

    x = True
    outcome1 = "You found an open receiver for a gain of 5 yards!"
    outcome2 = "You found an open receiver for a gain of 3 yards!"
    outcome3 = "You got sacked! Loss of 3 yards!"
    outcome4 = "You threw a deep bomb and connected for a gain of 10 yards"
    outcome5 = "You coudln't find any open receivers but scrambled for 4 yards"
    outcome6 = "Incomplete Pass. No gain"
    outcome7 = "You threw a passs right on target for a gain of 7 yards"
    possibleOutcomes = [outcome1, outcome2, outcome3, outcome4, outcome5, outcome6, outcome7]
    result = Results(possibleOutcomes)

    if (TimeLeft <= 30 or yardsGained >= 33):
        PikeToBinnsIntro()
    else:

        if result == outcome1:
            DownNum += 1
            ToGo -= 5
            yardsGained += 5
            TimeLeft -= 7

            if BallOn+5 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+5) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 5
            else:
                BallOn += 5


            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        elif result == outcome2:
            DownNum += 1
            ToGo -= 3
            yardsGained += 3
            TimeLeft -= 7

            if BallOn+3 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+3) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 3
            else:
                BallOn += 3

            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        elif result == outcome3:
            DownNum += 1
            ToGo += 3
            yardsGained -= 3
            TimeLeft -= 7

            if BallOn+3 > 50 and SideOfField == "PIT":
                yardsRemaining = (BallOn+3) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "CIN"
            elif yardsGained > 13:
                BallOn += 3
            else:
                BallOn -= 3

            if DownNum > 4:
                TurnoverScreen()

        elif result == outcome4:
            DownNum += 1
            ToGo -= 10
            yardsGained += 10
            TimeLeft -= 12

            if BallOn+10 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+10) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 10
            else:
                BallOn += 10

            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()
        
        elif result == outcome5:
            DownNum += 1
            ToGo -= 4
            yardsGained += 4
            TimeLeft -= 7

            if BallOn+4 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+5) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 4
            else:
                BallOn += 4


            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        elif result == outcome6:
            DownNum += 1
            TimeLeft -= 7

            if DownNum > 4:
                TurnoverScreen()

        else:
            DownNum += 1
            ToGo -= 7
            yardsGained += 7
            TimeLeft -= 7

            if BallOn+7 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+7) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 7
            else:
                BallOn += 7


            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        while x:
            screen.fill(RED)
            screen.blit(pikePic, (325,140))
            if result == outcome1:
                displayText(outcome1,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            elif result == outcome2:
                displayText(outcome2,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            elif result == outcome3:
                displayText(outcome3,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415, 550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            elif result == outcome4:
                displayText(outcome4,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            elif result == outcome5:
                displayText(outcome5,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            elif result == outcome6:
                displayText(outcome6,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            else:
                displayText(outcome7,'Limonata', BLACK, 35, WIDTH, HEIGHT/4)
                buttons("NEXT PLAY", 415,550,350,50, BLACK,WHITE,BLACK, playcallScreen)
            pygame.display.update()
            clock.tick(framesPerSecond)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit

def getSuffix(currentDown):
    if currentDown == 1:
        return "st"
    elif currentDown == 2:
        return "nd"
    elif currentDown == 3:
        return "rd"
    else: 
        return "th"

def playcallScreen():
    pygame.mixer.music.stop()
    x = True
    if yardsGained < 13:
        message = "Down: " + str(DownNum) + getSuffix(DownNum) + " and " + str(ToGo) + "               " + "Ball on: " + str(SideOfField) + " " + str(BallOn) + "               " + "Time left: " + str(TimeLeft) + " seconds"
    elif yardsGained == 13:
        message = "Down: " + str(DownNum) + getSuffix(DownNum) + " and " + str(ToGo) + "               " + "Ball on: " + str(SideOfField) + "               " + "Time left: " + str(TimeLeft) + " seconds"
    else:
        message = "Down: " + str(DownNum) + getSuffix(DownNum) + " and " + str(ToGo) + "               " + "Ball on: " + str(SideOfField) + " " +  str(BallOn) + "           " + "Time left: " + str(TimeLeft) + " seconds"
    playcallImage = Results([playCall1Pic, playCall2Pic])
    while x:
        screen.fill(RED)
        if playcallImage == playCall2Pic:
            screen.blit(playcallImage, (285,280))
        else:
            screen.blit(playcallImage, (350,280))
        if timeoutsLeft > 0:
            displayText(message,'Limonata',BLACK,35,1155,225)
            buttons("PASS", 250,175,150,75,BLACK,WHITE,BLACK, passOption)
            buttons("RUN", 450,175,150,75,BLACK,WHITE,BLACK, runOption)
            buttons("TIMEOUT", 650,175,150,75,BLACK,WHITE,BLACK, timeoutScreen)
            pygame.display.update()
            clock.tick(framesPerSecond)
        else:
            displayText(message,'Limonata',BLACK,35,1155,225)
            buttons("PASS", 400,175,150,75,BLACK,WHITE,BLACK, passOption)
            buttons("RUN", 600,175,150,75,BLACK,WHITE,BLACK, runOption)
            pygame.display.update()
            clock.tick(framesPerSecond)



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

def timeoutScreen():
    global timeoutsLeft
    x = True
    timeoutsLeft -= 1
    message = "You called a timeout! You have " + str(timeoutsLeft) + " timeout left."
    while x:
        screen.fill(BLACK)
        displayText(message, "Limonata", RED, 35, WIDTH, HEIGHT)
        buttons("GOT IT! NEXT PLAY", 415,470,350,50, RED,WHITE,RED, playcallScreen)
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
        screen.blit(playCall1Pic, (420,180))
        displayText(message,'Limonata',BLACK,35,1155,225)
        buttons("PLAY AGAIN", 65, 300, 250, 75, BLACK, WHITE, BLACK, gameMenu)
        buttons("QUIT", 845, 300, 250, 75, BLACK, WHITE, BLACK, quit)
        pygame.display.update()
        clock.tick(framesPerSecond)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

def PikeToBinnsIntro():
    message = "The time has come. You see Armon Binns streaking down the right side of the field.\n\nLet the ball fly and listen to Dan Hoard make the call to see if you won the game!"
    PikeToBinnsFont = pygame.font.SysFont('Times New Roman', 23)
    PikeToBinnsFont.set_bold(True)
    x = True
    while x:
        screen.fill(BLACK)
        screen.blit(PikeToBinsPic, (255,190))
        blit_text(screen, message, (80,70), PikeToBinnsFont)
        buttons("LET IT RIP!",385,570,350,50, RED, WHITE, RED, PikeToBinns)
        pygame.display.update()
        clock.tick(framesPerSecond)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit


def PikeToBinns():
    x = True
    gameWinningSound = pygame.mixer.music.load(gameWinningAudioPath)
    pygame.mixer.music.play(0)

    while x:
        screen.fill(BLACK)
        displayText("YOU WON!", "Limonata", RED, 55, 1150,200)
        screen.blit(gameWinPic, (322,190))
        buttons("QUIT", 50,300,250,75, RED,WHITE,RED, quit)
        buttons("PLAY AGAIN", 850,300,250,75, RED,WHITE,RED, gameMenu)
        pygame.display.update()
        clock.tick(framesPerSecond)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

#function to display game menu
def gameMenu():
    resetGame()
    fightSongSound = pygame.mixer.music.load(fightSongAudioPath)
    pygame.mixer.music.play(0)
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
    global timeoutsLeft
    global TimeLeft
    global yardsGained
    global SideOfField

    DownNum = 1
    ToGo = 10
    BallOn = 37
    timeoutsLeft = 2
    TimeLeft = 90
    yardsGained = 0
    SideOfField = "CIN"

def gameLoop():
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
        buttons("GOT IT! LET'S GO!",385,570,350,50, RED, WHITE, RED, playcallScreen)
        pygame.display.update()
        clock.tick(framesPerSecond)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

    #close the game
    pygame.quit()
    quit

gameMenu()