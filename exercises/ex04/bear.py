"""File to define Bear class."""


class Bear:

    def __init__(self):
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        self.hunger_score += num_fish
