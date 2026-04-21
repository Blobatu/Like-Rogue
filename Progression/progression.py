max_level = 10

class actor():
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.ra = None 
        self.progression = 0
        print(f"{self.name} has been created at level {self.level}.")

    def update_progression(self):
        self.progression = (self.level / max_level) * 100
        print(f"{self.name}'s progression is now {self.progression:.2f}%.")

    def choose_ra(self, response):
        if response:
            self.level += 1
            self.update_progression()
            print(f"{self.name} has leveled up to level {self.level}!")
        else:
            print(f"{self.name} did not level up.")  

actor1 = actor("Alice")
actor1.choose_ra(True)   # Alice levels up
actor1.choose_ra(False)  # Alice does not level up
actor1.choose_ra(True)   # Alice levels up again
actor1.choose_ra(True)   # Alice levels up again