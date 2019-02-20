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
with open("hard3.txt") as text:
    maze = [list(line.strip()) for line in text]
[col, row] = np.shape(maze)

#print(type(maze))

# create map
root = Tk()
size = 800 / row
canvas = Canvas(root, width=(size*row), height=(size*col))
root.title("ANA* Algorithm")

# Creating  a class node
class node:
    def __init__(self,x,y,val,p):
        self.colour=val
        self.x=x
        self.y=y
        self.e=None  #Update this value using member function
        self.g=999999  #Assign a high value
        self.h=None  #Calculate using euclidean distance ( But do i need a member function)
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
        if(self.h)==0:
            self.h=1e-15
        self.e = (G - self.g) / (self.h)



    ## Function for checking whether the nodes are equal
    def __eq__(self, other):
        z=0
        if(self.x ==other.x and self.y==other.y):
            z=1
        return (z)

def draw_canvas(canvas, maze):
    '''
    Change this according to the data structure of your maze variable.3
    If you are using a node class like the one mentioned below,
    You may have to change fill=colors[int(maze[i][j])] to fill=colors[int(maze[i][j].color)]
    '''
    for i in range(0, col):
        for j in range(0, row):
            canvas.create_rectangle(j*size, i*size, (j+1)*size, (i+1)*size, fill=colors[int(maze[i][j])])
    canvas.pack()



def find_neighbours(maze,node2):
    global node_list
    '''Four neighbour approach'''
    #actions=[(0,-1),(0,1),(-1,0),(1,0)]

    '''eight neighbour approach'''
    actions = [(0, -1), (0, 1), (-1, 0), (1, 0),(-1,1),(1,1),(1,-1),(-1,-1)]
    neighbours =[]
    for a in actions:
        neighbour_node_position=(node2.x+a[0],node2.y+a[1])

        #verify whether the node position lies within the maze
        if(neighbour_node_position[0]>len(maze)-1 or neighbour_node_position[0]<0 or neighbour_node_position[1]>(len(maze[len(maze)-1])-1) or neighbour_node_position[1]<0):
            continue

        # verify whether the position doesn't have any obstacles
        if (maze[neighbour_node_position[0]][neighbour_node_position[1]])=='1':
            continue

        # create a new node
        #new_node=node(neighbour_node_position[0],neighbour_node_position[1],3,node2)

        # Append it with the neighbour list
        #print neighbour_node_position[0],neighbour_node_position[1]
        #neighbours.append(new_node)

        neighbours.append(node_list[neighbour_node_position[0]][neighbour_node_position[1]])

    return neighbours

#Creating a matrix of nodes
node_list = [[0 for x in range(0,row)] for y in range(0,col)]
def node_creation():
    global node_list
    for i in range(0, col):
        for j in range(0, row):
            node_list[i][j]=node(i,j,0,None)


def a_star(maze,start,exit):

    start_time=t.clock()
    start_time=t.clock()
    start_node=node(start[0],start[1],3,None)
    goal_node=node(exit[0], exit[1], 4, None)

    start_node.update(0,exit)
    goal_node.update(0, exit)

    open_list=[]
    closed_list=[]

    open_list.append(start_node)

    #Loop until the list is empty
    while(len(open_list)>0):
        #print("iteration begin")
        current_node=open_list[0]

        current_index=0

        for index,node1 in enumerate(open_list):

            if node1.f<current_node.f:

                current_node=node1
                current_index=index
            elif node1.f==current_node.f:
                if node1.g<current_node.g:
                    current_node = node1
                    current_index = index

        #Remove the element with the lowest f value from the open list
        y=open_list.pop(current_index)


        closed_list.append(y)

        #Check whether the current node is the goal
        #Backtrack the path
        if current_node == goal_node:
            end=t.clock()
            print("Time taken for Astar solution")
            print(end-start_time)
            shortest_path=[]
            current=current_node
            while current is not None:
                shortest_path.append((current.x,current.y))
                maze[current.x][current.y] = 5
                current=current.parent

            maze[start[0]][start[1]] = 3
            maze[exit[0]][exit[1]] = 4
            draw_canvas(canvas, maze)
            root.update()
            end=t.clock()
            print shortest_path
            return shortest_path[::-1],closed_list #returns reversed path


        #Find neighbours of the current node
        neighbours=find_neighbours(maze,current_node)





        # Loop through the neighbours to find which one to expand
        for neighbour in neighbours:
            maze[neighbour.x][neighbour.y]=2
            # Check whether the node is already expanded
            for expanded in closed_list:
                flag=0
                if neighbour==expanded:
                    flag=1
                    break
            if flag:
                continue


            # update the nodes values
            neighbour.update(current_node.g,exit)

            # Update the open list
            flag=0
            for unexpanded_node in open_list:
                if neighbour==unexpanded_node:
                    flag==1
                    if neighbour.g>unexpanded_node.g:
                         break

                    else:

                        neighbour.g=unexpanded_node.g
                        neighbour.f=unexpanded_node.f
                        neighbour.parent=unexpanded_node.parent
                        break




            if(flag==0):
                open_list.append(neighbour)

    return None,closed_list







