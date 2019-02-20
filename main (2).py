
from algorithms import*

def main():

    '''
    Define start and goal node. You may change how to define the nodes.
    '''
    entrance_node = (row-2, 3)
    exit_node = (0, col-2)


    # run the ana_star algorithm
    #ana_star(maze, entrance_node, exit_node)
    sol=a_star(maze, entrance_node, exit_node)
    #print(list(sol))
    root.mainloop()

if __name__ == '__main__':
    main()