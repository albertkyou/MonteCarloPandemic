import pygame
import numpy as np 
import matplotlib.pyplot as plt 


# Create a Monte Carlo simulation of random walk.

def initialize_board(num_people):
    # calculate initial positions of people
    init_pos = 100*np.random.rand(num_people,2) # x,y positions of num_people people in 100x100 grid

    return init_pos

def random_walk_step(init_pos, speed):
    num_people = init_pos.shape[0]
    pos = init_pos + speed*(2*np.random.rand(num_people,2)-1)

    return pos

def draw_dots(pos,screen):

    for i in range(pos.shape[0]):
        pygame.draw.circle(screen,(0,0,0),(int(pos[i,0]),int(pos[i,1])),1)
    
    pygame.display.update()



# Now we need to wrap those functions in a pygame window


# Display the counter for dots inside the circle and outside the circle



def main():
    pygame.init()

    background_colour = (255,255,255) # white
    (width, height) = (500,500)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Approximate Pi')
    screen.fill(background_colour)

    pos = initialize_board(1)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pos = random_walk_step(pos,5)

        draw_dots(pos,screen)


main()