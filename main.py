#!/usr/bin/env python3
from maze import mazer

height = 3 
width  = 3

maze = mazer(height, width)
maze.print_maze(maze.prims())

#maze.print_maze(maze.kruskal())

