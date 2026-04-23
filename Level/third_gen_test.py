from cor_tile import tileset as ts
from cor_tile import tile_rules as tr
import random as rd

dir_ = ['u', 'd', 'l', 'r']
size = (16, 7)


def choose_dir(x, y, maze, row):
    width, height = size
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


def gen_template():
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

def get_near(plan, x, y):
    width = len(plan[0]) if plan else 0
    height = len(plan)
    neighbors = {'u': None, 'd': None, 'l': None, 'r': None, 's': None}
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
    maze = []#['' for i in range(len(plan))]
    for y in range(len(plan)):
        row = []#['' for i in range(len(plan[y]))]
        for x in range(len(plan[y])):
            t = get_near(plan, x, y)
            if t['s'] == 'u':
                if t['d'] == 'u' and t['l'] == 'r' and t['r'] == 'l':
                    row.append('cross')
                if t['d'] != 'u' and t['l'] == 'r' and t['r'] == 'l':
                    row.append('3way_lrt')
                if t['d'] == 'u' and t['l'] != 'r' and t['r'] == 'l':
                    row.append('3way_rtb')
                if t['d'] == 'u' and t['l'] == 'r' and t['r'] != 'l':
                    row.append('3way_ltb')
                if t['d'] != 'u' and t['l'] != 'r' and t['r'] == 'l':
                    row.append('crnr_rt')
                if t['d'] != 'u' and t['l'] == 'r' and t['r'] != 'l':
                    row.append('crnr_lt')
                if t['d'] == 'u' and t['l'] != 'r' and t['r'] != 'l':
                    row.append('strgt_vert')
                if t['d'] != 'u' and t['l'] != 'r' and t['r'] != 'l':
                    row.append('end_t')
            if t['s'] == 'd':
                if t['u'] == 'd' and t['l'] == 'r' and t['r'] == 'l':
                    row.append('cross')
                if t['u'] != 'd' and t['l'] == 'r' and t['r'] == 'l':
                    row.append('3way_lrb')
                if t['u'] == 'd' and t['l'] != 'r' and t['r'] == 'l':
                    row.append('3way_rtb')
                if t['u'] == 'd' and t['l'] == 'r' and t['r'] != 'l':
                    row.append('3way_ltb')
                if t['u'] != 'd' and t['l'] != 'r' and t['r'] == 'l':
                    row.append('crnr_rb')
                if t['u'] != 'd' and t['l'] == 'r' and t['r'] != 'l':
                    row.append('crnr_lb')
                if t['u'] == 'd' and t['l'] != 'r' and t['r'] != 'l':
                    row.append('strgt_vert')
                if t['u'] != 'd' and t['l'] != 'r' and t['r'] != 'l':
                    row.append('end_b')
            if t['s'] == 'l':
                if t['d'] == 'u' and t['u'] == 'd' and t['r'] == 'l':
                    row.append('cross')
                if t['d'] != 'u' and t['u'] == 'd' and t['r'] == 'l':
                    row.append('3way_lrt')
                if t['d'] == 'u' and t['u'] != 'd' and t['r'] == 'l':
                    row.append('3way_lrb')
                if t['d'] == 'u' and t['u'] == 'd' and t['r'] != 'l':
                    row.append('3way_ltb')
                if t['d'] != 'u' and t['u'] != 'd' and t['r'] == 'l':
                    row.append('strgt_horz')
                if t['d'] != 'u' and t['u'] == 'd' and t['r'] != 'l':
                    row.append('crnr_lt')
                if t['d'] == 'u' and t['u'] != 'd' and t['r'] != 'l':
                    row.append('crnr_lb')
                if t['d'] != 'u' and t['u'] != 'd' and t['r'] != 'l':
                    row.append('end_l')
            if t['s'] == 'r':
                if t['d'] == 'u' and t['u'] == 'd' and t['l'] == 'r':
                    row.append('cross')
                if t['d'] != 'u' and t['u'] == 'd' and t['l'] == 'r':
                    row.append('3way_lrt')
                if t['d'] == 'u' and t['u'] != 'd' and t['l'] == 'r':
                    row.append('3way_lrb')
                if t['d'] == 'u' and t['u'] == 'd' and t['l'] != 'r':
                    row.append('3way_rtb')
                if t['d'] != 'u' and t['u'] != 'd' and t['l'] == 'r':
                    row.append('strgt_horz')
                if t['d'] != 'u' and t['u'] == 'd' and t['l'] != 'r':
                    row.append('crnr_rt')
                if t['d'] == 'u' and t['u'] != 'd' and t['l'] != 'r':
                    row.append('crnr_rb')
                if t['d'] != 'u' and t['u'] != 'd' and t['l'] != 'r':
                    row.append('end_r')
        maze.append(row)
    return maze


def print_maze(maze = gen_maze()):
    for i in maze:
        print(i)




# imp

def make_lvl_data(maze):
    """
    gets a list from the maze generator and stitches rooms together to create the actual level data
    in: list of lists of rooms from maze generator
    out: list of strings, each list is a line of the level
    """
    lvl_data = []
    for line in maze:
        for i in range(1, 8):
            lvl_data.append('')
            for room in line:
                if room =='':
                    room = 'void'   
                lvl_data[-1] += ts[room][i]
    return lvl_data

def print_room(maze = gen_maze()):
    """
    prints the actual level as it will appears in the game
    in: list of lists of rooms from maze generator
    out: lines of the level being printed out one by one
    """
    for i in make_lvl_data(maze):
        print(i)

#print_template()
#print_maze()

print_room()
