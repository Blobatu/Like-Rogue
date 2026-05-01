"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
import Actors.npc_repository as repo
import Actors.npc as n 
import public

gob = repo.listof_npc["Goblin"]
orc = repo.listof_npc["Orc"]
is_dead = False
while (is_dead is False):

    is_dead = orc.lose_life(public.scale(1))
    
    if(is_dead is True):
        break
