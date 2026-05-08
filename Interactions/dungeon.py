
"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description : Module pour la gestion du donjon du jeu,
qui contient la carte du donjon et les sprites 
utilisés pour les différentes entités.
"""
from Level.level_generation import full_level as fl, generate_maze, make_level
from Level import level_generation

def generate_them_all():
    """
    But: Génère tous les niveaux dès le début

    Sortie: la liste de tous les niveaux
    """
    testlist = []
    level_generation.current_level = "level_1"
    testlist.append(fl())
    level_generation.current_level = "level_2"
    testlist.append(fl(make_level(generate_maze(level_generation.size[0], 
                                                level_generation.size[1]))))
    level_generation.current_level = "level_3"
    testlist.append(fl(make_level(generate_maze(level_generation.size[0], 
                                                level_generation.size[1]))))
    level_generation.current_level = "level_4"
    testlist.append(fl(make_level(generate_maze(level_generation.size[0], 
                                                level_generation.size[1]))))
    return testlist

levels: list[list[str]] = generate_them_all()

wall_sprite = "##"
player_sprite = "@ "
air_sprite = ". "
damage_sprite = ": "
exit_opened_sprite = "| "
exit_closed_sprite = "X "
barrel_sprite = "⩉ "
chest_sprite = "▤ "
spike_trap_sprite = "△ "
monster_spawn = "& "

whitelist_sprites = [air_sprite, 
                     damage_sprite,
                     chest_sprite, 
                     barrel_sprite, 
                     exit_opened_sprite, 
                     spike_trap_sprite,
                     ""]



