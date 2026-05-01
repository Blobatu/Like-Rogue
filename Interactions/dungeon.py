
from Level.level_generation import full_level as fl

dungeon_rows: list[str] = fl()
# vieile map utilisée pour les tests.
# dungeon_rows = ["####################",
#                 "##. . . . . . . . ##",
#                 "##. . . . . . . . ##",
#                 "##. . . . @ . . . ##",
#                 "##. . . . . . . . ##",
#                 "####################"]


wall_sprite = "##"
player_sprite = "@ "
air_sprite = ". "
exit_sprite = "|"
barrel_sprite = "⩉ "
chest_sprite = "▤ "
spike_trap_sprite = "△ "

whitelist_sprites = [air_sprite, 
                     chest_sprite, 
                     barrel_sprite, 
                     exit_sprite, 
                     spike_trap_sprite]
