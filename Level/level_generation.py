"""
Code responsable de la génération des niveaux
par Antoine D-C
"""


# import
from .levels import levels as lv
from .cor_tile import tileset as ts
from .cor_tile import tile_rules as tr
import random as rd


# constantes/variables
current_level = 'level_3'
size = lv[current_level]['size']
WALL = '#'
PATH = ' '

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


def print_room(maze: list[list[str]]):
    """
    prints the actual level as it will appears in the game
    in: list of lists of rooms from maze generator
    out: lines of the level being printed out one by one
    """
    for i in make_lvl_data(maze):
        print(i)
    
    
def print_room_as_list(maze: list[list[str]]):
    """
    to debug, simply prints the result of maze_to_lvl_data, kinda useless but has clear labeling
    in: list of lists of rooms from maze generator
    out: list of strings, each list is a line of the level 
    """
    print(make_lvl_data(maze))

def generate_maze(width, height):
    maze_width = width * 3
    maze_height = height * 3
    maze = [[WALL for _ in range(maze_width)] for _ in range(maze_height)]

    def carve_passages(cx, cy):
        maze_center_y = cy * 3 + 1
        maze_center_x = cx * 3 + 1
        maze[maze_center_y][maze_center_x] = PATH
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        rd.shuffle(directions)

        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < width and 0 <= ny < height:
                neighbor_center_y = ny * 3 + 1
                neighbor_center_x = nx * 3 + 1
                if maze[neighbor_center_y][neighbor_center_x] == WALL:
                    if dx == 1:
                        maze[maze_center_y][maze_center_x + 1] = PATH
                        maze[neighbor_center_y][neighbor_center_x - 1] = PATH
                    elif dx == -1:
                        maze[maze_center_y][maze_center_x - 1] = PATH
                        maze[neighbor_center_y][neighbor_center_x + 1] = PATH
                    elif dy == 1:
                        maze[maze_center_y + 1][maze_center_x] = PATH
                        maze[neighbor_center_y - 1][neighbor_center_x] = PATH
                    elif dy == -1:
                        maze[maze_center_y - 1][maze_center_x] = PATH
                        maze[neighbor_center_y + 1][neighbor_center_x] = PATH
                    
                    carve_passages(nx, ny)
    
    carve_passages(0, 0)
    return maze


def check_around(maze, pos):
    height = len(maze)
    width = len(maze[0])
    x, y = pos 
    
    neighbors = {'u': None, 'd': None, 'l': None, 'r': None}
    
    if 0 <= y-1 < height and 0 <= x < width:
        neighbors['u'] = maze[y-1][x]
    if 0 <= y+1 < height and 0 <= x < width:
        neighbors['d'] = maze[y+1][x]
    if 0 <= y < height and 0 <= x-1 < width:
        neighbors['l'] = maze[y][x-1]
    if 0 <= y < height and 0 <= x+1 < width:
        neighbors['r'] = maze[y][x+1]
    
    return neighbors

def make_level(maze=generate_maze(size[0], size[1])):
    center_rows = [row for i, row in enumerate(maze) if i % 3 == 1]
    
    center_positions = []
    for row_idx, row in enumerate(center_rows):
        center_row = [cell for j, cell in enumerate(row) if j % 3 == 1]
        for col_idx, cell in enumerate(center_row):
            full_y = row_idx * 3 + 1
            full_x = col_idx * 3 + 1
            center_positions.append((full_x, full_y))
    
    level = []
    for pos in center_positions:
        t = check_around(maze, pos)
        wall = []
        gen = []
        
        if t['u'] == '#': wall.append('up')
        else: gen.append('up')
        if t['d'] == '#': wall.append('down')
        else: gen.append('down')
        if t['l'] == '#': wall.append('left')
        else: gen.append('left')
        if t['r'] == '#': wall.append('right')
        else: gen.append('right')
        
        matching_tile = 'void'
        for tile_name, rules in tr.items():
            if sorted(rules['gen']) == sorted(gen) and sorted(rules['wall']) == sorted(wall):
                matching_tile = tile_name
                break
        
        level.append(matching_tile)
    
    level_grid = [level[i:i+16] for i in range(0, len(level), 16)]
    return level_grid




def print_level(maze: list[list[str]] = make_level()):
    """
    prints the actual level as it will appears in the game
    in: list of lists of rooms from maze generator
    out: lines of the level being printed out one by one
    """
    for i in make_lvl_data(maze):
        print(i)

def level(maze: list[list[str]] = make_level()):
    level = make_lvl_data(maze)
    return level

def full_level(maze: list[list[str]] = make_level(), 
               enn_spwn = int(lv[current_level]['difficulty'] * 2.5), 
               loot = int(lv[current_level]['difficulty'] + 1), 
               traps = int(lv[current_level]['difficulty'] * 1.5)):
    lvl_data = make_lvl_data(maze)


    center_row_cell = len(maze) // 2
    center_row_line = center_row_cell * 7 + 3
    
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
            new_data[y][tile_x:tile_x+2] = ['&', ' ']
    
    exit_line = center_row_line
    exit_start_col = 222
    player_start_col = 6
    new_data[exit_line][exit_start_col:exit_start_col+2] = ['|','|']
    new_data[exit_line][player_start_col:player_start_col+2] = ['@',' ']
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