import random
import copy
import operator
from time import sleep
from disjoint import disjoint_set

# To avoid newline
def printf(s):
    print(s, end = '')

# Helper class that keeps track of our edges
class corner():
    def __init__(self, north, west, index):
        self.north = north
        self.west = west
        self.index = index

    def get_north(self):
        return self.north

    def get_west(self):
        return self.west

    def set_north(self, val):
        self.north = val

    def set_west(self, val):
        self.west = val

    def get_index(self):
        return self.index

# Helper class that tracks a node in prim
class node():
    def __init__(self, westNorth, south, east):
        self.node = [westNorth, south, east]
    
    def __iter__(self):
        for n in self.node:
            yield n

    def get_indexes(self):
        indexes = []
        for n in self.node:
            indexes.append(n.get_index)
        return indexes
    
    def getNode():
        return self.node;

# Main class for generating a maze based on different algorithms
class mazer():
    def __init__(self, height, width):
        self.width = width + 1
        self.height = height + 1
        # Initalize the edges that will build the maze
        self.maze = self.pop_maze()

    # Filler function for all mazes. This generates a x*y grid with walls between each node
    # A node is considered to be a square with the walls being corners in
    # the following fashion x,y;(left,top) x,y-1;(bottom) x+1,y(right)
    def pop_maze(self):
        sz = self.width*self.height
        self.maze = [None] * sz
        for i in range(sz):
            if (self.get_col(i) < self.width - 1) and (self.get_row(i) < self.height - 1):
                self.maze[i] = corner(1, 1, i)
            elif self.get_col(i) == self.width - 1:
                self.maze[i] = corner(0, 1, i)
            elif self.get_row(i) == self.height - 1:
                self.maze[i] = corner(1, 0, i)
            else:
                self.maze[i] = corner(0, 0, i)
            # Get the edge case out of the way as well
            self.maze[len(self.maze) - 1] = corner(0,0, sz - 1)
        return self.maze

    def get_row(self, index):
        return index // self.width

    def get_col(self, index):
        return index % self.width

    def print_row_col(self, rows, cols):
        for row in rows:
            printf(row)
        printf("\n")
        for col in cols:
            printf(col)
        printf("\n")

    # Prints the current state of the maze
    def print_maze(self, maze):
        rows = [0]*self.width
        cols = [0]*self.width
        for i in range(len(self.maze)):
            north = maze[i].get_north()
            west = maze[i].get_west()
            col = self.get_col(i)
            if north == 1:
                rows[col] = f'{"--".center(4)}'
            else:
                rows[col] = f'{"".center(4)}'
            if west == 1:
                cols[col] = f'{"|".ljust(4)}'
            else:
                cols[col] = f'{"".center(4)}'
            if col == self.width - 1:
                self.print_row_col(rows, cols)

    # Get a random edge left or right of us for x and up or down for y.
    def get_random_edge(self, index, x=True):
        op = random.choice([operator.add, operator.sub])
        if x:
            new_index = op(index, 1)
            return new_index if new_index < self.width - 1 else index - 1
        else:
            new_index = op(index, self.width)
            return new_index if new_index < self.width - 1 else index - self.width

    '''
    Generates the maze from the Kruskal maze generation algorithm

    Choose two nodes that shares a wall vertical or horizontal
    if the cells of that set are not in the same set
    then remove the wall andmerge the two sets
    '''
    def kruskal(self):
        tree = copy.copy(self.maze)
        random.shuffle(tree)
        ds = disjoint_set(self.maze)
        for i in range(len(tree) - 1):
            edge = self.maze[tree.pop().get_index()]
            edgeIndex = edge.get_index()
            x = self.get_col(edgeIndex)
            y = self.get_row(edgeIndex)
            if x > 0 and x < self.width-1:
                neighIndex = self.get_random_edge(edgeIndex)
                parentEdge, neighEdge = ds.find(edge), ds.find(self.maze[neighIndex])
                if parentEdge != neighEdge:
                    if neighIndex > edgeIndex:
                        self.maze[neighIndex].set_west(0)
                    else:
                        self.maze[edgeIndex].set_west(0)
                    ds.union(edge, neighEdge)
            if y > 0 and y < self.height-1:
                neighIndex = self.get_random_edge(edgeIndex,False)
                parentEdge, neighEdge = ds.find(edge), ds.find(self.maze[neighIndex])
                if parentEdge != neighEdge:
                    if neighIndex > edgeIndex:
                        self.maze[neighIndex].set_north(0)
                    else:
                        self.maze[edgeIndex].set_north(0)
                    ds.union(parentEdge, neighEdge)
        return self.maze

    # Returns the neighbouring nodes of a node
    def get_neighbours(self, node):
        indexes = node.get_indexes()
        x,y = self.get_row(indexes[0]), self.get_col(indexes[0])
        # Constructing list of x+1,y; x-1,y; x,y+1; x,y-1;
        # None if we cannot move in that direction
        neighbours = [None, None, None, None] 

        # We can move right
        if x >= 1 and x < self.width - 1:
            neighbours[0] = node(indexes[2], indexes[2] + self.width, indexes[2] + 1), 
        # We can move left
        if x > 1 and x <= self.width - 1:
            neighbours[1] = node(indexes[0] - 1, indexes[0] + self.width, indexes[0]), 
        # We can move up
        if y > 1 and y <= self.height -1:
            neighbours[2] = node(indexes[0] - self.width, indexes[0], indexes[0] - self.width + 1)
        # We can move down 
        if y >= 1 and y < self.height :
            neighbours[3] = node(indexes[0] + self.width, indexes[0] + self.width*2 , indexes[0] + self.width + 1)

