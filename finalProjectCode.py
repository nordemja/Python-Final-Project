"""'
Name: Justin Nordeman
Email: nordemja@mail.uc.edu

Project Title: Game Winning Drive

Description: This project is a game that was developed for my final project
             for my python progamming class, CS2021, at the University of 
             Cincinnati. j

Developer: Justin Nordeman

"""

import pygame
import random

pygame.init()

""" 
CREDIT FOR IMAGE AND AUDIO FILES:

BRIAN KELLY WITH TONY PIKE AND MARTY GILLYARD: https://www.gannett-cdn.com/presto/2019/05/06/PCIN/c43f2f35-82e5-412d-a937-b97d340991c1-1205_UC_PITT-55.jpg?width=2560
BRIAN KELLY IN SNOW: https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTVGCiiAv6a9jSFWQh4gKuaqNBv-36igVrzhfdQuMUe5PjKiUq16A&s
MENU IMAGE: data: https://s3media.247sports.com/Uploads/Assets/629/197/9197629.jpg
ISIAH PEAD: https://gobearcats.com/images/2017/8/29/isaiah_pead_111616_getty_ftr_jxzilqiauwbt1wjswozryrph1.jpg?width=1023&quality=80&format=jpg .
TONY PIKE PASSING: https://cdn.theathletic.com/app/uploads/2019/07/23232133/GettyImages-94023308.jpg
ARMON BINNS CATHCING FOOTBALL: https://theamerican.org/images/2019/9/4/CINCINNATI_BINNS_ARMON_2032.jpg?width=1416&height=797&mode=crop.
WINNING MENU PICTURE: https://cdn.vox-cdn.com/thumbor/5MndDDROmTOvM0Vr_HSO7RKojX4=/0x0:2876x2040/1200x800/filters:focal(1002x287:1462x747)/cdn.vox-cdn.com/uploads/chorus_image/image/65831728/94022910.jpg.0.jpg
BEARCAT LOGO: https://i.pinimg.com/originals/d9/2a/ed/d92aedc83aa7f91135046954c2687ea8.png

INTRO MUSIC: https://www.youtube.com/watch?v=m0gPFqFYA0E&t=2s
GAME WINNING AUDIO: https://www.youtube.com/watch?v=F0pyYwuyG90
"""

                #----------PICTURES FOR GAME---------------#

        # CHANGE THE PATH FOR EACH PICTURE TO THE DIRECTORY ON YOUR COMPUTER WHERE THE PICTURES ARE STORED

menuPicPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\Binns.jpg"
bearcatLogoPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\BearcatLogo.png"
peadPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\Pead.jpg"
pikePath =r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\Pike.jpg"
gameWinPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\GameWin.jpg"
playCall1Path = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\kelly1.jpg"
playCall2Path = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\kelly2.jpg"
PikeToBinnsPath = r"C:\\Users\\justi\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GamePictures\\PikeToBinns.jpg"


#LOADS THE PICTURES THAT ARE USED IN THE GAME
menuPic = pygame.image.load(menuPicPath)
bearcatLogo = pygame.image.load(bearcatLogoPath)
peadPic = pygame.image.load(peadPath)
pikePic = pygame.image.load(pikePath)
gameWinPic = pygame.image.load(gameWinPath)
playCall1Pic = pygame.image.load(playCall1Path)
playCall2Pic = pygame.image.load(playCall2Path)
PikeToBinsPic = pygame.image.load(PikeToBinnsPath)


                #----------SOUND FOR GAME---------------#

        # CHANGE THE PATH FOR EACH SOUND FILE TO THE DIRECTORY ON YOUR COMPUTER WHERE THE SOUND FILES ARE STORED
gameWinningAudioPath = r"C:\\Users\\justi\\Documents\\Python Programming\\Final Project\\Python-Final-Project\\GameWinningAudio.mp3"
fightSongAudioPath = r"C:\\Users\\justi\\Documents\\Python Programming\\Final Project\\Python-Final-Project\\FightSong.mp3"


