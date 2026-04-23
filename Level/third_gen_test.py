from cor_tile import tileset as ts
from cor_tile import tile_rules as tr
import random as rd

dir_ = ['u', 'd', 'l', 'r']
size = (16, 7)


def choose_dir(x, y, maze, row):
    width, height = size
    while True:
        wall = rd.choice(dir_)
        if y == 0 and wall == 'u':
            continue
        if y == height - 1 and wall == 'd':
            continue
        if x == 0 and wall == 'l':
            continue
        if x == width - 1 and wall == 'r':
            continue
        if y > 0 and wall == 'u' and maze[y-1][x] == 'd':
            continue
        if x > 0 and wall == 'l' and row[x-1] == 'r':
            continue
        
        return wall


def gen_template():
    maze = []
    for y in range(size[1]):
        row = []
        for x in range(size[0]):
            wall = choose_dir(x, y, maze, row)
            row.append(wall)
        maze.append(row)
    return maze


def print_template(maze = gen_template()):
    for i in maze:
        print(i)

def get_near(plan, x, y):
    width = len(plan[0]) if plan else 0
    height = len(plan)
    neighbors = {}
    if y > 0:
        neighbors['u'] = plan[y-1][x]
    if y < height - 1:
        neighbors['d'] = plan[y+1][x]
    if x > 0:
        neighbors['l'] = plan[y][x-1]
    if x < width - 1:
        neighbors['r'] = plan[y][x+1]
    neighbors['s'] = plan[y][x]
    return neighbors

def gen_maze():
    plan = gen_template()
    for y in range(len(plan)):
        for x in range(len(plan[y])):
            tiles = get_near(plan, x, y)
            print(tiles)
            #match tiles:
            #    case  

print_template()

gen_maze()