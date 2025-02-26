#Import the pygame library
import pygame
from pygame import RESIZABLE


#constant variables
SNEKCOLOR = (0,255,0) #Green
FOODCOLOR = (255,222,33) #Yellow
BLACK = (0,0,0,) #Black
WIDTH_OF_WINDOW = 600
HEIGHT_OF_WINDOW = 600
SNEK_HEAD_SIZE = (20,20,20,20)

#Global variables
pos_x = 0
pos_y = 0
food_size = (220, 300, 20,20)

#Create a resizable window of size determined in the setting variables using .set_mode function
window = pygame.display.set_mode((WIDTH_OF_WINDOW,HEIGHT_OF_WINDOW))
snek_head = pygame.Rect(SNEK_HEAD_SIZE)
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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snek_head.move_ip(-20,0)
            elif event.key == pygame.K_RIGHT:
                snek_head.move_ip(20,0)
            elif event.key == pygame.K_DOWN:
                snek_head.move_ip(0,20)
            elif event.key == pygame.K_UP:
                snek_head.move_ip(0,-20)

    window.fill(BLACK)
    #snake head
    pygame.draw.rect(window, SNEKCOLOR, snek_head)

    #check if the food is spawned and draw our next food piece
    if food_spawned == True:
        pygame.draw.rect(window, FOODCOLOR, food)

    #if food is caught we need to delete and respawn elsewhere
    if foodCaught(snek_head.x, snek_head.y, food.x, food.y):
        pygame.draw.rect(window, SNEKCOLOR, food)
        food_spawned = False

    #update the state of the screen
    pygame.display.update()