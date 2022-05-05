"""
Book Session controller.
"""
from abc import ABC, abstractmethod


class ControlSoundEffects(ABC):
    """
    Abstract base class representing a controller for a tic-tac-toe game.

    Attributes:
        _board: A TicTacToeBoard instance representing the tic-tac-toe game to
            send moves to.
    """

    def __init__(self, sound_effects):
        """
        Create a new controller for a tic-tac-toe game.

        Args:
            board: A TicTacToeBoard instance representing the tic-tac-toe game
                to send moves to.
        """
        self._sound_effects = sound_effects

    @property
    def sound_effects(self):
        """
        Return the TicTacToeBoard instance this controller interacts with.
        """
        return self._sound_effects

    @abstractmethod
    def play(self):
        """
        Make a valid move in the current board.
        """


class Controller(ControlSoundEffects):
    """
    Text-based controller for tic-tac-toe that takes user input representing
    board coordinates.
    """

    def play(self):
        """
        Obtain text input from the user to make a move in the current board,
        repeating the process until a valid move is made.
        """
        self._sound_effects
