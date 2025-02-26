#Import the pygame library
import pygame
from pygame import RESIZABLE


#constant variables
SNEKCOLOR = (0,255,0) #Green
FOODCOLOR = (255,222,33) #Yellow
WIDTH_OF_WINDOW = 600
HEIGHT_OF_WINDOW = 600
SNEK_HEAD_SIZE = (20,20,20,20)

#Global variables
pos_x = 0
pos_y = 0

#Create a resizable window of size determined in the setting variables using .set_mode function
window = pygame.display.set_mode((WIDTH_OF_WINDOW,HEIGHT_OF_WINDOW))
snek_head = pygame.Rect(SNEK_HEAD_SIZE)
clock = pygame.time.Clock()


#Main Function
#Set the title of the game
pygame.display.set_caption('Nope Rope')

#create variables that will loop the game until the user exits
running = True

while running == True:
    #Timer for the game
    clock.tick(60)

    #Check for the user quitting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snek_head.move_ip(-5,0)
            elif event.key == pygame.K_RIGHT:
                snek_head.move_ip(5,0)
    window.fill((0, 0, 0))
    pygame.draw.rect(window, SNEKCOLOR, snek_head)
    pygame.display.update()