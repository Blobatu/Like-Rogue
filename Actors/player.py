"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
import Actors.actor as a
class NPC(a.Actor):

    def __init__(self, 
                 level: int,
                 damage_done: int,
                 damage_received: int,
                 name: str, 
                 position: tuple[int, int], 
                 health: int = 1, 
                 damage: int = 1):
        """
        description: Constructeur
        """
        super().__init__(name, position, health, damage)
        self.level = level
        self.damage_done = damage_done
        self.damage_received = damage_received
