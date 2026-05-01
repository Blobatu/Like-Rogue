"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
from . import npc
import public

listof_npc = {
    "Goblin": npc.NPC(name = "Goblin",
                      sprite = "B ",
                      health = 1,
                      damage = 1, 
                      size = 1,
                      zone = 1),
    "Orc": npc.NPC(name = "Orc",
                   sprite = "C ",
                   health = 2,
                   damage = 2,
                   size = 1,
                   zone = 1),
    "Ogre": npc.NPC(name = "Ogre",
                    sprite = "G ",
                    health = 5,
                    damage = 3,
                    size = 2,
                    zone = 1),
    "AuraFarmer": npc.NPC(name = "Aura Farmer",
                          sprite = "A ",
                          health = 2,
                          damage = 1,
                          size = 1,
                          zone = 2)
}