# DEFINE COLORS THAT ARE USED IN THE GAME
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (224,1,34)

# DEFINE THE WIDTH AND HEIGHT OF THE GAME SCREEN
WIDTH = 1150
HEIGHT = 700

# HOW FAST THE GAME WILL RUN
framesPerSecond = 50

# GLOBAL VARIABLES THAT WILL BE USED THROUGHOUT THE GAME
DownNum = 1
ToGo = 10
BallOn = 37
TimeLeft = 90
midfield = 50
SideOfField = "CIN"
timeoutsLeft = 2
yardsGained = 0

"""
FUNCTION NAME: blit_text

FUNCTION DESCRIPTION: This function solves the issue of displaying
                      multiline text and text wrapping in the game

ARGUMENTS: surface = the surface to which the text will display

           text = the text that will be displayed

           pos = a tupple of x,y coordinates that determines
                 where on the screen the text will be displayed

           font = a string that determines what font will be used

           color = what color the text will be
                   text will be red by default

FUNCTION CREDIT: Ted Klein Bergman - stack overflow
                 URL = https://stackoverflow.com/questions/42014195/rendering-text-with-multiple-lines-in-pygame/42015712
"""

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

"""
FUNCTION NAME: displayText

FUNCTION DESCRIPTION: This function allows text to be displayed
                      without needing to retype the text commands
                      each time text needs to be displayed.

ARGUMENTS: messge = the text that is going to displayed to the screen

           font = what font the text will be

           fontSize = what size the text will be

           locationX = the x coordinate that the text will be
                        displayed to

           locationY = the y coordinate that the text will be
                       displayed to

"""

def displayText(message, font, color, fontSize, locationX, locationY):
    text = pygame.font.SysFont('Limonata', fontSize)
    text.set_bold(True)
    text.set_italic(True)
    textSurf = text.render(message, True, color)
    textRect = textSurf.get_rect()
    textRect.center = (locationX/2,locationY/2)
    screen.blit(textSurf,textRect)

"""
FUNCTION NAME: buttons

FUNCTION DESCRIPTION: This function solves the issue of creating buttons
                      in the game that can be clicked and trigger a new
                      event.

ARGUMENTS: msg = what text is going to be displayed on the button

           btnX = the x coordinate that the button will be at 

           btnY = the y coordinate that the button will be at

           buttonWidth = how wide the button will be

           buttonHeight = how tall the button will be

           inactiveColor = the color the button will be when the mouse
                           is not over the button

           activeColor = the color the button will be when the mouse
                         is hovering over the button
            
           activeTextColor = what color the text on the button will be
                             when the mouse is hovering over the button
            
           action = what action is triggered when the button is clicked
                    no action is default. 

            FUNCTION CREDIT: Harrison Kinsley - pythonprogramming.net
                             URL = https://pythonprogramming.net/pygame-button-function-events/
"""

def buttons(msg, btnX, btnY, buttonWidth, buttonHeight, inactiveColor, activeColor, activeTextColor, action=None):
        
        # get mouse click event
        mouse = pygame.mouse.get_pos()
        mouseClick = pygame.mouse.get_pressed()

        buttonFont = pygame.font.SysFont('Limonata', 35)
        buttonFont.set_bold(True)
        buttonText = buttonFont.render(msg, True, WHITE)
        buttonTextRect = buttonText.get_rect()
        buttonTextRect.center = ((btnX+(buttonWidth/2)),(btnY+(buttonHeight/2)))
        screen.blit(buttonText,buttonTextRect)

        # check to see if button is pressed
        if btnX+buttonWidth > mouse [0] > btnX and btnY+buttonHeight > mouse[1] > btnY:
              pygame.draw.rect(screen, activeColor, (btnX,btnY,buttonWidth,buttonHeight))
              buttonText = buttonFont.render(msg, True, activeTextColor)
              screen.blit(buttonText,buttonTextRect)
              if mouseClick[0] == 1 and action != None:
                  action()
        else:
            pygame.draw.rect(screen, inactiveColor, (btnX,btnY,buttonWidth,buttonHeight))
            screen.blit(buttonText,buttonTextRect)

