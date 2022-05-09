"""
Unit tests for The Three Little Pigs.
"""
import pytest

from three_little_pigs import ThreeLittlePigs

# Define sets of test cases
audio_cue_cases = [
    # Check that the audio cues are added to the dictionary for ThreeLittlePigs
    # for categories (keys) already existing.
    ("boil", "Fire"),
    # Check that the audio cues are added to the dictionary for ThreeLittlePigs
    # for categories (keys) not existing.
    ("you can", "Festive"),
    ("wolf", "Howl"),
    ("kettle", "Water")
]

# Define standard testing functions to check functions' outputs given certain
# inputs defined above. This also includes functions that don't take any inputs.

def test_sound_effect_keys():
    """
    Check that the newly defined categories related to sound effects have been
    added to the list '_sound_effect_keys'.
    """
    pigs = ThreeLittlePigs()
    all_se_keys_present = True
    for key in ["Straw", "Stick", "Brick", "Howl", "Water"]:
        if key not in pigs.get_sound_effect_keys():
            all_se_keys_present = False

    assert all_se_keys_present is True

def test_music_keys():
    """
    Check that the newly defined categories related to backgrund music have been
    added to the list '_music_keys'.
    """
    pigs = ThreeLittlePigs()
    assert "Festive" in pigs.get_music_keys()

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
    pigs = ThreeLittlePigs()
    assert pigs.check_for_key_word(audio_cue) == category_name
