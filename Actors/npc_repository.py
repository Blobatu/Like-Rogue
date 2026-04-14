import Actors.npc as npc
import public

listof_npc = {
    "Goblin": npc.NPC(name = "Goblin", 
                      health = public.scale,
                      damage = public.scale, 
                      size = 1,
                      zone = 1),
    "Orc": npc.NPC(name = "Orc",
                    health = 2,
                    damage = 2,
                    size = 1,
                    zone = 1),
    "Ogre": npc.NPC(name = "Ogre",
                    health = 5,
                    damage = 3,
                    size = 2,
                    zone = 1),
    "AuraFarmer": npc.NPC(name = "Aura Farmer",
                          health = 2,
                          damage = 1,
                          size = 1,
                          zone = 2)
}