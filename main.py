"""
Main program to set up and run the fairytale sound effect player.
"""

from menu_states import FairytaleMenu
from view import TextView
#from controller import TextController


def main():
    """
    This function creates a tic-tac-toe board, text view, and two text
    controller instances.  With these instances, a tic-tac-toe game is run
    using user inputs and the winner (or draw) of the game is printed in the
    terminal.
    """

    menu = FairytaleMenu()
    view_board = TextView(menu)
    #controller = TextController(menu)

    view_board.draw()

if __name__ == "__main__":
    main()
