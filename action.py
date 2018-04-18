# ICS3U
# Assignment 2: Action
# <MOAIZ AHMAD>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from snow import Snow
pygame.init()

pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer=4096)
pygame.mixer.music.load('Sounds/Boyz II Men- Let It Snow.mp3')
pygame.mixer.music.play(-1)

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the screen size
SCREENWIDTH = 400
SCREENHEIGHT = 400

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My Animation")
speed = 1
SNOW = pygame.sprite.Group()

for i in range (50):
    mySnow = Snow(WHITE,10,10,random.randint(5,20))
    mySnow.rect.x = random.randint(0,400)
    mySnow.rect.y = random.randint(0,400)
    SNOW.add(mySnow)
    
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                carryOn = False

    # --- Game logic goes here
    for snow in SNOW:
        snow.moveBackward(5)
        if snow.rect.y > SCREENHEIGHT:
            snow.changeSpeed(random.randint(5,20))
            snow.rect.y = -200
            snow.rect.x = random.randint(0,400)

    
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(BLACK)
    SNOW.draw(screen)
    pygame.draw.line(screen, RED, [200, 0], [200, 400], 7)
    pygame.draw.line(screen, RED, [0, 200], [400, 200], 7)

    # Queue different shapes and lines to be drawn
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
