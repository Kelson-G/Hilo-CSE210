#Erik Benson wrote/adapted this code for this file.
import random

# 1) Class declaration
class Deck:
    """A deck of flat playing cards. This will allow the game to be played 
    by guessing whether the next value will be higher or lower than the 
    currently displayed value.
    Attributes:
        value (int): The number on the card.
    """

# 2) The class constructor.
    def __init__(self):
        """Constructs a new instance of Deck with a value and points attribute.
        Args:
            self (Deck): An instance of Deck.
        """
        self.value = 0
        self.player = 300
# 3) Create the draw(self) method. 
    def draw(self):
        """Generates a new random value by 'drawing' a card 
        and compares the points.
        Args:
            self (Deck): An instance of Deck.
        """

        rng = random.randint(1,13)
        self.value = rng
        return self.value
