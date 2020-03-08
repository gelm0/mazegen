Small python application for generating mazes.

Can currently generate mazes with the following algorihms

    * Kruskals Algorithm

Usage:

from maze import mazer

mazer = mazer(10,10)
maze = mazer.kruskal()
maze.print()
