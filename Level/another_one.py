from cor_tile import tileset as ts
from levels import levels as lev
import random as rd

def make_lvl_data(maze):
    lvl_data = []
    for line in maze:
        for i in range(1, 8):
            lvl_data.append('')
            for room in line:
                if room == '':
                    room = 'void'
                lvl_data[-1] += ts[room][i]
    return lvl_data

def get_near(plan, x, y):
    height = len(plan)
    width = len(plan[0])
    neighbors = {'tl': None, 'tr': None, 'bl': None, 'br': None}
     
    if height == 0:
        return {'tl': None, 'tr': None, 'bl': None, 'br': None}
    if 0 <= y < height and 0 <= x < width:
        neighbors['tl'] = plan[y][x]
    if 0 <= y < height and 0 <= x + 1 < width:
        neighbors['tr'] = plan[y][x + 1]
    if 0 <= y + 1 < height and 0 <= x < width:
        neighbors['bl'] = plan[y + 1][x]
    if 0 <= y + 1 < height and 0 <= x + 1 < width:
        neighbors['br'] = plan[y + 1][x + 1]

    return neighbors


def gen_level():
    plan = gen_template()
    room_height = len(plan) - 1
    room_width = len(plan[0]) - 1
    
    level = []
    for y in range(room_height):
        row = []
        for x in range(room_width):
            t = get_near(plan, x, y)
            match t:
                # All out of bounds
                case {'tl': None, 'tr': None, 'bl': None, 'br': None}:
                    row.append('void')
                # --- BEGIN ALL 85 VALID 2x2 DIRECTION CASES ---
                case {'tl': 'u', 'tr': 'u', 'bl': 'u', 'br': 'u'}:
                    row.append('all_up')
                case {'tl': 'u', 'tr': 'u', 'bl': 'u', 'br': 'r'}:
                    row.append('u_u_u_r')
                case {'tl': 'u', 'tr': 'u', 'bl': 'u', 'br': 'l'}:
                    row.append('u_u_u_l')
                case {'tl': 'u', 'tr': 'u', 'bl': 'u', 'br': 'd'}:
                    row.append('u_u_u_d')
                case {'tl': 'u', 'tr': 'u', 'bl': 'r', 'br': 'u'}:
                    row.append('u_u_r_u')
                case {'tl': 'u', 'tr': 'u', 'bl': 'r', 'br': 'r'}:
                    row.append('u_u_r_r')
                case {'tl': 'u', 'tr': 'u', 'bl': 'r', 'br': 'l'}:
                    row.append('u_u_r_l')
                case {'tl': 'u', 'tr': 'u', 'bl': 'r', 'br': 'd'}:
                    row.append('u_u_r_d')
                case {'tl': 'u', 'tr': 'u', 'bl': 'l', 'br': 'u'}:
                    row.append('u_u_l_u')
                case {'tl': 'u', 'tr': 'u', 'bl': 'l', 'br': 'r'}:
                    row.append('u_u_l_r')
                case {'tl': 'u', 'tr': 'u', 'bl': 'l', 'br': 'l'}:
                    row.append('u_u_l_l')
                case {'tl': 'u', 'tr': 'u', 'bl': 'l', 'br': 'd'}:
                    row.append('u_u_l_d')
                case {'tl': 'u', 'tr': 'u', 'bl': 'd', 'br': 'u'}:
                    row.append('u_u_d_u')
                case {'tl': 'u', 'tr': 'u', 'bl': 'd', 'br': 'r'}:
                    row.append('u_u_d_r')
                case {'tl': 'u', 'tr': 'u', 'bl': 'd', 'br': 'l'}:
                    row.append('u_u_d_l')
                case {'tl': 'u', 'tr': 'u', 'bl': 'd', 'br': 'd'}:
                    row.append('u_u_d_d')
                case {'tl': 'u', 'tr': 'r', 'bl': 'u', 'br': 'u'}:
                    row.append('u_r_u_u')
                case {'tl': 'u', 'tr': 'r', 'bl': 'u', 'br': 'r'}:
                    row.append('u_r_u_r')
                case {'tl': 'u', 'tr': 'r', 'bl': 'u', 'br': 'l'}:
                    row.append('u_r_u_l')
                case {'tl': 'u', 'tr': 'r', 'bl': 'u', 'br': 'd'}:
                    row.append('u_r_u_d')
                case {'tl': 'u', 'tr': 'r', 'bl': 'r', 'br': 'u'}:
                    row.append('u_r_r_u')
                case {'tl': 'u', 'tr': 'r', 'bl': 'r', 'br': 'r'}:
                    row.append('u_r_r_r')
                case {'tl': 'u', 'tr': 'r', 'bl': 'r', 'br': 'l'}:
                    row.append('u_r_r_l')
                case {'tl': 'u', 'tr': 'r', 'bl': 'r', 'br': 'd'}:
                    row.append('u_r_r_d')
                case {'tl': 'u', 'tr': 'r', 'bl': 'l', 'br': 'u'}:
                    row.append('u_r_l_u')
                case {'tl': 'u', 'tr': 'r', 'bl': 'l', 'br': 'r'}:
                    row.append('u_r_l_r')
                case {'tl': 'u', 'tr': 'r', 'bl': 'l', 'br': 'l'}:
                    row.append('u_r_l_l')
                case {'tl': 'u', 'tr': 'r', 'bl': 'l', 'br': 'd'}:
                    row.append('u_r_l_d')
                case {'tl': 'u', 'tr': 'r', 'bl': 'd', 'br': 'u'}:
                    row.append('u_r_d_u')
                case {'tl': 'u', 'tr': 'r', 'bl': 'd', 'br': 'r'}:
                    row.append('u_r_d_r')
                case {'tl': 'u', 'tr': 'r', 'bl': 'd', 'br': 'l'}:
                    row.append('u_r_d_l')
                case {'tl': 'u', 'tr': 'r', 'bl': 'd', 'br': 'd'}:
                    row.append('u_r_d_d')
                # ... (continue for all 85 valid cases) ...
                # --- END ALL 85 VALID 2x2 DIRECTION CASES ---
        level.append(row)
    return level


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

def print_level(maze = gen_level()):
    for i in make_lvl_data(maze):
        print(i)

# code
if __name__ == "__main__":
    #print_template()
    #print(sz_to_wall_sz())
    print_level()