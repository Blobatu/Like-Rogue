# Progression Module — Like-Rogue Game

##  Description

Le module **Progression** gère l'évolution d'un acteur (joueur) dans le jeu Like-Rogue.  
Il prend en charge les niveaux, les points d'expérience (XP), et la progression globale du joueur.

Ce module fait partie d'un projet collaboratif composé de :

| Module | Responsable | Rôle |
|--------|------------|------|
| **Progression** *(ce module)* | Toi | Niveaux, XP, progression |
| Actor | Collègue 1 | Création et gestion du joueur |
| UI | Collègue 2 | Affichage et interface |
| Interaction | Collègue 3 | Actions du joueur dans le jeu |
| Level | Collègue 4 | Environnement et carte |


##  Fonctionnement

### Règles de progression

- Le joueur commence au **niveau 1**
- Chaque action réussie rapporte **50 XP**
- Il faut **100 XP** pour passer au niveau 2
- Le seuil d'XP augmente de **×1.5** à chaque niveau
- Le niveau maximum est **10**

### Exemple de progression XP

| Niveau | XP requis |
|--------|-----------|
| 1 → 2  | 100 XP    |
| 2 → 3  | 150 XP    |
| 3 → 4  | 225 XP    |
| ...    | ...       |
| 9 → 10 | ~1139 XP  |


## Utilisation

### Création d'un acteur

```python
actor = Progression("Nard")
# Output: Nard a été créé au niveau 1.
```

### Faire gagner de l'XP (via une action)

```python
actor.choose_ra(True)   # Action réussie → +50 XP
actor.choose_ra(False)  # Action échouée → pas d'XP
```

### Récupérer les stats (pour l'UI)

```python
stats = actor.get_stats()
# Retourne un dictionnaire avec : name, level, xp, xp_to_next, progression, max_level
```

---

##  Intégration avec les autres modules

###  Depuis Actor
```python
# Le module Actor crée un objet Progression pour chaque joueur
class Actor:
    def __init__(self, name):
        self.progression = Progression(name)
```

### Depuis Interaction
```python
# Le module Interaction appelle choose_ra() après chaque action du joueur
actor.progression.choose_ra(response=True)   # si l'action réussit
actor.progression.choose_ra(response=False)  # si l'action échoue
```

###  Vers UI
```python
# Le module UI appelle get_stats() pour afficher la barre de progression
stats = actor.progression.get_stats()
ui.update_bar(stats["progression"], stats["level"])
```


##  Prérequis

- Python 3.8+
- Aucune bibliothèque externe requise


## Lancer le module seul (test)

```bash
python Progression.py
```


##  Auteur

- **Progression module** — *Marvyn Mbeugmo*
- Projet scolaire — *Programmation/ Cegep de sherbrooke*
