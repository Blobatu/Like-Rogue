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
                 potion_count: int,
                 bomb_count: int,
                 name: str, 
                 sprite: str,
                 position: tuple[int, int], 
                 level: int = 1,
                 health: int = 10, 
                 damage: int = 1):
        """
        description: Constructeur
        """
        super().__init__(name, sprite, position, health, damage)
        self.level = level
        self.potion_count = potion_count
        self.bomb_count = bomb_count
        self.listof_npc_killed: dict[int, npc.NPC] = {}
        self.progression = s.Progression(self.name)
        self.npc_killed_count = 0

    def drink_health_potion(self, value: int):
        """
        But:    Redonne de la vie au joueur
        Sortie: si le joueur a but la potion
        """
        if self.potion_count > 0:
            if self.health < self.max_health:
                self.health += public.scale(value)
                if self.health > self.max_health:
                    self.health = self.max_health
                self.potion_count -= 1
                return True
        return False


player_instance: Player = Player(potion_count=0,
                                 bomb_count=0,
                                 name="Nard", 
                                 sprite="@ ",
                                 position=(6, 24))