"""
FUNCTION NAME: Results

FUNCTION DESCRIPTION: This function solves the issue of randomly
                      choosing an event that will be used throughout
                      the game

ARGUMENTS: lst - a list that will have a radnom element chosen and returned
"""

def Results(lst):
    return random.choice(lst)

"""
FUNCTION NAME: runOption

FUNCTION DESCRIPTION: This function solves the issue of running the 
                      game if the user selects run ball on the playcall
                      screen
"""

def runOption():

    #declare global so global variables can be modified in the function
    global ToGo
    global DownNum
    global BallOn
    global TimeLeft
    global yardsGained
    global SideOfField

    #possible outcomes that can  be used in the function
    outcome1 = "Not sure why you're running right now but you gained 4 yards."
    outcome2 = "You got lucky and gained 7 yards!"
    outcome3 = "You fool! Pass the stinking ball! You don't play for the Bengals!"
    outcome4 = "You got back to the line of scrimmage. No gain"
    outcome5 = "You got tripped up and only gained 3 yards. Maybe try passing the ball"
    outcome6 = "Defense wasn't expecting run and you gained 10 yards"
    outcome7 = "You got tackled in the backfield. You lost 3 yards"
    
    #create a list of the outcomes and return a random result
    possibleOutcomes = [outcome1, outcome2, outcome3, outcome4, outcome5, outcome6, outcome7]
    result = Results(possibleOutcomes)
    
    #check to see if user wins the game and gets the Pike to Binns animation
    if (TimeLeft <= 30 or yardsGained >= 43):
        PikeToBinnsIntro()

    else:

        # check to see if outcome 1 is ran
        if result == outcome1:
            DownNum += 1
            ToGo -= 4
            yardsGained += 4
            TimeLeft -= 7

            # handles the issue of crossing the 50 yard line
            if BallOn+4 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+4) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 4
            else:
                BallOn += 4

            # check to see if first down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10

            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # otherwise check to see if outcome 2 is ran
        elif result == outcome2:
            DownNum += 1
            ToGo -= 7
            yardsGained += 7
            TimeLeft -= 7

            # handles the isse of crossing the 50 yard line
            if BallOn+7 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+7) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 7
            else:
                BallOn += 7

            # check to see if first down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10

            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # othwerwise check to see if outcome 4 is ran
        elif result == outcome4:
            DownNum += 1
            TimeLeft -= 3

            #check to see if fourth down
            if DownNum > 4:
                TurnoverScreen()

        # otherwise check to see if outcome 5 is ran
        elif result == outcome5:
            DownNum += 1
            ToGo -= 3
            yardsGained += 3
            TimeLeft -= 7

            # handles the issue of crossing the 50 yard line
            if BallOn+3 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+3) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 3
            else:
                BallOn += 3

            #  check to see if fourth down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10

            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # otherwise check to see if outcome 6 is ran
        elif result == outcome6:
            DownNum += 1
            ToGo -= 10
            yardsGained += 10
            TimeLeft -= 7

            # handles issue of crossing the 50 yard line
            if BallOn+10 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+10) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 10
            else:
                BallOn += 10

            # check to see if first down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            
            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # check to see if outcome7 is ran
        elif result == outcome7:
            DownNum += 1
            ToGo += 3
            yardsGained -= 3
            TimeLeft -= 7

            # handles issue of crossing 50 yard line
            if BallOn+3 > 50 and SideOfField == "PIT":
                yardsRemaining = (BallOn+3) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "CIN"
            elif yardsGained > 13:
                BallOn += 3
            else:
                BallOn -= 3

            # check to see if first down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # loop to display play outcome and let user move to next play
        x = True
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

            # check to see if user quit the game
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit

