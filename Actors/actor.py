"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
from pathlib import Path

class Actor:

    def __init__(self, name, health = 1):
        """
        description: Constructeur
        """
        self.health = health
        self.name = name
