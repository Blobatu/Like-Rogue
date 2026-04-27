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
    width = len(plan[0]) if plan else 0
    height = len(plan)
    neighbors = {'tl': None, 'tr': None, 'bl': None, 'br': None}
    if x != width and y != height:
        neighbors['tl'] = plan[y][x]
        neighbors['tr'] = plan[y][x+1]
        neighbors['bl'] = plan[y+1][x]
        neighbors['br'] = plan[y+1][x+1]
    return neighbors


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
    """
    Generate a level from the vector grid.
    Hard-coded all possible combinations based on which walls are OPEN.
    
    A wall is OPEN if the corner vector points parallel to it:
    - Left/Right wall: open if corner points 'l' or 'r'
    - Top/Bottom wall: open if corner points 'u' or 'd'
    """
    plan = gen_template()
    
    room_height = len(plan) - 1
    room_width = len(plan[0]) - 1
    
    level = []
    for y in range(room_height):
        row = []
        for x in range(room_width):
            tl = plan[y][x]
            tr = plan[y][x + 1]
            bl = plan[y + 1][x]
            br = plan[y + 1][x + 1]
            
            # Determine which walls are OPEN
            left_open = tl in ('l', 'r')
            right_open = tr in ('l', 'r')
            top_open = bl in ('u', 'd')
            bottom_open = br in ('u', 'd')
            
            # All 16 possible combinations of 4 boolean walls
            # 4 walls open
            if left_open and right_open and top_open and bottom_open:
                tile = 'hollow'
            # 3 walls open
            elif left_open and right_open and top_open and not bottom_open:
                tile = '3way_lrb'
            elif left_open and right_open and bottom_open and not top_open:
                tile = '3way_lrt'
            elif left_open and top_open and bottom_open and not right_open:
                tile = '3way_rtb'
            elif right_open and top_open and bottom_open and not left_open:
                tile = '3way_ltb'
            # 2 walls open - opposite (straight)
            elif left_open and right_open and not top_open and not bottom_open:
                tile = 'strgt_horz'
            elif top_open and bottom_open and not left_open and not right_open:
                tile = 'strgt_vert'
            # 2 walls open - adjacent (corner)
            elif left_open and top_open and not right_open and not bottom_open:
                tile = 'crnr_rb'
            elif left_open and bottom_open and not right_open and not top_open:
                tile = 'crnr_rt'
            elif right_open and top_open and not left_open and not bottom_open:
                tile = 'crnr_lb'
            elif right_open and bottom_open and not left_open and not top_open:
                tile = 'crnr_lt'
            # 2 walls open - single opening (dead end)
            elif left_open and not right_open and not top_open and not bottom_open:
                tile = 'end_l'
            elif right_open and not left_open and not top_open and not bottom_open:
                tile = 'end_r'
            elif top_open and not left_open and not right_open and not bottom_open:
                tile = 'end_t'
            elif bottom_open and not left_open and not right_open and not top_open:
                tile = 'end_b'
            # 1 wall open
            elif left_open:
                tile = 'end_l'
            elif right_open:
                tile = 'end_r'
            elif top_open:
                tile = 'end_t'
            elif bottom_open:
                tile = 'end_b'
            # 0 walls open
            else:
                tile = 'void'
            
            row.append(tile)
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

    for i in make_lvl_data(maze):
        print(i)

# code
if __name__ == "__main__":
    #print_template()
    #print(sz_to_wall_sz())
    print_level()