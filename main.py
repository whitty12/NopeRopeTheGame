#Import the pygame library
from operator import truediv

import pygame
from pygame import RESIZABLE

#constant variables
SNEKCOLOR = (0,255,0) #Green
FOODCOLOR = (255,222,33) #Yellow
WIDTH_OF_WINDOW = 800
HEIGHT_OF_WINDOW = 800
SNEK_HEAD_SIZE = (20,20,20,20)

#Global variables
pos_x = 0
pos_y = 0

#Initialize pygame to initialize all the pygame modules
pygame.init()

#Create a resizable window of size determined in the setting variables using .set_mode function
screen = pygame.display.set_mode((WIDTH_OF_WINDOW,HEIGHT_OF_WINDOW), RESIZABLE)

#function that updates the position of the snake every second. While prototyping, only the user can move it forward
def movesnekforward(pos_x, pos_y, is_alive):

    if is_alive == True:
        pos_x += 0
        pos_y += 1

        position_on_screen = pygame.display.set_mode(pos_x,pos_y)
        pygame.draw.rect(position_on_screen,SNEKCOLOR, pygame.Rect(SNEK_HEAD_SIZE))

def isalive():
    if WIDTH_OF_WINDOW + 1 == pos_x:
        return False

    if HEIGHT_OF_WINDOW + 1 == pos_y:
        return False

    if WIDTH_OF_WINDOW - 1 == pos_x:
        return False

    if HEIGHT_OF_WINDOW- 1 == pos_y:
        return False

    return True


#funtion that updates all parts of the game
def updategame(screen):
    #move snake if alive
    movesnekforward(pos_x,pos_y,isalive)

    # The pygame.display.flip() method is used
    # to update content on the display screen
    pygame.display.flip()

#Main Function
#Set the title of the game
pygame.display.set_caption('Nope Rope')

# Draw the snake's head
pygame.draw.rect(screen, SNEKCOLOR, pygame.Rect(SNEK_HEAD_SIZE))

#create variables that will loop the game until the user exits
running = True

while running == True:

    updategame(screen)

    #Check for the user quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
