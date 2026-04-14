"""
Auteur : Luc Desforges
Date : 14 avril 2026
Description : TODO
"""
import Actors.actor as a
class NPC(a.Actor):

    health = 1

    def __init__(self, health = 1):
        """
        description: Constructeur
        """
        self.health = health
