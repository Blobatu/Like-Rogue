from level_generation import make_lvl_data
import random as rd
from tileset import tileset as ts


# because importing it wouldn't work, somehow
def print_room(maze):
    for i in make_lvl_data(maze):
        print(i)


# generation de niveau aléatoire 

tiles = []              # crée une liste des tuiles pour les choisir aléatoirement
for t in ts:            #
    tiles.append(t)     #


out_left = ['void', 'full', 'hollow', 'strgt_vert', 'end_r', 'end_b', 'end_t', 'crnr_rb', 'crnr_rt', '3way_rtb', 'wall_l', 'crnr_wall_rb', 'crnr_wall_rt', 'crnr_door_t_rb', 'crnr_door_b_rt'] 
out_right = ['void', 'full', 'hollow', 'strgt_vert', 'end_l', 'end_b', 'end_t', 'crnr_lb', 'crnr_lt', '3way_ltb', 'wall_r', 'crnr_wall_lb', 'crnr_wall_lt', 'crnr_door_t_lb','crnr_door_b_lt']
out_top = ['void', 'full', 'hollow', 'strgt_horz', 'end_r', 'end_b', 'end_l', 'crnr_rb', 'crnr_lb', '3way_lrb', 'wall_t', 'crnr_wall_rb', 'crnr_wall_lb', 'crnr_door_r_lb', 'crnr_door_l_rb'] 
out_bottom = ['void', 'full', 'hollow', 'strgt_horz', 'end_l', 'end_r', 'end_t', 'crnr_lt', 'crnr_rt', '3way_lrt', 'wall_b', 'crnr_wall_rt', 'crnr_wall_lt', 'crnr_door_r_lt','crnr_door_l_rt']

open_top = ['cross', 'strgt_vert', 'end_t', 'crnr_lt', 'crnr_rt', '3way_lrt', '3way_ltb', '3way_rtb', 'door_t', 'cross-lb', 'cross-rb', 'crnr_door_t_lb', 'crnr_door_t_rb']
open_bottom = ['cross', 'strgt_vert', 'end_b', 'crnr_lb', 'crnr_rb', '3way_lrb', '3way_ltb', '3way_rtb', 'door_b', 'cross-lt', 'cross-rt', 'crnr_door_b_lt', 'crnr_door_b_rt']
open_left = ['cross', 'strgt_horz', 'end_l', 'crnr_lt', 'crnr_lb', '3way_lrt', '3way_ltb', '3way_lrb', 'door_l', 'cross-rb', 'cross-rt', 'crnr_door_l_rb', 'crnr_door_l_rt']
open_right = ['cross', 'strgt_horz', 'end_r', 'crnr_rt', 'crnr_rb', '3way_lrt', '3way_rtb', '3way_lrb', 'door_r', 'cross-lb', 'cross-lt', 'crnr_door_r_lb', 'crnr_door_r_lt']


big_open_top = ['empty', 'wall_b', 'wall_r', 'wall_l', 'door_b', 'door_l', 'door_r', 'cross-lt', 'cross-rt', 'crnr_wall_lt', 'crnr_wall_rt', 'pillar', 'crnr_door_r_lt', 'crnr_door_l_rt', 'crnr_door_b_lt', 'crnr_door_b_rt']
big_open_bottom = ['empty', 'wall_t', 'wall_r', 'wall_l', 'door_t', 'door_l', 'door_r', 'cross-lb', 'cross-rb', 'crnr_wall_lb', 'crnr_wall_rb', 'pillar', 'crnr_door_r_lb', 'crnr_door_l_rb', 'crnr_door_t_lb', 'crnr_door_t_rb']
big_open_left = ['empty', 'wall_t', 'wall_r', 'wall_b', 'door_t', 'door_b', 'door_r', 'cross-rb', 'cross-rt', 'crnr_wall_lb', 'crnr_wall_lt', 'pillar', 'crnr_door_r_lb', 'crnr_door_r_lt', 'crnr_door_t_lb', 'crnr_door_b_lt']
big_open_right = ['empty', 'wall_t', 'wall_l', 'wall_b', 'door_t', 'door_b', 'door_l', 'cross-lb', 'cross-lt', 'crnr_wall_rb', 'crnr_wall_rt', 'pillar', 'crnr_door_l_rb', 'crnr_door_l_rt', 'crnr_door_t_rb', 'crnr_door_b_rt']

    ##for a second pass, check for corners, for diagonnals and replace some percentage of cross with cross pillar


def valid(x, y, maze,):
    width = len(maze[0])
    height = len(maze)

    c = {
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
    
    for i in c:
        if c[i] == 'void':
           c[i] = 'out'

    if c['left'] == 'out' and c['current'] not in out_left:
        return out_left
    
    if c['right'] == 'out' and c['current'] not in out_right:
        return out_right
    
    if c['up'] == 'out' and c['current'] not in out_top:
        return out_top
    
    if c['down'] == 'out' and c['current'] not in out_bottom:
        return out_bottom


    #if c['left'] in big_open_right and c['current'] not in big_open_left:
    #    return big_open_left
    
    #if c['right'] in big_open_left and c['current'] not in big_open_right:
    #    return big_open_right

    #if c['up'] in big_open_bottom and c['current'] not in big_open_top:
    #    return open_top
    
    #if c['down'] in big_open_top and c['current'] not in big_open_bottom:
    #    return big_open_bottom
    

    if c['left'] in open_right and c['current'] not in open_left:
        return open_left
    
    if c['right'] in open_left and c['current'] not in open_right:
        return open_right

    if c['up'] in open_bottom and c['current'] not in open_top:
        return open_top
    
    if c['down'] in open_top and c['current'] not in open_bottom:
        return open_bottom


    else:
        return 'ok'



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
            while current_check != 'ok':
                maze[y][x] = rd.choice(current_check)
                current_check = valid(x, y, maze)
    return maze


print_room(generate_level(16, 7))