"""
Main program to set up and run the fairytale sound effect player.
"""

from menu_states import FairytaleMenu
from view import TextView
#from controller import Controller


def main():
    """
    This function creates a tic-tac-toe board, text view, and two text
    controller instances.  With these instances, a tic-tac-toe game is run
    using user inputs and the winner (or draw) of the game is printed in the
    terminal.
    """

    menu = FairytaleMenu()
    view_menu = TextView(menu)
    #controller = Controller()

    view_menu.draw()

    menu.ask_which_book()

    menu



if __name__ == "__main__":
    main()
