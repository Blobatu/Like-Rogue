from cor_tile import tileset as ts
from levels import levels as lev
import random as rd


def get_size():
    size = lev['level_1']['size']
    return size


def sz_to_wall_sz(size = get_size()):
    len_ = size[0] +1
    wid_ = size[1] +1
    sz = (len_, wid_)    
    return sz


def choose_dir(x, y, maze, row, dir_ = ['u', 'd', 'l', 'r']):
    width, height = get_size()
    candidates = []

    for wall in dir_:
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
        candidates.append(wall)

    if not candidates:
        candidates = choose_dir(x, y, maze, row)

    return rd.choice(candidates)


def gen_template(size = get_size()):
    while True:
        try:
            maze = []
            for y in range(size[1]):
                row = []
                for x in range(size[0]):
                    wall = choose_dir(x, y, maze, row)
                    row.append(wall)
                maze.append(row)
            break
        except:
            continue
    return maze


def print_template(maze = gen_template()):
    for i in maze:
        print(i)



# code
if __name__ == "__main__":
    print_template()
    print(sz_to_wall_sz())