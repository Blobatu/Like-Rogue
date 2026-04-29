import random
from cor_tile import tileset as ts
from cor_tile import tile_rules as tr
WALL = '#'
PATH = ' '

def generate_maze(width, height):
    maze_width = width * 3
    maze_height = height * 3
    maze = [[WALL for _ in range(maze_width)] for _ in range(maze_height)]

    def carve_passages(cx, cy):
        maze_center_y = cy * 3 + 1
        maze_center_x = cx * 3 + 1
        maze[maze_center_y][maze_center_x] = PATH
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)

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

def make_level(maze=generate_maze(16, 7)):
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

def print_level(maze=make_level()):
    for i in make_lvl_data(maze):
        print(i)

if __name__ == "__main__":
    print_level()