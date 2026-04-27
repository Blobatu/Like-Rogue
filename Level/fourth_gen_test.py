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
    width = len(plan[0]) if plan else 0
    height = len(plan)
    neighbors = {'tl': None, 'tr': None, 'bl': None, 'br': None}
    if x != width and y != height:
        neighbors['tl'] = plan[y][x]
        neighbors['tr'] = plan[y][x+1]
        neighbors['bl'] = plan[y+1][x]
        neighbors['br'] = plan[y+1][x+1]
    return neighbors

def gen_level():
    plan = gen_template()
    level = []
    for y in range(len(plan)):
        if y == len(plan):
            continue
        row = []
        for x in range(len(plan[y])):
            if x == len(plan[y]):
                continue
            w = get_near(plan, x, y)
            # Assign tiles based on the combination of walls around
            # r = right, l = left, u = up, d = down
            # corners: tl, tr, bl, br
            # If all directions open
            if w['tl'] in ('r', 'd', 'l', 'u'):
                # Cross (all open)
                if w['tl'] == 'r' and w['tr'] == 'd' and w['bl'] == 'u' and w['br'] == 'l':
                    row.append('hollow')
                # Horizontal straight
                elif w['tl'] == 'r' and w['tr'] == 'r' and w['bl'] == 'r' and w['br'] == 'r':
                    row.append('strgt_horz')
                # Vertical straight
                elif w['tl'] == 'd' and w['tr'] == 'd' and w['bl'] == 'd' and w['br'] == 'd':
                    row.append('strgt_vert')
                # End right
                elif w['tl'] == 'r' and w['tr'] != 'd' and w['bl'] == 'u' and w['br'] == 'l':
                    row.append('end_r')
                # End left
                elif w['tl'] == 'l' and w['tr'] == 'd' and w['bl'] == 'u' and w['br'] != 'l':
                    row.append('end_l')
                # End bottom
                elif w['tl'] == 'd' and w['tr'] == 'd' and w['bl'] != 'u' and w['br'] == 'l':
                    row.append('end_b')
                # End top
                elif w['tl'] == 'u' and w['tr'] == 'd' and w['bl'] == 'u' and w['br'] != 'l':
                    row.append('end_t')
                # Corner left-bottom
                elif w['tl'] == 'l' and w['tr'] == 'd' and w['bl'] != 'u' and w['br'] == 'l':
                    row.append('crnr_lb')
                # Corner left-top
                elif w['tl'] == 'l' and w['tr'] == 'l' and w['bl'] == 'u' and w['br'] == 'l':
                    row.append('crnr_lt')
                # Corner right-bottom
                elif w['tl'] == 'r' and w['tr'] == 'd' and w['bl'] == 'r' and w['br'] != 'l':
                    row.append('crnr_rb')
                # Corner right-top
                elif w['tl'] == 'r' and w['tr'] == 'r' and w['bl'] == 'u' and w['br'] == 'r':
                    row.append('crnr_rt')
                # 3-way left-right-top
                elif w['tl'] == 'l' and w['tr'] == 'l' and w['bl'] == 'u' and w['br'] == 'r':
                    row.append('3way_lrt')
                # 3-way left-right-bottom
                elif w['tl'] == 'l' and w['tr'] == 'd' and w['bl'] == 'l' and w['br'] == 'l':
                    row.append('3way_lrb')
                # 3-way left-top-bottom
                elif w['tl'] == 'l' and w['tr'] == 'l' and w['bl'] == 'd' and w['br'] == 'l':
                    row.append('3way_ltb')
                # 3-way right-top-bottom
                elif w['tl'] == 'r' and w['tr'] == 'd' and w['bl'] == 'r' and w['br'] == 'd':
                    row.append('3way_rtb')
                # Cross
                elif w['tl'] == 'd' and w['tr'] == 'r' and w['bl'] == 'l' and w['br'] == 'u':
                    row.append('cross')
                else:
                    row.append('void')
            else:
                row.append('void')
        level.append(row)
    return level
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