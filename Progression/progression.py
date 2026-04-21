import Actors.player as p
MAX_LEVEL = 10


class Progression():
    def __init__(self):
        self.ra = None 
        self.progression = 0
        print(f"{p.player_instance.name} has been created at level {p.player_instance.level}.")

    def update_progression(self):
        self.progression = (p.player_instance.level / MAX_LEVEL) * 100
        print(f"{p.player_instance.name}'s progression is now {self.progression:.2f}%.")

    def choose_ra(self, response):
        if response:
            p.player_instance.level += 1
            self.update_progression()
            print(f"{p.player_instance.name} has leveled up to level {p.player_instance.level}!")
        else:
            print(f"{p.player_instance.name} did not level up.")  

progression = Progression()
progression.choose_ra(True)   # Alice levels up
progression.choose_ra(False)  # Alice does not level up
progression.choose_ra(True)   # Alice levels up again
progression.choose_ra(True)   # Alice levels up again