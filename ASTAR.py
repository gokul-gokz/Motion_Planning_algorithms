
from helper_functions import *
def a_star(maze,start,exit):

    start_node=node(start[0],start[1],3,None)
    goal_node=node(exit[0], exit[1], 4, None)

    start_node.update(0,exit)
    goal_node.update(0, exit) #need to be changed

    open_list=[]
    closed_list=[]

    open_list.append(start_node)

    #Loop until the list is empty
    while(len(open_list)>0):
        print("iteration begin")
        current_node=open_list[0]

        current_index=0

        for index,node1 in enumerate(open_list):
            #print("node1.f",node1.f)
            #print("current_node.f", current_node.f)
            if node1.f<current_node.f:
                #print("choosen_node.f", node1.f)
                current_node=node1
                current_index=index
        # print("currentnode")
        # print(current_node.x, current_node.y)
        #
        #
        # print("open")
        # for o in open_list:
        #     print(o.x, o.y)
        #     print("---")
        #
        # print("closed")
        # for o in closed_list:
        #     print(o.x, o.y)
        #     print("---")
        #Remove the current element from the open list
        y=open_list.pop(current_index)
        print("after deleting node,open")
        for o in open_list:
            print(o.x, o.y)
        print("---")

        closed_list.append(y)

        #Check whether the current node is the goal
        #Backtrack the path
        if current_node == goal_node:
           shortest_path=[]
           current=current_node
           while current is not None:
               shortest_path.append((current.x,current.y))
               maze[current.x][current.y] = 5
               current=current.parent
               #current.value=2



           draw_canvas(canvas, maze)
           root.update()
           return shortest_path[::-1] #returns reversed path
        '''print("current")
        print(current_node.x, current_node.y)
        print("---")
        print("Neighbours of",current_node.x,current_node.y)'''

        #Find neighbours of the current node
        neighbours=find_neighbours(maze,current_node)




        # Loop through the neighbours to find which one to expand
        for neighbour in neighbours:
            maze[neighbour.x][neighbour.y]=2
            # Check whether the node is already expanded
            for expanded in closed_list:
                i=0
                if neighbour==expanded:
                    continue

            print("i=",i)
            # update the nodes values
            neighbour.update(current_node.g,exit)

            # Update the open list
            l=len(open_list)
            j=0
            for unexpanded_node in open_list:
                j=j+1
                print(neighbour.x,neighbour.y)
                if neighbour==unexpanded_node:
                    if neighbour.g>unexpanded_node.g:
                        j = j + 5;
                        print "Node already present in closed list and no updates"
                        continue

                    else:
                        j = j + 1;
                        neighbour.g=unexpanded_node.g
                        neighbour.f=unexpanded_node.f
                        neighbour.parent=unexpanded_node.parent
                        continue
            if(j==l):
                print "node not present"
            #print(neighbour.x,neighbour.y)
            # add the child to open list
            for index, node1 in enumerate(open_list):
                # print("node1.f",node1.f)
                # print("current_node.f", current_node.f)
                if node1==neighbour:
                    # print("choosen_node.f", node1.f)
                    current_index = index
                    z=open_list.pop(current_index)
                    break

            if(j == l):
                open_list.append(neighbour)

            for index, node1 in enumerate(closed_list):
                # print("node1.f",node1.f)
                # print("current_node.f", current_node.f)
                if node1==neighbour:
                    # print("choosen_node.f", node1.f)
                    current_index = index
                    z=open_list.pop(len(open_list)-1)
                    break