"""
FUNCTION NAME: passOption

FUNCTION DESCRIPTION: This function handles running the game if the 
                      user selects to pass the ball
"""

def passOption():

    #declare global so global variables can be modified in the function
    global ToGo
    global DownNum
    global BallOn
    global TimeLeft
    global yardsGained
    global SideOfField

    # possible outcomes that can  be used in the function
    outcome1 = "You found an open receiver for a gain of 5 yards!"
    outcome2 = "You found an open receiver for a gain of 3 yards!"
    outcome3 = "You got sacked! Loss of 3 yards!"
    outcome4 = "You threw a deep bomb and connected for a gain of 10 yards"
    outcome5 = "You coudln't find any open receivers but scrambled for 4 yards"
    outcome6 = "Incomplete Pass. No gain"
    outcome7 = "You threw a passs right on target for a gain of 7 yards"

    # create a list of the outcomes and return a random result
    possibleOutcomes = [outcome1, outcome2, outcome3, outcome4, outcome5, outcome6, outcome7]
    result = Results(possibleOutcomes)

    #check to see if user wins the game and gets the Pike to Binns animation
    if (TimeLeft <= 30 or yardsGained >= 33):
        PikeToBinnsIntro()
    else:

        # check to see if outcome 1 is ran
        if result == outcome1:
            DownNum += 1
            ToGo -= 5
            yardsGained += 5
            TimeLeft -= 7

            # handles the issue of crossing the 50 yard line
            if BallOn+5 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+5) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 5
            else:
                BallOn += 5

            # check to see if first down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10

            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # otherwise check to see if outcome 2 is ran
        elif result == outcome2:
            DownNum += 1
            ToGo -= 3
            yardsGained += 3
            TimeLeft -= 7

            # handles the issue of crossing the 50 yard line
            if BallOn+3 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+3) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 3
            else:
                BallOn += 3

            # check to see if first down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            
            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # otherwise check to see if outcome 3 is ran
        elif result == outcome3:
            DownNum += 1
            ToGo += 3
            yardsGained -= 3
            TimeLeft -= 7

            # handles the issue of crossing the 50 yard line
            if BallOn+3 > 50 and SideOfField == "PIT":
                yardsRemaining = (BallOn+3) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "CIN"
            elif yardsGained > 13:
                BallOn += 3
            else:
                BallOn -= 3

            # check to see if fourth down
            if DownNum > 4:
                TurnoverScreen()

        # otherwise check to see if outcome 4 is ran
        elif result == outcome4:
            DownNum += 1
            ToGo -= 10
            yardsGained += 10
            TimeLeft -= 12

            # handles the issue of crossing the 50 yard line
            if BallOn+10 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+10) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 10
            else:
                BallOn += 10

            # check to see if first down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10

            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # check to see if outcome5 is ran
        elif result == outcome5:
            DownNum += 1
            ToGo -= 4
            yardsGained += 4
            TimeLeft -= 7

            # handles the issue of crossing the 50 yard line
            if BallOn+4 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+5) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 4
            else:
                BallOn += 4

            # check to see if first down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10

            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # check to see if outcome6 is ran
        elif result == outcome6:
            DownNum += 1
            TimeLeft -= 7

            #check to see if fourth down
            if DownNum > 4:
                TurnoverScreen()

        # otherwise outcome 7 is ran
        else:
            DownNum += 1
            ToGo -= 7
            yardsGained += 7
            TimeLeft -= 7

            # handles the issue of crossing the 50 yard line
            if BallOn+7 > 50 and SideOfField == "CIN":
                yardsRemaining = (BallOn+7) - 50
                BallOn = 100 - 50 - yardsRemaining
                SideOfField = "PIT"
            elif yardsGained > 13:
                BallOn -= 7
            else:
                BallOn += 7

            # check to see if first down
            if (DownNum > 4 and ToGo <= 0) or ToGo <= 0:
                DownNum = 1
                ToGo = 10
            
            # otherwise check to see if fourth down
            elif DownNum > 4 and ToGo > 0:
                TurnoverScreen()

        # loop to display play result and let user advance to next play
        x = True
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

