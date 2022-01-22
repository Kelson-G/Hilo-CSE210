# Directory
from game.deck import Deck
"""
Edgar, take a look at the two commented functions, make sure they work
and try to have them done by the evening of Friday January 21. Text us
in slack if there are any issues and to let us know when you're finished.
"""
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card_one (int): The value of the first card.
        card_two (int): The value of the second card.
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.card_one = 0
        self.card_two = 0
        self.is_playing = True
        self.total_score = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.draw() 
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

#Edgar, look at this function too.
    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        play_game = input("Higher or lower? [h/l] ")
        self.is_playing = (play_game == "h" or play_game == "l")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
#        if not self.is_playing:
#            return

#        self.card.flip()
#        self.current_card = self.card.value


    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        card = self.card_two

        print("Next card was a %d" % (card))
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.total_score > 0)