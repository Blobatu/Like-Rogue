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
            t = get_near(gen_template(), x, y)
            if t['tl'] == 'r':
                if t['tr'] == 'd' and t['br'] == 'l' and t['bl'] == 'u':
                    row.append('hollow')
                if (t['tr'] != 'd' and t['br'] == 'l' and t['bl'] != 'u') or (t['tr'] != 'd' and t['br'] != 'l' and t['bl'] == 'r'):
                    row.append('strgt_horz')
                if (t['tr'] == 'd' and t['br'] == 'l' and t['bl'] != 'u') or (t['tr'] != 'd' and t['br'] == 'u' and t['bl'] == 'r'):
                    row.append('end_l')
                if (t['tr'] != 'd' and t['br'] == 'l' and t['bl'] == 'u'):
                    row.append('end_r')
            if t['tl'] == 'd': 
                pass #delete after the ifs are done
            if t['tl'] == 'u' or t['tl'] == 'r':
                pass #delete after the ifs are done
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