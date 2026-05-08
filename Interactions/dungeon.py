
"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description : Module pour la gestion du donjon du jeu,
qui contient la carte du donjon et les sprites 
utilisés pour les différentes entités.
"""
from Level.level_generation import full_level as fl, generate_maze, make_level
from Level import level_generation as l_g
from Actors.player import player_instance as p_i

def generate_them_all():
    """
    But: Génère tous les niveaux dès le début

    Sortie: la liste de tous les niveaux
    """
    testlist = []
    for i in range(1, 5):
        l_g.current_level = "level_"+str(i)
        l_g.size = l_g.lv[l_g.current_level]['size']
        diff = l_g.lv[l_g.current_level]['difficulty']
        testlist.append(fl(make_level(generate_maze(l_g.size[0], 
                                                    l_g.size[1])),
                           enn_spwn = int(diff * 2.5), 
                           loot = int(diff + 1), 
                           traps = int(diff * 6)))
    return testlist

def get_middle_row():
    return len(levels[p_i.level-1])//2

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



