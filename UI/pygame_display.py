import pygame
import sys

# Global display variables
width = 1450
height = 850
font_size = 11
screen = None
font = None
clock = None
line_height = 0

def init_display():
    """Initialize Pygame display."""
    global screen, font, clock, line_height
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Pygame Text Game")
    font = pygame.font.SysFont('Consolas', font_size)
    clock = pygame.time.Clock()
    line_height = font.get_height() + 2

def draw_game(p_i, dungeon):
    """Render status and dungeon map."""
    screen.fill((0, 0, 0))
    
    # Status lines
    status_lines = [
        f"    Level: {p_i.level}",
        f"    XP: {p_i.progression.xp}/{p_i.progression.xp_to_next}",
        f"    Health: {p_i.health}/{p_i.max_health}",
        f"    Potions: {p_i.potion_count}",
        f"    Bombs: {p_i.bomb_count}"
    ]
    
    y_offset = 10
    for line in status_lines:
        text_surf = font.render(line, True, (0, 255, 0))
        screen.blit(text_surf, (10, y_offset))
        y_offset += line_height
    
    # Dungeon map
    map_start_y = y_offset + 5
    dungeon_map = '\n'.join(dungeon.levels[p_i.level-1])
    map_lines = dungeon_map.split('\n')
    
    for i, map_line in enumerate(map_lines):
        text_surf = font.render(map_line, True, (255, 255, 255))
        screen.blit(text_surf, (10, map_start_y + i * line_height))

def show_death(p_i):
    """Show death screen."""
    screen.fill((0, 0, 0))
    dead_text = font.render(f"{p_i.name} is dead", True, (255, 0, 0))
    text_rect = dead_text.get_rect(center=(width // 2, height // 2))
    screen.blit(dead_text, text_rect)

def flip():
    """Update display."""
    pygame.display.flip()

def quit():
    """Clean up Pygame."""
    pygame.quit()
    sys.exit()