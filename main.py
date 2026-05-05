"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description :   Point d'entrée du jeu, qui initialise le donjon, 
                le joueur et les monstres,
"""
import sys
import os
import pygame
from Actors.player import player_instance as p_i
from Interactions import actor_movement as a_m
from Interactions import monster_spawn
from Interactions import monster_AI
from Interactions import dungeon
from Props import props_interaction as pr_i
from Interactions import aura_behavior
import UI.pygame_display as disp

# Setup paths
SCRIPT_DIR = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Initialize game
p_i.set_position(6, 24)
monster_spawn.spawn_monster()

# Initialize display
disp.init_display()
font = pygame.font.SysFont('Consolas', 11)

# Function to render centered text
def draw_centered_text_block(text_lines, screen, font):
    """Draw all lines centered horizontally and vertically."""
    line_height = font.get_height() + 2  # Font height + smaller gap
    rendered_texts = [font.render(str(text), True, (255, 255, 255)) for text in text_lines]
    total_height = len(rendered_texts) * line_height
    start_y = (screen.get_height() - total_height) // 2
    for i, text_surf in enumerate(rendered_texts):
        text_rect = text_surf.get_rect(center=(screen.get_width() // 2, start_y + i * line_height))
        screen.blit(text_surf, text_rect)

running = True
is_pressed = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            is_pressed = True
            # Handle keys
            if event.key in (pygame.K_a, pygame.K_LEFT):
                a_m.move_left()
                monster_AI.react_to_player_movement()
            elif event.key in (pygame.K_d, pygame.K_RIGHT):
                a_m.move_right()
                monster_AI.react_to_player_movement()
            elif event.key in (pygame.K_w, pygame.K_UP):
                a_m.move_up()
                monster_AI.react_to_player_movement()
            elif event.key in (pygame.K_s, pygame.K_DOWN):
                a_m.move_down()
                monster_AI.react_to_player_movement()
            elif event.key == pygame.K_q:
                a_m.move_up()
                a_m.move_left()
                monster_AI.react_to_player_movement()
            elif event.key == pygame.K_e:
                a_m.move_down()
                a_m.move_right()
                monster_AI.react_to_player_movement()
            elif event.key == pygame.K_x:
                aura_behavior.aura_damage(True)
            elif event.key == pygame.K_z:
                p_i.drink_health_potion(5)
            elif event.key == pygame.K_b:
                pr_i.bomb_interaction()
    
    if p_i.is_alive():
        # Bomb logic
        pr_i.is_actor_on_bomb()
        pr_i.bomb_counter()
        pr_i.bomb_explodes()
        
        if is_pressed:
            # Clear screen
            disp.screen.fill((0, 0, 0))
            
            # Prepare text lines
            stats_lines = [
                f"Level: {p_i.level}",
                f"XP: {p_i.progression.xp}/{p_i.progression.xp_to_next}",
                f"Health: {p_i.health}/{p_i.max_health}",
                f"Potions: {p_i.potion_count}",
                f"Bombs: {p_i.bomb_count}",
                ""  # Empty line
            ]
            dungeon_lines = dungeon.levels[p_i.level - 1]
            all_lines = stats_lines + dungeon_lines
            
            # Draw centered
            draw_centered_text_block(all_lines, disp.screen, font)
            is_pressed = False
    else:
        # Show death
        disp.screen.fill((0, 0, 0))
        death_text = f"{p_i.name} is dead"
        text_surface = font.render(death_text, True, (255, 0, 0))
        text_rect = text_surface.get_rect(center=(disp.screen.get_width() // 2, disp.screen.get_height() // 2))
        disp.screen.blit(text_surface, text_rect)
        running = False
    
    disp.flip()
    disp.clock.tick(60)

disp.quit()