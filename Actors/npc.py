"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
import Actors.actor as a
class NPC(a.Actor):
    
    def __init__(self, name, health = 1, zone = 1, damage = 1):
        """
        description: Constructeur
        """
        super().__init__(name, health, damage)
        self.zone = zone
        
