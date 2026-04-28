from .cor_tile import tileset as ts
from .cor_tile import tile_rules as tr
import random as rd

# imp funct:

def make_lvl_data(maze):
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
    for i in make_lvl_data(maze):
        print(i)


# code:

lvl_hgt = 7
lvl_len = 16

def make_canevas(hgt, len):
    canevas = []
    for y in range(hgt):
        row = []
        for x in range(len):
            row.append('empty')      #change back to none
        canevas.append(row)
    return canevas

def mk_lvl(hgt=lvl_hgt, len_=lvl_len):
    maze = make_canevas(hgt, len_)
    
    for posy in range(hgt):
        for posx in range(len_):
            c = {
                'left': maze[posy][posx-1] if posx > 0 else None,
                'right': maze[posy][posx+1] if posx < len_ - 1 else None,
                'up': maze[posy-1][posx] if posy > 0 else None,
                'down': maze[posy+1][posx] if posy < hgt - 1 else None,
                'up_left': maze[posy-1][posx-1] if posx > 0 and posy > 0 else None,
                'up_right': maze[posy-1][posx+1] if posx < len_ - 1 and posy > 0 else None,
                'down_left': maze[posy+1][posx-1] if posx > 0 and posy < hgt - 1 else None,
                'down_right': maze[posy+1][posx+1] if posx < len_ - 1 and posy < hgt - 1 else None,
                'current': maze[posy][posx],
            }
            valid = []
            for i in tr:
                if c['left'] is None: 
                    if 'left' in tr[i]['wall']:
                        valid.append(i)
                #elif c['right'] is None: 
                    if 'right' in tr[i]['wall']:
                        valid.append(i)
                elif c['up'] is None: 
                    if 'up' in tr[i]['wall']:
                        valid.append(i)
                #elif c['down'] is None: 
                    if 'down' in tr[i]['wall']:
                        valid.append(i)
                else:    
                    if ('right' in tr[c['left']]['gen'] and 'left' in tr[i]['gen']) or ('right' in tr[c['left']]['wall'] and 'left' in tr[i]['wall']) or ('right' in tr[c['left']]['big'] and 'left' in tr[i]['big']):
                        valid.append(i)
                    #elif ('left' in tr[c['right']]['gen'] and 'right' in tr[i]['gen']) or ('left' in tr[c['right']]['wall'] and 'right' in tr[i]['wall']) or ('left' in tr[c['right']]['big'] and 'right' in tr[i]['big']):
                        valid.append(i)
                    elif ('up' in tr[c['down']]['gen'] and 'down' in tr[i]['gen']) or ('up' in tr[c['down']]['wall'] and 'down' in tr[i]['wall']) or ('up' in tr[c['down']]['big'] and 'down' in tr[i]['big']):
                        valid.append(i)
                    #elif ('down' in tr[c['up']]['gen'] and 'up' in tr[i]['gen']) or ('down' in tr[c['up']]['wall'] and 'up' in tr[i]['wall']) or ('down' in tr[c['up']]['big'] and 'up' in tr[i]['big']):
                        valid.append(i)
        maze[posy][posx] = rd.choice(valid)
    return maze 


def gen_maze(hgt=lvl_hgt, len=lvl_len):
    None



#for i in tr:
#    print(i, tr[i])
print_room(gen_maze())
