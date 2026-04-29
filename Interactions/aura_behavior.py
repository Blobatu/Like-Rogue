from .random_npc import r_npc
from Actors import player as p

def detected():
    if(r_npc.position[0] + 1 == p.player_instance.position[0] 
       and (r_npc.position[1] == p.player_instance.position[1] or
            r_npc.position[1] + 1 == p.player_instance.position[1] or
            r_npc.position[1] - 1 == p.player_instance.position[1]) or                         
       r_npc.position[0] - 1 == p.player_instance.position[0]
       and (r_npc.position[1] == p.player_instance.position[1] or
            r_npc.position[1] + 1 == p.player_instance.position[1] or
            r_npc.position[1] - 1 == p.player_instance.position[1]) or
       r_npc.position[0] == p.player_instance.position[0] 
       and (r_npc.position[1] + 1 == p.player_instance.position[1] or
            r_npc.position[1] - 1 == p.player_instance.position[1])
    ):
        print("Combat !")
        print("player position : " + str(p.player_instance.position))
        print("monster position : " + str(r_npc.position))