"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
import Actors.actor as a
class NPC(a.Actor):
    
    def __init__(self,
                 zone: int, 
                 name: str,
                 symbol: str,
                 position: tuple[int, int], 
                 health: int, 
                 damage: int,
                 size: int):
        """
        description: Constructeur
        """
        super().__init__(name, symbol, position, health, damage, size)
        self.zone = zone
        
