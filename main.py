import argparse
from maze import mazer

def main():
    parser = argparse.ArgumentParser(
            description='Prints a maze via asciiart generated by\
                        the Kruskal maze algoritm')
    parser.add_argument('--height', type=int, default=4,
                        help='Height of the maze')
    parser.add_argument('--width', type=int, default=4,
                        help='Width of the maze')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Verbose output')
    args = parser.parse_args()

    if args.verbose:
        print()
        print(f'Generating maze of {args.height} height and {args.width} width')
        print()

    maze = mazer(args.height, args.width)
    maze.print_maze(maze.kruskal())

if __name__ == '__main__':
    main()

