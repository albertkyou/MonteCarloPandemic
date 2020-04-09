import pygame
import numpy as np 
import matplotlib.pyplot as plt 


# Create a Monte Carlo simulation of random walk.


def init(e1=50,e2=10,e3=2,e4=5):

    global num_people,speed,infected,r0,social_distance

    num_people = e1
    r0 = e2
    speed = e3

    social_distance = e4

    main()



def initialize_board(num_people):
    # calculate initial positions of people
    init_pos = 500*np.random.rand(num_people,2) # x,y positions of num_people people in 500x500 grid
    infected = [np.random.randint(num_people+1)] # list of infected individuals

    return init_pos, infected

def random_walk_step(init_pos, speed ,infected):
    num_people = init_pos.shape[0]
    pos = init_pos + speed*(2*np.random.rand(num_people,2)-1)
    # make bounds
    for i in range(pos.shape[0]):
        if pos[i,0] < 0 or pos[i,0] > 500:
            pos[i,0] = init_pos[i,0]
        if pos[i,1] < 0 or pos[i,1] > 500:
            pos[i,1] = init_pos[i,1]
        if near_infected(infected,pos,pos[i,:],social_distance,r0) and (i not in infected):
            infected.append(i)

    

    return pos

def near_infected(infected,pos,person, social_distance, r0):
    # calculate distance between person and all infected individuals
    for individual in infected:
        infected_individual_position = pos[individual,:]

        distance = np.sqrt((person[0]-infected_individual_position[0])**2+(person[1]-infected_individual_position[1])**2)
        if distance < social_distance:
            if r0*np.random.rand()>1:
                return True
    
    return False

def draw_dots(pos,infected,screen):

    for i in range(pos.shape[0]):
        if i in infected:
            color = (255,0,0)
            marker_size = 4
        else:
            color = (0,0,0)
            marker_size = 2
        
        pygame.draw.circle(screen,color,(int(pos[i,0]),int(pos[i,1])),marker_size)
    
    pygame.display.update()



##### Now we need to wrap those functions in a pygame window
pygame.init()


def main():


    background_colour = (255,255,255) # white
    (width, height) = (500,500)

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Pandemic Simulator')
    screen.fill(background_colour)

    pos, infected = initialize_board(num_people)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pos = random_walk_step(pos,speed,infected)
        screen.fill((255,255,255))
        draw_dots(pos,infected,screen)
        pygame.time.wait(50)

