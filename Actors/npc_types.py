"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description : Liste des types de NPCs du jeu.
"""
from . import npc

listof_npc = {
    "Goblin": npc.NPC(name = "Goblin",
                      sprite = "¤ ",
                      health = 1,
                      damage = 1,
                      aura = 1),
    "Orc": npc.NPC(name = "Orc",
                   sprite = "Θ ",
                   health = 2,
                   damage = 2,
                   aura = 1),
    "AuraFarmer": npc.NPC(name = "Aura Farmer",
                          sprite = "Ω ",
                          health = 2,
                          damage = 1,
                          aura = 3)
}