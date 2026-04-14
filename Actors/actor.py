"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
class Actor:

    def __init__(self, 
                 name: str, 
                 position: tuple[int, int], 
                 health: int = 1, 
                 damage: int = 1):
        """
        description: Constructeur
        """
        self.name = name
        self.position = position
        self.health = health
        self.damage = damage
