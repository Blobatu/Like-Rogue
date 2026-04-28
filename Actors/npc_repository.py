from . import npc
import public

listof_npc = {
    "Goblin": npc.NPC(name = "Goblin",
                      sprite = "oB",
                      health = public.scale(1),
                      damage = public.scale(1), 
                      size = 1,
                      zone = 1),
    "Orc": npc.NPC(name = "Orc",
                   sprite = "oC",
                   health = public.scale(2),
                   damage = public.scale(2),
                   size = 1,
                   zone = 1),
    "Ogre": npc.NPC(name = "Ogre",
                    sprite = "oG",
                    health = public.scale(5),
                    damage = public.scale(3),
                    size = 2,
                    zone = 1),
    "AuraFarmer": npc.NPC(name = "Aura Farmer",
                          sprite = "oA",
                          health = public.scale(2),
                          damage = public.scale(1),
                          size = 1,
                          zone = 2)
}