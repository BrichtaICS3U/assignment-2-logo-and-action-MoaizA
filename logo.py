# ICS3U
# Assignment 2: Logo
# <MOAIZ AHMAD>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (224, 53, 53)
yellow = (227,221,71)
# Set the screen size (please don't change this)
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(RED)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    pygame.draw.ellipse(screen, yellow, [100, 100, 200, 200], 0)#The outer yellow circle
    pygame.draw.ellipse(screen, BLACK, [100, 100, 200, 200], 4)#The outer outline
    pygame.draw.ellipse(screen, WHITE, [125, 125, 150, 150], 0)#The inner most circle 
    pygame.draw.ellipse(screen, BLACK, [125, 125, 150, 150], 4)#The border around the white circle
    pygame.draw.polygon(screen, yellow,[[135,200],[300,40],[200,200]])#the top of the lightning bolt
    pygame.draw.polygon(screen, BLACK,[[135,200],[300,40],[200,200]],4)#the top border of the lightning bolt
    pygame.draw.polygon(screen, yellow,[[265,180],[100,300],[200,180]])#The lower lightning bolt
    pygame.draw.polygon(screen, BLACK,[[265,180],[100,300],[200,180]],4)#The lower border of the lightning bolt
    pygame.draw.line(screen, yellow,[200,178],[185,198],6)
    
        

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
