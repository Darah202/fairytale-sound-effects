"""
Unit tests for audio_controller
"""
import pytest
from audio_controller import AudioController

# Define sets of test cases
find_and_play_key_word_cases = [
    # Check that each key name returns the correct list representing the
    # location of corresponding audio files for 'Music' related keys
    ("Beginning"),
    ("Sad"),
    # Check that each key name returns the correct list representing the
    # location of correspon ding audio files for 'Sound_Effects' related keys
    ("Huff"),
    ("Fire"),
    ("Footsteps"),
    ("Laughter"),
    ("Horse"),
    ("Clock"),
    ("Knock")
]

@pytest.mark.parametrize("key", find_and_play_key_word_cases)
def find_and_play_key_word(key):
    """
    Check that for the given location, a random file from the folder of audio
    files corresponding to it's location is played through pygame.

    Args:
        key: A string representing the category name related to which the
            audio file will be randomly played.
    """
    controller = AudioController("BookSession")
    assert controller.find_and_play_key_word(key) is True
