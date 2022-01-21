import random


# TODO: Implement the Die class as follows...

# 1) Add the class declaration. Use the following class comment.
class Deck:
    """A deck of flat playing cards. This will allow the game to be played 
    by guessing 
    Attributes:
        value (int): The number of spots on the side facing up.
        compare (int): The number of points the die is worth.
    """

# 2) Create the class constructor. Use the following method comment.
    def __init__(self):
        """Constructs a new instance of Die with a value and points attribute.
        Args:
            self (Die): An instance of Die.
        """
        self.points = 0
        self.value = 0
# 3) Create the roll(self) method. Use the following method comment.
    def draw(self):
        """Generates a new random value and compares the points.
        Args:
            self (Deck): An instance of Deck.
        """

        rng = random.randint(1,6)
        self.value = rng
        if rng == 1:
            rng = 100
        elif rng == 5:
            rng = 50
        self.points = rng 