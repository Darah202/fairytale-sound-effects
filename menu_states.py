"""
Keeps track of the menu's values

Classes:
    FairytaleMenu: This class is used to keep track of a fairytale menu,
    including information such as the current book chosen

    Functions:
        __init__: Creates an empty tic-tac-toe board
        next_move: Returns a string equal to the next player to move
        mark: Adds a player's symbol to an empty square or raises a value error
        get_square: Returns the symbol in a given board square
        check_win:  Returns which player (X or O or None) wins the game
        __repr__:  Returns a string representation of the board

"""
class FairytaleMenu:
    """
    This class is used to keep track of a tic-tac-toe board, including
    information such as the X and O symbol locations and the winning player

    Attributes:
        board: A list representing the values of the tic-tac-toe board in their
        respective locations.  For example, list location 0 correlates to the
        top left location in the board, location 4 correlates to the center
        position, and location 8 correlates to the bottom right position
    """

    def __init__(self):
        """
        Creates an empty tic-tac-toe board
        """
        self.menu = input("Welcome to Fairytale Sound Effects!  Press enter to begin")
        self._menu_options = ["Cinderella", "The 3 Little Pigs"]

    def ask_which_book(self):
        """
        This function updates the menu string to ask the user to select a book
        """

        book_number = input("Select a book - type the number of the book and press enter \n 1. Cinderella \n 2. The 3 Little Pigs\n")

        book_title = self._menu_options[int(book_number)-1]

        return str(self.menu), book_title

    def book_choice(self, book_title):
        """
        This function returns a string equal to the name of the chosen book

        Returns:
            A string equal to the name of the chosen book
        """

        self.menu = f"Great choice!  You are reading {book_title}.  Begin reading out loud now."

        return str(self.menu)

    def __repr__(self):
        """
        This function returns a string that represents the menu with the
        appropriate spaces filled in

        The string "+-+-+-+" denotes boundaries between rows and "|" denotes
        boundaries between columns

        Returns:
            _board_representation: A string representing the tic-tac-toe board
            with the appropriate spaces filled in
        """
        #_menu_representation = f"Choose a book to read:\n {self._menu[1]}\n{self._menu[2]}"

        return str(self.menu)
