# Directory
from game.deck import Deck

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card_one (int): The value of the first card.
        card_two (int): The value of the second card.
        is_playing (boolean): Whether or not the game is being played.
        compare (boolean): True = higher, False = lower.
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
        self.compare = False
        self.total_score = 0

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to roll.

        Args:
            self (Director): An instance of Director.
        """
        play_game = input("Play again? [y/n] ")
        self.is_playing = (play_game == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.dice)):
            die = self.dice[i]
            die.roll()
            self.score += die.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the dice and the score. Also asks the player if they want to roll again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        
        values = ""
        for i in range(len(self.dice)):
            die = self.dice[i]
            values += f"{die.value} "

        print("Next card was a %d" % ())
        print(f"You rolled: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)