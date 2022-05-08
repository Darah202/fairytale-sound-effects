"""
Unit tests for Cinderella.
"""
import pytest

from cinderella import Cinderella

# Define sets of test cases
audio_cue_cases = [
    # Check that the audio cues are added to the dictionary for Cinderella for
    # categories already existing
    ("turned", "Beginning"),
    ("poof", "Beginning"),
    ("dirty", "Sad"),
    # Check that the audio cues are added to the dictionary for Cinderella for
    # categories not existing
    ("scream", "Scary"),
    ("blow", "Wind"),
    ("bride", "Festive")
]

# Define standard testing functions to check functions' outputs given certain
# inputs defined above. This also includes functions that don't take any inputs.

def test_sound_effect_keys():
    """
    Check that the newly defined categories related to sound effects have been
    added to the list '_sound_effect_keys'.
    """
    cind = Cinderella()
    assert "Wind" in cind.get_sound_effect_keys()

def test_music_keys():
    """
    Check that the newly defined categories related to background music have
    been added to the list '_music_keys'.
    """
    cind = Cinderella()
    festive = "Festive" in cind.get_music_keys()
    scary = "Scary" in cind.get_music_keys()

    assert festive and scary is True

@pytest.mark.parametrize("audio_cue, category_name", audio_cue_cases)
def test_audio_cues(audio_cue, category_name):
    """
    Check that the newly defined audio cues have been added to the main
    dictionary '_key_words'.

    Args:
        audio_cue: A string representing the audio cue that is expected to
            have been added to the main dictionary.
        category_name: A string representing the key for the value entered in
            the dictionary that is expected to be returned.
    """
    cind = Cinderella()
    assert cind.check_for_key_word(audio_cue) == category_name
