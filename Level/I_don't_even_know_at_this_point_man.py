import random

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
    
     ## if we wand entrances and exits:
    #maze[1][0] = PATH
    #maze[maze_height-2][maze_width-1] = PATH
    
    return maze

def print_maze(maze):
    for row in maze:
        print(''.join(row))

def check_around(maze, pos):
    height = len(maze)
    width = len(maze[0])
    x, y = pos 
    
    neighbors = {'tl': None, 'tr': None, 'bl': None, 'br': None}
    
    if height == 0 or width == 0:
        return neighbors
    
    if 0 <= y < height and 0 <= x < width:
        neighbors['tl'] = maze[y][x]
    if 0 <= y < height and 0 <= x + 1 < width:
        neighbors['tr'] = maze[y][x + 1]
    if 0 <= y + 1 < height and 0 <= x < width:
        neighbors['bl'] = maze[y + 1][x]
    if 0 <= y + 1 < height and 0 <= x + 1 < width:
        neighbors['br'] = maze[y + 1][x + 1]

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
    
    for pos in center_positions:
        t = check_around(maze, pos)
        print(f"Pos {pos}: {t}")




if __name__ == "__main__":
    make_level()