# Global variable for storing the G
G=99999999
E=99999999


def improvesolution(goal):
    global open_list
    global E
    global shortest_path
    goal_node=goal

    while(len(open_list)>0):
        current_node=open_list[0]

        #Finding the element with maximum of e(s)
        for index,element in enumerate(open_list):
            current_index=0
            if element.e>current_node.e:
                current_node=element
                current_index=index

        current_node=open_list.pop(current_index)

        #Assign colour to it
        maze[current_node.x][current_node.y] = 2

        #Updating E
        if current_node.e<E:
            E=current_node.e

        #Checking goal condition
        if current_node.x==goal_node[0] and current_node.y==goal_node[1]:
            global G
            G=current_node.g

            # Backtrack the path
            shortest_path = []
            current = current_node

            while current is not None:
                shortest_path.append((current.x, current.y))
                current = current.parent
            return shortest_path[::-1]

        #Finding the neighbour nodes
        neighbours=find_neighbours(maze,current_node)

        #Iterate through neighbours
        for neighbour in neighbours:

            if current_node.g+1<neighbour.g:
                neighbour.update_ana(current_node.g, goal)
                neighbour.parent=current_node
                if (neighbour.g+neighbour.h)<G:
                    flag=1
                    for unexpanded_node in open_list:
                        if(unexpanded_node.x==neighbour.x and unexpanded_node.y==neighbour.y):
                            flag=0
                            unexpanded_node.update_ana(current_node.g,goal_node)
                    if(flag):

                        neighbour.update_ana(current_node.g,goal_node)

                        open_list.append(neighbour)










open_list=[]
#path=[]
def ana_star(maze, start_node, exit_node):

    global open_list
    global shortest_path
    #Create the node matrix
    node_creation()
    #Assign start node
    start=node(start_node[0],start_node[1],3,None)
    start.update_ana(0,exit_node)
    #Append the start to the open list
    open_list.append(start)

    #Assign colours for start and end node
    maze[start_node[0]][start_node[1]] = 3
    maze[exit_node[0]][exit_node[1]] = 3

    a=[]
    z=0
    total_start=t.clock()
    while(len(open_list)!=0):
        print("Global_cost")
        print(G)
        start_time=t.clock()
        z=z+1
        a.append(improvesolution(exit_node))
        end_time=t.clock()
        print("Solution-",z,"=",end_time-start_time)


        for index,elements in enumerate(open_list):

            elements.update(elements.parent.g,exit_node)
            #Prune the states having greater G value
            if(elements.g+elements.h>=(G)):
                k=open_list.pop(index)
        total_end=t.clock()
    print("Total time for anastar",total_end-total_start)

    for j in range(len(a)-1):
        print("Path",j,)
        print a[j]
        if len(a[j])==0:
            continue
        else:
            for i in range(len(a[j])):
                ind=a[j]
                ele=ind[i]
                maze[ele[0]][ele[1]]=5

    #print("Length of solution")
    #print(len(shortest_path))




    '''
    You may use or change the functions as you like.

    For each solution, you have to report:
    1) A list of expanded nodes
    2) A list of the path found from start to goal
    3) The time taken and cost for that solution
    '''

    # This visualizes the grid. You may remove this and use the functions as you wish.
    maze[start_node[0]][start_node[1]] = 3
    maze[exit_node[0]][exit_node[1]] = 4
    draw_canvas(canvas, maze)
    root.update()
    return

def main():
    global G
    '''
    Define start and goal node. You may change how to define the nodes.
    '''
    entrance_node = (row-2, 5)
    exit_node = (0, col-2)

    # If you are using a node class, you may want to convert each maze node to its class here

    '''
    Run your ana_star algorithm function. You may choose to change the function or not use it.
    '''
    #run the ana_star algorithm
    ana_star(maze, entrance_node, exit_node)
    #root.mainloop()
    # start=t.clock()
    # sol,expanded_nodes=a_star(maze, entrance_node, exit_node)
    # end=t.clock()
    # if (sol!=None):
    #     print("Length of astar solution")
    #     print(len(sol))
    #     #print("Timetaken for astar")
    #     #print(end-start)
    #
    # else:
    #     print("No solution found")
    root.mainloop()



if __name__ == '__main__':
    main()