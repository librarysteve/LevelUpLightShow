from colordict import *
import random
from time import sleep
def randColor():
    i = random.randint(1,len(c))
    b = i-1
    return c[b]

def fill_strip(np, num_pix, color):
    for i in range(num_pix):
        np[i] = color
        sleep(0.1)

def randomFlashes(np, number):
    for i in range(number):
        np.fill(randColor())
        sleep(1)
        np.fill(BLACK)

def randFill(np, num_pix):
    for i in range(num_pix):
        np[i] = randColor()
        sleep(0.1)
    for i in range(num_pix):
        np[i] = BLACK
        sleep(0.1)

def runner(np, num_pix, color):
    for i in range(num_pix):
        np[i] = color
        sleep(0.05)
        np[i] = BLACK
