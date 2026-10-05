from random import randint

class Dice:
    """A calss repersenting a single dice"""

    def __init__(self, num_side=6):
        """Assume a six sided dice."""
        self.num_sides = num_side

    def roll(self):
        """Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)