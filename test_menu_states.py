"""
Unit tests for the Menu.
"""
from menu_states import FairytaleMenu

# Define standard testing functions to check functions' outputs given certain
# inputs defined above. This also includes functions that don't take any inputs.

def test_valid_book():
    """
    Check that only a valid book can be requested.
    """
    menu = FairytaleMenu()
    book_info = menu.ask_which_book()
    assert "Cinderella" in book_info[0] or "The 3 Little Pigs" in book_info[0]

def test_opened_text_file():
    """
    Check that only a valid book file can be requested.
    """
    menu = FairytaleMenu()
    book_info = menu.ask_which_book()
    assert "cinderella.txt" in book_info[1] or "three_little_pigs.txt" in book_info[1]
    