#Import the pygame library
from operator import truediv

import pygame

#global variables
width_of_window = 800
height_of_window = 800

#Initialize pygame to initialize all the pygame modules
pygame.init()

#Create a window of size determined in the setting variables using .set_mode function
pygame.display.set_mode((width_of_window,height_of_window))

#create variables that will loop the game until the user exits
running = True

while running == True:

    #Check for the user quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False