## ANA* Algorithm

# import libraries
import Queue as Q
from sys import version_info
import math
if version_info.major == 2:
    # We are using Python 2.x
    from Tkinter import *
    import ttk
elif version_info.major == 3:
    # We are using Python 3.x
    from tkinter import *
    from tkinter import ttk

import time as t
import numpy as np

'''
Define the color scheme for visualization. You may change it but I recommend using the same colors
'''
# white (0) is an unvisited node, black(1) is a wall, blue(2) is a visited node
# yellow(3) is for start node, green(4) is for exit node, red (5) is a node on the completed path
colors = {5: "red", 4: "green", 3: "yellow", 2: "blue", 1: "black", 0: "white"}


'''
Opens the maze file and creates tkinter GUI object
'''
# load maze
with open("hard.txt") as text:
    maze = [list(line.strip()) for line in text]
[col, row] = np.shape(maze)

print(type(maze))

# create map
root = Tk()
size = 800 / row
canvas = Canvas(root, width=(size*row), height=(size*col))
root.title("ANA* Algorithm")

# Creating  a class node
G=999999

shortest_path=[]
class node:
    def __init__(self,x,y,val,p):
        self.colour=val
        self.x=x
        self.y=y
        self.e=None  #Update this value using member function
        self.g=None  #Assign a high value
        self.h=0.000001  #Calculate using euclidean distance ( But do i need a member function)
        self.f=None  #Update using a member function)
        self.parent=p

    def update(self,g_p,goal):
        self.g=g_p+1    # g_p -> cost of parent and 1->cost for moving from parent to child
        self.h=math.sqrt((self.x-goal[0])**2 +(self.y-goal[1])**2)
        #self.h=0
        self.f=self.g+self.h

    def update_ana(self,g_p,goal):
        global G
        self.g=g_p+1    # g_p -> cost of parent and 1->cost for moving from parent to child
        self.h=math.sqrt((self.x-goal[0])**2 +(self.y-goal[1])**2)
        self.e = (G - self.g) / (self.h+0.0000000001)

        self.f=self.g+self.h

    ## Function for checking whether the nodes are equal
    def __eq__(self, other):
        z=0
        if(self.x ==other.x and self.y==other.y):
            z=1
        return (z)