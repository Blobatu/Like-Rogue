"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
import Actors.actor as a
class NPC(a.Actor):

    def __init__(self, level, name, health = 1, damage = 1, damage_done = 0):
        """
        description: Constructeur
        """
        super().__init__(name, health, damage)
        self.level = level
        self.damage_done = damage_done
        self.damage_received = damage_done
