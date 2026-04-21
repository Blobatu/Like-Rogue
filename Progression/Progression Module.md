**Progression Module**

**Description**

Le module **Progression** gère l'évolution d'un acteur (joueur) dans le jeu.  
Il prend en charge les niveaux, les points d'expérience (XP), et la progression globale du joueur.

Ce module fait partie d'un projet collaboratif composé de :

| Module | Responsable | Rôle |
| :---- | :---- | :---- |
| **Progression** *(ce  module)* | Marvyn  | Niveaux, XP, progression |
| Actor | Luc | Création et gestion du joueur |
| UI | James | Affichage et interface |
| Interaction | Leonard | Actions du joueur dans le jeu |
| Level |  | Environnement et carte |

**Fonctionnement**

**Règles de progression**

* Le joueur commence au niveau 1

* Chaque action réussie rapporte 50 XP

* Il faut 100 XP pour passer au niveau 2

* Le seuil d'XP augmente de ×1.5 à chaque niveau

* Le niveau maximum est 10

**Exemple de progression XP**

| Niveau | XP requis |
| :---- | :---- |
| 1 \=2 | 100 XP |
| 2 \= 3 | 150 XP |
| 3 \= 4 | 225 XP |
|  |  |
| 9 \=10 | \~1139 XP |

 **Utilisation**

**Création d'un acteur**

actor \= Progression("Nard")

\# Output: Nard  a été créé au niveau 1\.

**Faire gagner de l'XP (via une action)**

actor.choose\_ra(True)   \# Action réussie \=+50 XP

actor.choose\_ra(False)  \# Action échouée \= pas d'XP

**Récupérer les stats (pour l'UI)**

stats \= actor.get\_stats()

\# Retourne un dictionnaire avec : name, level, xp, xp\_to\_next, progression, max\_level

---

 **Intégration avec les autres modules**

**Depuis Actor**

\# Le module Actor crée un objet Progression pour chaque joueur

class Actor:

    def \_\_init\_\_(self, name):

        self.progression \= Progression(name)

**Depuis Interaction**

\# Le module Interaction appelle choose\_ra() après chaque action du joueur

actor.progression.choose\_ra(response=True)   \# si l'action réussit

actor.progression.choose\_ra(response=False)  \# si l'action échoue

 **Vers UI**

\# Le module UI appelle get\_stats() pour afficher la barre de progression

stats \= actor.progression.get\_stats()

ui.update\_bar(stats\["progression"\], stats\["level"\])

**Prérequis**

* Python 3.14.4

* Aucune bibliothèque externe requise

**Lancer le module seul (test)**

python Progression.py

**Auteur**

* **Progression module** — *Marvyn*

* Projet scolaire — *Programmation /Cegep de sherbrooke*

