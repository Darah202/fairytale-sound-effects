"""
Main program to set up and run the fairytale sound effect player.
"""

from menu_states import FairytaleMenu
from audio_controller import AudioController
from view import TextView
from cinderella import Cinderella
from three_little_pigs import ThreeLittlePigs

def main():
    """
    This function creates a tic-tac-toe board, text view, and two text
    controller instances.  With these instances, a tic-tac-toe game is run
    using user inputs and the winner (or draw) of the game is printed in the
    terminal.
    """
    menu = FairytaleMenu()
    view_menu = TextView(menu)

    view_menu.draw()

    which_book = menu.ask_which_book()

    book_chosen = menu.book_choice(which_book[1])
    sound_effects = AudioController(book_chosen)

    sound_effects.combine_listening()

if __name__ == "__main__":
    main()
