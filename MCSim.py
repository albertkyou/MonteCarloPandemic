import pygame as pg 
import numpy as np 
import matplotlib.pyplot as plt 


# Create a Monte Carlo simulation of random walk.

def initialize_board(num_people):
    # calculate initial positions of people
    init_pos = 100*np.random.rand(num_people,2) # x,y positions of num_people people in 100x100 grid
    plt.plot(init_pos[:,0],init_pos[:,1],'o')
    plt.show()
    return init_pos

def random_walk_step(init_pos, speed):
    num_people = init_pos.shape[0]
    pos = init_pos + speed*(2*np.random.rand(num_people,1)-1)
    plt.figure()
    plt.plot(pos[:,0],pos[:,1],'o')
    plt.show()

    return pos

init_pos=initialize_board(10)

random_walk_step(init_pos, 5)