
"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description : Module pour la gestion du donjon du jeu,
qui contient la carte du donjon et les sprites 
utilisés pour les différentes entités.
"""
from Level.level_generation import full_level as fl

dungeon_rows: list[str] = fl()


wall_sprite = "##"
player_sprite = "@ "
air_sprite = ". "
damage_sprite = ": "
exit_openned_sprite = "| "
exit_closed_sprite = "X "
barrel_sprite = "⩉ "
chest_sprite = "▤ "
spike_trap_sprite = "△ "

whitelist_sprites = [air_sprite, 
                     damage_sprite,
                     chest_sprite, 
                     barrel_sprite, 
                     exit_openned_sprite, 
                     spike_trap_sprite]
