import pygame
import numpy as np 
import matplotlib.pyplot as plt 


# Create a Monte Carlo simulation of random walk.

def initialize_board(num_people):
    # calculate initial positions of people
    init_pos = 500*np.random.rand(num_people,2) # x,y positions of num_people people in 500x500 grid
    infected = [np.random.randint(num_people+1)] # list of infected individuals

    return init_pos, infected

def random_walk_step(init_pos, speed,infected):
    num_people = init_pos.shape[0]
    pos = init_pos + speed*(2*np.random.rand(num_people,2)-1)
    # make bounds
    for i in range(pos.shape[0]):
        if pos[i,0] < 0 or pos[i,0] > 500:
            pos[i,0] = init_pos[i,0]
        if pos[i,1] < 0 or pos[i,1] > 500:
            pos[i,1] = init_pos[i,1]
        if near_infected(infected,pos,pos[i,:]) and (i not in infected):
            infected.append(i)

    return pos

def near_infected(infected,pos,person):
    # calculate distance between person and all infected individuals
    social_distance = 6 

    for individual in infected:
        infected_individual_position = pos[individual,:]

        distance = np.sqrt((person[0]-infected_individual_position[0])**2+(person[0]-infected_individual_position[0])**2)
        if distance < social_distance:
            return True
    
    return False

def draw_dots(pos,infected,screen):

    for i in range(pos.shape[0]):
        if i in infected:
            color = (255,0,0)
        else:
            color = (0,0,0)
        
        pygame.draw.circle(screen,color,(int(pos[i,0]),int(pos[i,1])),2)
    
    pygame.display.update()



# Now we need to wrap those functions in a pygame window

# Approximate social distancing by saying the chance of infection as dependent on the distance to those infected

# Display the counter for dots inside the circle and outside the circle

pygame.init()

def main():


    background_colour = (255,255,255) # white
    (width, height) = (500,500)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Approximate Pi')
    screen.fill(background_colour)

    pos, infected = initialize_board(300)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pos = random_walk_step(pos,5,infected)
        screen.fill((255,255,255))
        draw_dots(pos,infected,screen)
        pygame.time.wait(50)

main()