"""
FUNCTION NAME: getSuffix

FUNCTION DESCRIPTION: This function solves the issue of getting
                      the correct suffix to display to the screen
                      based on the corresponding screen

ARGUMENTS: currentDown - takes the current down to determine
                         the correct suffix to display
"""

def getSuffix(currentDown):
    if currentDown == 1:
        return "st"
    elif currentDown == 2:
        return "nd"
    elif currentDown == 3:
        return "rd"
    else: 
        return "th"

"""
FUNCTION NAME: playcallScreen

FUNCTION DESCRIPTION: This function solves the issue of displaying
                      the playcall screen which allows the user to
                      select pass, run, or timeout

"""

def playcallScreen():
    #stop playing the intro music
    pygame.mixer.music.stop()

    #determine what text will be displayed to the screen
    if yardsGained < 13:
        message = "Down: " + str(DownNum) + getSuffix(DownNum) + " and " + str(ToGo) + "               " + "Ball on: " + str(SideOfField) + " " + str(BallOn) + "               " + "Time left: " + str(TimeLeft) + " seconds"
    elif yardsGained == 13:
        message = "Down: " + str(DownNum) + getSuffix(DownNum) + " and " + str(ToGo) + "               " + "Ball on: " + str(BallOn) + "               " + "Time left: " + str(TimeLeft) + " seconds"
    else:
        message = "Down: " + str(DownNum) + getSuffix(DownNum) + " and " + str(ToGo) + "               " + "Ball on: " + str(SideOfField) + " " +  str(BallOn) + "           " + "Time left: " + str(TimeLeft) + " seconds"
    
    #gets a random image to display to the playcall screen
    playcallImage = Results([playCall1Pic, playCall2Pic])

    # loop to display options to call pass, run, or timeout, and display an image
    x = True
    while x:

        #fill the screen and display an image
        screen.fill(RED)
        if playcallImage == playCall2Pic:
            screen.blit(playcallImage, (285,280))
        else:
            screen.blit(playcallImage, (350,280))
        
        #screen if the user has timeouts left
        if timeoutsLeft > 0:
            displayText(message,'Limonata',BLACK,35,1155,225)
            buttons("PASS", 250,175,150,75,BLACK,WHITE,BLACK, passOption)
            buttons("RUN", 450,175,150,75,BLACK,WHITE,BLACK, runOption)
            buttons("TIMEOUT", 650,175,150,75,BLACK,WHITE,BLACK, timeoutScreen)
            pygame.display.update()
            clock.tick(framesPerSecond)
        
        #screen if the user has no timeouts left
        else:
            displayText(message,'Limonata',BLACK,35,1155,225)
            buttons("PASS", 400,175,150,75,BLACK,WHITE,BLACK, passOption)
            buttons("RUN", 600,175,150,75,BLACK,WHITE,BLACK, runOption)
            pygame.display.update()
            clock.tick(framesPerSecond)

        # check to see if the user quits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit


"""
FUNCTION NAME: timeoutScreen

FUNCTION DESCRIPTION: This function solves the issue of displaying
                      a screen if the user calls a timeout
"""
def timeoutScreen():
    global timeoutsLeft

    #decrement timoeouts and create a message to display to the screen
    timeoutsLeft -= 1
    message = "You called a timeout! You have " + str(timeoutsLeft) + " timeout left."

    x = True
    while x:
        screen.fill(BLACK)
        displayText(message, "Limonata", RED, 35, WIDTH, HEIGHT)
        buttons("GOT IT! NEXT PLAY", 415,470,350,50, RED,WHITE,RED, playcallScreen)
        pygame.display.update()
        clock.tick(framesPerSecond)

        # check to see if the user quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

"""
FUNCTION NAME: blit_text

FUNCTION DESCRIPTION: This function solves the issue of displaying
                      a screen and allowing the user to quit or play 
                      again if the user turned the ball over on downs

"""

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

        #check to see if the user quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit
