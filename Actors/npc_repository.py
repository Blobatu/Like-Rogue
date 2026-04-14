import Actors.npc as npc
import public

listof_npc = {
    "Goblin": npc.NPC(name = "Goblin", 
                      health = public.scale(1),
                      damage = public.scale(1), 
                      size = public.scale(1),
                      zone = public.scale(1)),
    "Orc": npc.NPC(name = "Orc",
                    health = public.scale(2),
                    damage = public.scale(2),
                    size = public.scale(1),
                    zone = public.scale(1)),
    "Ogre": npc.NPC(name = "Ogre",
                    health = public.scale(5),
                    damage = public.scale(3),
                    size = public.scale(2),
                    zone = public.scale(1)),
    "AuraFarmer": npc.NPC(name = "Aura Farmer",
                          health = public.scale(2),
                          damage = public.scale(1),
                          size = public.scale(1),
                          zone = public.scale(2))
}