#!/usr/bin/env python3
from maze import mazer

height = 10
width  = 10

maze = mazer(height, width)
maze.print_maze(maze.kruskal())