"""
FUNCTION NAME: blit_text

FUNCTION DESCRIPTION: This function solves the issue of displaying
                      a screen that will allow the user to trigger
                      an event to play the winning audio and display
                      the winnning screen
"""

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

        # check to see if the user quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

"""
FUNCTION NAME: PikeToBinns():

FUNCTION DESCRIPTION: This function solves the issue of displaying
                      the game winning screen and playing the game
                      winning audio
"""

def PikeToBinns():
    
    #load the game winning sound and play
    gameWinningSound = pygame.mixer.music.load(gameWinningAudioPath)
    pygame.mixer.music.play(0)

    x = True
    while x:
        screen.fill(BLACK)
        displayText("YOU WON!", "Limonata", RED, 55, 1150,200)
        screen.blit(gameWinPic, (322,190))
        buttons("QUIT", 50,300,250,75, RED,WHITE,RED, quit)
        buttons("PLAY AGAIN", 850,300,250,75, RED,WHITE,RED, gameMenu)
        pygame.display.update()
        clock.tick(framesPerSecond)

        #check to see if the user quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

"""
FUNCTION NAME: blit_text

FUNCTION DESCRIPTION: This function solves the issue of displaying
                      the main menu of the game

"""
def gameMenu():
    #reset the game to intitial values
    resetGame()

    #load music and play
    fightSongSound = pygame.mixer.music.load(fightSongAudioPath)
    pygame.mixer.music.play(0)

    intro = True
    while intro:
        screen.fill(BLACK)
        buttons("PLAY!", 415,470,350,50, RED, WHITE, RED, gameLoop)
        displayText("Pike to Binns Recreation", "Limonata", RED, 50, 1150, 150)
        screen.blit(menuPic, (325,130))
        screen.blit(bearcatLogo, (40,170))
        screen.blit(bearcatLogo, (870,170))
        pygame.display.update()
        clock.tick(framesPerSecond)

        #check to see if the user quit the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit

#initialize game screen and display the window
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Game Winning Drive")
clock = pygame.time.Clock()

"""
FUNCTION NAME: blit_text

FUNCTION DESCRIPTION: This function solves the issue of resetting
                      the game to initial values

"""

def resetGame():
    # global keyword so gloabl variables can me modified in the function
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

"""
FUNCTION NAME: blit_text

FUNCTION DESCRIPTION: This function solves the issue of runnnig the game
                      in a loop until the user quits
"""

def gameLoop():
    text = "It's December 5, 2009 and your beloved University of Cincinnati Bearcats are taking on the University of Pittsburgh Panthers.\n\nThe winner clinches the conference championship.\n\nThe Bearcats have a shot at playing inthe national championship with a win.\n\nHowever, the game starts out rough and the Bearcats are down 31-17 at haltime.\n\nAfter making some halftime adjustments, you come out strong in the second half and manage to tie the game up 38-38 at halftime.\n\nUnfortunately, Pittsburgh scores a touchdown late and manages to take the lead.\n\nBUT THEY MISS THE TWO POINT CONVERSION!\n...................................................................................................................................................\nThere's 1:30 left in the game and you have the ball on your own 39 yard line with 2 timeouts left.\n\nCan you drive down the field and score the game winning touchdown and give the Bearcats a chance to play in the national championship game?"
    instructionFont = pygame.font.SysFont('Times New Roman', 18)
    instructionFont.set_bold(True)

    gameRunning = True
    while gameRunning:
        #keep the game running at the right speed
        screen.fill(BLACK)
        blit_text(screen, text, (20,100), instructionFont)
        buttons("ONWARDS TO VICTORY!",385,570,350,50, RED, WHITE, RED, playcallScreen)
        pygame.display.update()
        clock.tick(framesPerSecond)
        
        #check to see if the user quits the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameRunning = False

    pygame.quit()
    quit

#CALL TO START PLAYING THE GAME!
gameMenu()