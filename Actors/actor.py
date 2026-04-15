"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
class Actor:

    def __init__(self, 
                 name: str,
                 symbol: str, 
                 position: tuple[int, int], 
                 health: int, 
                 damage: int,
                 size: int):
        """
        description: Constructeur
        """
        self.name = name
        self.symbol = symbol
        self.position = position
        self.health = health
        self.damage = damage
        self.size = size
