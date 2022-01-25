# Directory
from game.deck import Deck
"""
The code seems to be mostly working, but the do_updates function needs
to be finished for the code to be complete and working.
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
        self.guess = ""
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        #Loop, determins if the game continues running.
        while self.is_playing:  
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to play, also allows for quitting.
        Args:
            self (Director): An instance of Director.
        """
        #Displays the current score.
        print(f"Current Score is: {self.total_score}")
        #Sets the first card value.
        card_one = Deck.draw(self)
        self.card_one = card_one
        print(self.card_one)
        #Starts the actual game by inviting the director to make a guess. 
        #It is also possible to quit out here by pressing q.
        play_game = input("Higher or Lower or Quit? [h/l/q] ")
        self.is_playing = (play_game == "h" or play_game == "l")
        #Sets the play_game input equal to the self.guess to determine 
        #the right answer in the next method.
        self.guess = play_game
        #Terminates the program if the player decided to quit.
        if play_game == "q":
            print(f"Final Score: {self.total_score}")
            print("Thanks for playing!")
            quit()
   
    def do_updates(self):
        """Compares the card values and updates the player's score.
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        #Generates the value for the second card.
        card_two = Deck.draw(self)
        self.card_two = card_two
        card_one = self.card_one
        #compares the card values utilizing the self.guess arguement
        #to determine the outcome.
        if card_two > card_one:
            if self.guess == "h":
                self.total_score += 100
            elif self.guess == "l":
                self.total_score -= 75
        elif card_two < card_one:
            if self.guess == "l":
                self.total_score += 100
            elif self.guess == "h":
                self.total_score -= 75
                
        
    def do_outputs(self):
        """Displays the dice and the score. 
        Also asks the player if they want to roll again. 
        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        #Displays all the outputs, including the compared card and the total score.
        #Also determines if the program ought to terminate due to a too low score.
        print(f"Next card was a {self.card_two}")
        print(f"Your score is: {self.total_score}\n")
        if self.total_score <= 0:
            print("Game Over!\nResetting Score!\n\n")
            self.total_score = 300