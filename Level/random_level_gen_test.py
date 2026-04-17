from .level_generation import make_lvl_data
import random as rd
from .tileset import tileset as ts


# because importing it wouldn't work, somehow
def print_room(maze):
    for i in make_lvl_data(maze):
        print(i)


# generation de niveau aléatoire 

tiles = []              # crée une liste des tuiles pour les choisir aléatoirement
for t in ts:            #
    tiles.append(t)     #


## make a list of all valid tiles when on the left wall
out_left = ['void', 'full', 'hollow', 'strgt_vert', 'end_r', 'end_b', 'end_t', 'crnr_rb', 'crnr_rt', '3way_rtb', 'wall_l', 'crnr_wall_rb', 'crnr_wall_rt', 'crnr_door_t_rb', 'crnr_door_b_rt'] 
out_right = ['void', 'full', 'hollow', 'strgt_vert', 'end_l', 'end_b', 'end_t', 'crnr_lb', 'crnr_lt', '3way_ltb', 'wall_r', 'crnr_wall_lb', 'crnr_wall_lt', 'crnr_door_t_lb','crnr_door_b_lt']
out_top = ['void', 'full', 'hollow', 'strgt_horz', 'end_r', 'end_b', 'end_l', 'crnr_rb', 'crnr_lb', '3way_lrb', 'wall_t', 'crnr_wall_rb', 'crnr_wall_lb', 'crnr_door_r_lb', 'crnr_door_l_rb'] 
out_bottom = ['void', 'full', 'hollow', 'strgt_horz', 'end_l', 'end_r', 'end_t', 'crnr_lt', 'crnr_rt', '3way_lrt', 'wall_b', 'crnr_wall_rt', 'crnr_wall_lt', 'crnr_door_r_lt','crnr_door_l_rt']


def valid(x, y, maze,):
    width = len(maze[0])
    height = len(maze)

    check = {
        'left': maze[y][x-1] if x > 0 else 'out',
        'right': maze[y][x+1] if x < width - 1 else 'out',
        'up': maze[y-1][x] if y > 0 else 'out',
        'down': maze[y+1][x] if y < height - 1 else 'out',
        'up_left': maze[y-1][x-1] if x > 0 and y > 0 else 'out',
        'up_right': maze[y-1][x+1] if x < width - 1 and y > 0 else 'out',
        'down_left': maze[y+1][x-1] if x > 0 and y < height - 1 else 'out',
        'down_right': maze[y+1][x+1] if x < width - 1 and y < height - 1 else 'out',
        'current': maze[y][x],
    }
    
    for i in check:
        if check[i] == 'void':
           check[i] = 'out'

    if check['left'] == 'out' and check['current'] not in out_left:     ## repeat this style of check for all rules
        return out_left
    
    if check['right'] == 'out' and check['current'] not in out_right:
        return out_right
    
    if check['up'] == 'out' and check['current'] not in out_top:
        return out_top
    
    if check['down'] == 'out' and check['current'] not in out_bottom:
        return out_bottom


    else:
        return 'ok'   ## returns a signal that the tile is valid



def random_pattern(width, height):
    maze = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(rd.choice(tiles))
        maze.append(row)
    return maze


def generate_level(width, height):
    maze = random_pattern(width, height)
    for y in range (height):
        for x in range (width):
            current_check = valid(x, y, maze)
            while current_check != 'ok':            ## check this part of the code, it may not be correct
                maze[y][x] = rd.choice(current_check)
                current_check = valid(x, y, maze)
    return maze


print_room(generate_level(16, 7))