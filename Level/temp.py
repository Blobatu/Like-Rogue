from .cor_tile import tileset as ts
from .cor_tile import tile_rules as tr
import random as rd

lvl_hgt = 7
lvl_len = 16


def make_canevas(hgt, len_):
    return [['empty' for _ in range(len_)] for _ in range(hgt)]


def get_neighbors(maze, posy, posx):
    hgt = len(maze)
    len_ = len(maze[0])
    return {
        'left': maze[posy][posx-1] if posx > 0 else None,
        'right': maze[posy][posx+1] if posx < len_ - 1 else None,
        'up': maze[posy-1][posx] if posy > 0 else None,
        'down': maze[posy+1][posx] if posy < hgt - 1 else None,
        'current': maze[posy][posx],
    }


def can_tile_connect_side(neigh_tile, side, tile_name):
    if neigh_tile is None:
        return True

    if neigh_tile not in tr or tile_name not in tr:
        return False

    neigh_data = tr[neigh_tile]
    my_data = tr[tile_name]

    if side == 'left':
        return (('right' in neigh_data.get('gen', [])) and ('left' in my_data.get('gen', []))) or \
               (('right' in neigh_data.get('wall', [])) and ('left' in my_data.get('wall', []))) or \
               (('right' in neigh_data.get('big', [])) and ('left' in my_data.get('big', [])))

    if side == 'right':
        return (('left' in neigh_data.get('gen', [])) and ('right' in my_data.get('gen', []))) or \
               (('left' in neigh_data.get('wall', [])) and ('right' in my_data.get('wall', []))) or \
               (('left' in neigh_data.get('big', [])) and ('right' in my_data.get('big', [])))

    if side == 'up':
        return (('down' in neigh_data.get('gen', [])) and ('up' in my_data.get('gen', []))) or \
               (('down' in neigh_data.get('wall', [])) and ('up' in my_data.get('wall', []))) or \
               (('down' in neigh_data.get('big', [])) and ('up' in my_data.get('big', [])))

    if side == 'down':
        return (('up' in neigh_data.get('gen', [])) and ('down' in my_data.get('gen', []))) or \
               (('up' in neigh_data.get('wall', [])) and ('down' in my_data.get('wall', []))) or \
               (('up' in neigh_data.get('big', [])) and ('down' in my_data.get('big', [])))

    return False


def gather_valid_tiles(maze, posy, posx, tr):
    c = get_neighbors(maze, posy, posx)
    valid = []

    for tile_name in tr:
        if tile_name in ('hollow', 'full'):
            continue

        if (c['left'] is not None and not can_tile_connect_side(c['left'], 'left', tile_name)) or \
           (c['right'] is not None and not can_tile_connect_side(c['right'], 'right', tile_name)) or \
           (c['up'] is not None and not can_tile_connect_side(c['up'], 'up', tile_name)) or \
           (c['down'] is not None and not can_tile_connect_side(c['down'], 'down', tile_name)):
            continue

        valid.append(tile_name)

    return valid


def mk_lvl(hgt=lvl_hgt, len_=lvl_len):
    maze = make_canevas(hgt, len_)

    for posy in range(hgt):
        for posx in range(len_):
            valid = gather_valid_tiles(maze, posy, posx, tr)
            if valid:
                maze[posy][posx] = rd.choice(valid)
            else:
                maze[posy][posx] = 'empty'  # fallback

    return maze


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


def print_room(maze):
    for row in make_lvl_data(maze):
        print(row)


print_room(mk_lvl())