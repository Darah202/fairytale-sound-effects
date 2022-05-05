"""
Contains class to create a text-based menu for the reading session.
"""
class FairytaleMenu:
    """
    Create and track information for a menu for the fairy tale session.

    Attributes:
        _menu: A string representing the input from the user.
        _menu_options: A list of strings representing the different story
            options for the user to choose from.
    """

    def __init__(self):
        """
        Initialize Menu with the input to begin and options of books to choose
        from.
        """
        self._menu = input("Welcome to Fairytale Sound Effects!  Press enter \
            to begin")
        self._menu_options = ["Cinderella", "The 3 Little Pigs"]

    def ask_which_book(self):
        """
        Update 'menu' to ask the user to select a book.

        Returns:
        A tuple including a string representing '_menu' and a string
        representing the name of the book.
        """
        book_number = input("Select a book - type the number of the book and \
            press enter \n 1. Cinderella \n 2. The 3 Little Pigs\n")

        book_title = self._menu_options[int(book_number)-1]

        return str(self._menu), book_title

    def book_choice(self, book_title):
        """
        Print a string telling the user the name of their chosen book.

        Args:
            book_title: A string representing the name of the chosen book
        """
        self._menu = f"Great choice!  You are reading {book_title}.  Begin \
            reading out loud now."
        print(self._menu)

    def __repr__(self):
        """
        Return a string that represents the menu with the appropriate spaces
        filled in.

        Returns:
        A string representing the menu in text format.
        """
        #_menu_representation = f"Choose a book to read:\n {self._menu[1]}\n{self._menu[2]}"
        return str(self._menu)
