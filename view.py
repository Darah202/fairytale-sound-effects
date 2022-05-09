"""
View and interact with a text based menu
"""
from abc import ABC, abstractmethod

class MenuView(ABC):
    """
    Abstract base class representing a view menu for the fairytale sound effect
    player.

    Attributes:
        _menu: A FairytaleMenu instance representing the menu to display.
    """
    def __init__(self, menu):
        """
        Initialize MenuView with an instance of a FairyTaleMenu object that
        was inputted.

        Args:
            menu: A FairyTaleMenu to be viewed.
        """
        self._menu = menu

    @property
    def menu(self):
        """
        Return the FairytaleMenu instance being represented by this view.
        """
        return self._menu

    @abstractmethod
    def draw(self):
        """
        Display a representation of the current state of the menu.
        """


class TextView(MenuView):
    """
    Text-based view of the fairytale sound effects menu.
    """
    def draw(self):
        """
        Display a representation of the current state of the menu.
        """
        print(self._menu)
