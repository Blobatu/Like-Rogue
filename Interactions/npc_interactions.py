import Actors.npc_repository as repo
import Actors.npc as n 
import public

gob = repo.listof_npc["Goblin"]
orc = repo.listof_npc["Orc"]
is_dead = False
while (is_dead is False):

    is_dead = orc.lose_life(public.scale(1))
    print(f"\nHealth:{orc.health}/{orc.max_health}")
    if(is_dead is True):
        break
    print(f"{orc.name} is not dead")

print(f"{orc.name} is dead")
