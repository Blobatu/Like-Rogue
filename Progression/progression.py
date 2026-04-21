import Actors.player as p
MAX_LEVEL = 10


class Progression():
    def __init__(self):
        self.player_actor = p.get_player()
        self.ra = None 
        self.progression = 0
        print(f"{self.player_actor.name} has been created at level {self.player_actor.level}.")

    def update_progression(self):
        self.progression = (self.player_actor.level / MAX_LEVEL) * 100
        print(f"{self.player_actor.name}'s progression is now {self.progression:.2f}%.")

    def choose_ra(self, response):
        if response:
            self.player_actor.level += 1
            self.update_progression()
            print(f"{self.player_actor.name} has leveled up to level {self.player_actor.level}!")
        else:
            print(f"{self.player_actor.name} did not level up.")  

progression = Progression()
progression.choose_ra(True)   # Alice levels up
progression.choose_ra(False)  # Alice does not level up
progression.choose_ra(True)   # Alice levels up again
progression.choose_ra(True)   # Alice levels up again