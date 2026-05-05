"""
Auteur : Luc Desforges
Date : 1 mai 2026
Description : Classe pour le joueur du jeu, héritant de la classe Actor.
"""
from Progression import Simulation as s
import public

from . import npc

from . import actor as a

class Player(a.Actor):
    def __init__(self, 
                 weapon: Weapon,
                 potion_count: int,
                 bomb_count: int,
                 level: int,
                 damage_done: int,
                 damage_received: int,
                 name: str, 
                 sprite: str,
                 position: tuple[int, int], 
                 health: int = 20, 
                 damage: int = 1,
                 size: int = 1):
        """
        description: Constructeur
        """
        super().__init__(name, sprite, position, health, damage, size)
        self.level = level
        self.damage_done = damage_done
        self.damage_received = damage_received
        self.weapon = weapon
        self.potion_count = potion_count
        self.bomb_count = bomb_count
        self.listof_npc_killed: dict[int, npc.NPC] = {}
        self.progression = s.Progression(self.name)
        self.npc_killed_count = 0

    def drink_health_potion(self, value: int):
        self.health += public.scale(value)


player_instance: Player = Player(weapon=None,
                                 potion_count=3,
                                 bomb_count=5,
                                 level=1, 
                                 damage_received=0, 
                                 damage_done=0,
                                 name="Nard", 
                                 sprite="@ ",
                                 position=(0, 0))


class Weapon:
    def __init__(self, name: str,):
        self.name = name
