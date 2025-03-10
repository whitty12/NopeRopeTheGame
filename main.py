#Import the pygame library
import pygame
from pygame import RESIZABLE
import numpy as np


#constant variables
SNEKCOLOR = (0,255,0) #Green
FOODCOLOR = (255,222,33) #Yellow
NOPEROPECOLOR = (255,228,196) #variation of brown, for the body segments
BLACK = (0,0,0,) #Black
WIDTH_OF_WINDOW = 600
HEIGHT_OF_WINDOW = 600
SNEK_SEGMENT_SIZE = (20,20) #this is the dimensions of each box

#Global variables
#default food dimensions
food_size = [220, 300, 20,20]
#replace individual x, y value with one array
snek_head_position = [20,50]
#snake default (TODO: Randomize starting position later)
snek_nope_rope = [[20,50],
                  [20,40],
                  [20,30],
                  [20,20]]

#Create a resizable window of size determined in the setting variables using .set_mode function
window = pygame.display.set_mode((WIDTH_OF_WINDOW,HEIGHT_OF_WINDOW))
clock = pygame.time.Clock()
food = pygame.Rect(food_size)

############################################
def foodCaught(head_xpos, head_ypos, food_xpos, food_ypos):
    if (head_xpos == food_xpos) and (head_ypos == food_ypos):
        return True

############################################
#Main Function
#Set the title of the game
pygame.display.set_caption('Nope Rope')

#create variables that will loop the game until the user exits
running = True
food_spawned = True

while running == True:
    #Timer for the game
    clock.tick(60)

    #Check for the user quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            #NOTE: swap from move_ip to simple incrementing as it is not a rectangle and therefore does not use this method
            if event.key == pygame.K_LEFT:
                snek_head_position[0] -= 20
            elif event.key == pygame.K_RIGHT:
                snek_head_position[0] += 20
            elif event.key == pygame.K_DOWN:
                snek_head_position[1] += 20
            elif event.key == pygame.K_UP:
                snek_head_position[1] -= 20

    #we fill BEFORE to prevent overwriting as well as to erase the previous movement drawn on the screen
    window.fill(BLACK)

    snek_nope_rope.insert(0,list(snek_head_position))

    #initial snake body and draw the array
    for segment in snek_nope_rope:
        pygame.draw.rect(window, SNEKCOLOR, pygame.Rect(segment[0],segment[1], 20,20))

    #check if the food is spawned and draw our next food piece
    if food_spawned == True:
        pygame.draw.rect(window, FOODCOLOR, food)

    #if food is caught we need to delete and respawn elsewhere
    #TODO: Fix the comparison method to ensure the x/y can always align to trigger this condition
    if foodCaught(snek_head_position[0], snek_head_position[1], food.x, food.y):
        pygame.draw.rect(window, SNEKCOLOR, food)
        #increment number of body parts
        # insert at the start of our snek array
        food_spawned = False
        #for segment in num_of_nope_ropes:
        #    snek_segment.x = snek_segment.x - 20
        #    snek_segment.y = snek_segment.y - 20
        #    pygame.draw.rect(window, NOPEROPECOLOR, snek_segment)

    #TODO: Fix the removal of every element from the snake body as we only want to remove part of it
    #snek_nope_rope.pop()

    #update the state of the screen
    pygame.display.update()