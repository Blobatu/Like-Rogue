from level_generation import print_room 
import random as rd
import tileset as ts

# generation de niveau aléatoire 

tiles = []              # crée une liste des tuiles pour les choisir aléatoirement
for t in ts:            #
    tiles.append(t)     #


out_left = ['full', 'strgt_vert', 'crnr_rb', 'crnr_rt']       ## make a list of all valid tiles when on the left wall

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

    if check['left'] == 'out' and check['current'] != out_left: ## repeat this style of check for all rules
        return out_left
    
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
            while current_check != 'ok':            ## check this parrt of the code, it may not be 
                maze[y][x] = rd.choice(current_check)
                current_check = valid(x, y, maze)
    return maze


print_room(generate_level(16, 7))