"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
from pathlib import Path

class Actor:

    health = 1

    def __init__(self, health = 1):
        """
        description: Constructeur
        """
        self.health = health
