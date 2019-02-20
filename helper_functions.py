from nodes import *
def find_neighbours(maze,node2):
    '''Four neighbour approach'''
    actions=[(0,-1),(0,1),(-1,0),(1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
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
        new_node=node(neighbour_node_position[0],neighbour_node_position[1],3,node2)

        # Append it with the neighbour list
        neighbours.append(new_node)

    return neighbours


E=99999999
open_list=[]


def improvesolution(goal):
    global open_list
    global E
    global shortest_path
    goal_node=goal
    closed_list = []

    while(len(open_list)>0):
        current_node=open_list[0]
        print(current_node.e)

        for index,element in enumerate(open_list):
            current_index=0
            if element.e>current_node.e:
                current_node=element
                current_index=index

        current_node=open_list.pop(current_index)
        # maze[current_node.x][current_node.y] = 5
        # draw_canvas(canvas, maze)
        # root.update()
        closed_list.append(current_node)

        print (current_node.x,current_node.y)

        if current_node.e<E:
            E=current_node.e
            print("Currnt E=",current_node.e)

        if current_node.x==goal_node[0] and current_node.y==goal_node[1]:
            global G
            G=current_node.g
            print("goal")
            # Backtrack the path


            current = current_node
            while current is not None:
                shortest_path.append((current.x, current.y))
                current = current.parent
                    # current.value=2
                print "asfhabhsavcfhsajvchlsajvhlsaygvlahysgdlaiusgdluaisgdluugida"
            #print shortest_path
            return shortest_path

        neighbours=find_neighbours(maze,current_node)
        print("Current_node.g",current_node.g)


        for neighbour in neighbours:
            print("Neighbour",neighbour.x,neighbour.y)
            print("Neighbour.g",neighbour.g)
            print("----")
            for expanded in closed_list:
                flag=0
                if neighbour==expanded:
                    flag=1
                    break
            if(flag):
                continue
            neighbour.update_ana(current_node.g+1,goal)
            maze[neighbour.x][neighbour.y] = 2
            if current_node.g+1<neighbour.g:
                neighbour.g=current_node.g+1
                neighbour.parent=current_node
                if (neighbour.g+neighbour.h)<G:
                    flag=1
                    for unexpanded_node in open_list:
                        if(unexpanded_node.x==neighbour.x and unexpanded_node.y==neighbour.y):
                            flag=0
                            unexpanded_node.update_ana(current_node.g,goal_node)
                            break

                    if(flag):
                        node1=node(neighbour.x,neighbour.y,5,current_node)
                        node1.update_ana(current_node.g,goal_node)

                        open_list.append(node1)

                        print(node1.x,node1.y)



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

