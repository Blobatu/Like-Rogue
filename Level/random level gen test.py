from tileset import tileset as ts
import random as rd

tiles = []
for t in ts:
    tiles.append(t)



# pas mon code, exemple seulement, ne fonctionne pas

TILES = ['grass', 'water', 'lava', 'stone']

def generate_level(width, height):
    level = []
    for y in range(height):
        row = []
        for x in range(width):
            tile = rd.choice(TILES)
            row.append(tile)
        level.append(row)
    return level

def print_level(level):
    for row in level:
        print(' '.join(row))

# Generate a level of size 5x5
level = generate_level(5, 5)
print_level(level)

def is_valid_tile(level, x, y, tile):
    # Check adjacent tiles
    adjacent_tiles = [
        level[y-1][x] if y > 0 else None,  # Above
        level[y+1][x] if y < len(level) - 1 else None,  # Below
        level[y][x-1] if x > 0 else None,  # Left
        level[y][x+1] if x < len(level[0]) - 1 else None  # Right
    ]

    if tile == 'water' and 'lava' in adjacent_tiles:
        return False
    return True

def generate_level_with_rules(width, height):
    level = []
    for y in range(height):
        row = []
        for x in range(width):
            tile = rd.choice(TILES)
            while not is_valid_tile(level, x, y, tile):
                tile = rd.choice(TILES)
            row.append(tile)
        level.append(row)
    return level

# Generate a level of size 5x5 with rules
level_with_rules = generate_level_with_rules(5, 5)
print_level(level_with_rules)