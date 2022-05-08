"""
Main program to set up and run the fairytale sound effect player.
"""
from menu_states import FairytaleMenu
from audio_controller import AudioController
from view import TextView

def main():
    """
    Run the entire sound effect player by integrating the Menu and
    AudioController together.
    """
    # Create text-version of menu
    menu = FairytaleMenu()
    view_menu = TextView(menu)
    view_menu.draw()

    # Ask user for book
    which_book = menu.ask_which_book()
    book_chosen = menu.book_choice(which_book[0], which_book[1])

    # Listen for audio cues for the book chosen
    sound_effects = AudioController(book_chosen)
    sound_effects.combine_listening()

if __name__ == "__main__":
    main()
