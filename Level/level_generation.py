"""

"""


# import
from .levels import levels as lv
from .cor_tile import tileset as ts
import random as rd


# constantes/variables
current_level = 'level_3'
size = lv[current_level]['size']


# fonctions

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


def print_room(maze):
    """
    prints the actual level as it will appears in the game
    in: list of lists of rooms from maze generator
    out: lines of the level being printed out one by one
    """
    for i in make_lvl_data(maze):
        print(i)
    
    
def print_room_as_list(maze):
    """
    to debug, simply prints the result of maze_to_lvl_data, kinda useless but has clear labeling
    in: list of lists of rooms from maze generator
    out: list of strings, each list is a line of the level 
    """
    print(make_lvl_data(maze))

def choose_dir(x, y, maze, row, dir_ =['u', 'd', 'l', 'r']):
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


def print_level(maze = gen_maze()):
    """
    prints the actual level as it will appears in the game
    in: list of lists of rooms from maze generator
    out: lines of the level being printed out one by one
    """
    for i in make_lvl_data(maze):
        print(i)

def level(maze = gen_maze()):
    level = make_lvl_data(maze)
    return level

def full_level(maze=gen_maze(), enn_spwn = int(lv[current_level]['difficulty'] * 2.5), loot = int(lv[current_level]['difficulty'] + 1), traps = int(lv[current_level]['difficulty'] * 1.5)):
    lvl_data = make_lvl_data(maze)
    
    tile_positions = [(y, tile_x) for y, line in enumerate(lvl_data) for tile_x in range(0, len(line), 2) if tile_x + 1 < len(line) and line[tile_x] != '#' and line[tile_x + 1] != '#']
    
    chest_positions = [(y, tile_x) for y, tile_x in tile_positions if y > 0 and lvl_data[y-1][tile_x:tile_x+2] == '##']
    
    total_tiles = len(tile_positions)
    enn_count = min(enn_spwn, total_tiles // 2)
    chest_count = min(loot, len(chest_positions))
    trap_count = min(traps, total_tiles // 5)
    
    all_selected = []
    
    if enn_count > 0:
        all_selected.extend(rd.sample(tile_positions, enn_count))

    if chest_count > 0:
        available = [p for p in chest_positions if p not in all_selected]
        if available:
            all_selected.extend(rd.sample(available, min(chest_count, len(available))))

    if trap_count > 0 and lv[current_level]['difficulty'] >= 5:
        available = [p for p in tile_positions if p not in all_selected]
        if available:
            all_selected.extend(rd.sample(available, min(trap_count, len(available))))
    
    new_data = [list(line) for line in lvl_data]
    enemy_positions = all_selected[:enn_count]
    chest_selected = all_selected[enn_count:enn_count + chest_count]
    
    for y, tile_x in all_selected:
        if (y, tile_x) in chest_positions:
            new_data[y][tile_x:tile_x+2] = list('[]')
        elif (y, tile_x) in all_selected[enn_count + chest_count:]:
            new_data[y][tile_x:tile_x+2] = ['△', ' ']
        else:
            new_data[y][tile_x:tile_x+2] = ['&', '&']
    
    return [''.join(line) for line in new_data]

def print_full():
    for i in full_level():
        print(i)

# test

fullscreen_layout_template = [[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16], [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]]
test_1 = [['end_b','','','','crnr_rb','3way_lrb','3way_lrb','strgt_horz','end_l','crnr_wall_rb','wall_t','crnr_wall_lb','crnr_rb','3way_lrb','crnr_lb',''], ['strgt_vert','','end_r','3way_lrb','crnr_lt','crnr_rt','cross-rb','wall_t','wall_t','empty+lt','pillar','empty+rt','cross-lb','cross_pillar','3way_ltb',''], ['3way_rtb','strgt_horz','strgt_horz','cross','strgt_horz','3way_lrb','door_l','empty','empty','empty','empty','empty','cross-lt','3way_lrt','crnr_lt',''], ['3way_ltb','crnr_wall_rb','wall_t','door_t','crnr_wall_lb','end_t','wall_l','empty','full','full','empty','empty','end_t','crnr_wall_rb','wall_t','crnr_wall_lb'], ['strgt_vert','crnr_wall_rt','door_b','empty+lb','door_r','crnr_lb','wall_l','empty','empty','empty+rb','wall_b','empty+lb','empty','empty','empty','wall_r'], ['strgt_vert','hollow','strgt_vert','crnr_wall_rt','crnr_wall_lt','strgt_vert','crnr_wall_rt','door_b','wall_b','crnr_wall_lt','crnr_rb','cross-rt','wall_b','empty+lb','empty','wall_r'], ['crnr_rt','strgt_horz','3way_lrt','strgt_horz','strgt_horz','3way_lrt','strgt_horz','crnr_lt','','crnr_rb','3way_lrt','3way_lrt','end_l','crnr_wall_rt','wall_b','crnr_wall_lt']]

#print_room(test_1)
#print_room_as_list(test_1)

if __name__ == "__main__":
    #print_level()
    print_full()