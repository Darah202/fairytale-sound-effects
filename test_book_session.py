"""
Unit tests for BookSession.
"""
import os
import pytest
from book_session import BookSession

# Define sets of test cases

audio_cue_cases = [
    # Check that the audio cues are added to the dictionary for BookSession.
    ("once upon a time", "Beginning"),
    ("fire", "Fire"),
    ("sad", "Sad"),
    ("knock", "Knock")
]

check_for_key_word_cases = [
    # Check that text with no audio cue returns None
    ("awful awesome teacher cloud", None),
    # Check that text with one word that is the cue returns the key word for it
    ("ran", "Footsteps"),
    # Check that text with >1 word that is the cue returns the key word for it
    ("ran far away", "Footsteps"),
    # Check that text with >1 word that is the cue (not at the beginning)
    # returns the key word for it
    ("the cloud ran far away", "Footsteps"),
    # Check that text with >1 key word returns the one that is first in the
    # dictionary
    ("ding dong horse", "Horse"),
    ("the sad dog ran home once upon a time", "Beginning"),
    # Check that taking spaces away from cases above doesn't change the results
    ("ranfaraway", "Footsteps"),
    ("thecloudranfaraway", "Footsteps"),
    ("dingdonghorse", "Horse"),
    ("thesaddogranhomeonce upon a time", "Beginning")
]

find_audio_location_cases = [
    # Check that each key name returns the correct list representing the
    # location of corresponding audio files for 'Music' related keys
    ("Beginning", ["Music", "Beginning"]),
    ("Sad", ["Music", "Sad"]),
    # Check that each key name returns the correct list representing the
    # location of corresponding audio files for 'Sound_Effects' related keys
    ("Huff", ["Sound_Effects", "Huff"]),
    ("Fire", ["Sound_Effects", "Fire"]),
    ("Footsteps", ["Sound_Effects", "Footsteps"]),
    ("Laughter", ["Sound_Effects", "Laughter"]),
    ("Horse", ["Sound_Effects", "Horse"]),
    ("Clock", ["Sound_Effects", "Clock"]),
    ("Knock", ["Sound_Effects", "Knock"])
]

pick_random_audio_cases = [
    # Check that all category names return an audio file from their
    # corresponding directory.
    ("Beginning"),
    ("Sad"),
    ("Huff"),
    ("Fire"),
    ("Footsteps"),
    ("Laughter"),
    ("Horse"),
    ("Clock"),
    ("Knock")
]

add_key_word_cases = [
    # Check that one audio cue is added correctly to the dictionary when the
    # category for the key word already exists in the dictionary.
    ([["Beginning", "hello"]]),
    # Check that >1 audio cues are added correctly when all key words are in
    # categories that already exist in the dictionary.
    ([["Footsteps", "runs"], ["Sad", "depressed"], ["Knock", "bang"]]),
    # Check that one audio cue is added correctly when the category for it
    # doesn't exist in the dictionary already.
    ([["Keys", "typed"]]),
    # Check that >1 audio cues are added correclty when none of them already
    # exist in the dictionary.
    ([["Guitar", "pluck"], ["Swallow", "gulp"], ["Breath", "exhale"]]),
    # Check that >1 audio cues are added correctly when some of them are already
    # there and some aren't.
    ([["Beginning", "hello"], ["Swallow", "gulp"], ["Footsteps", "runs"]])
]

# Define standard testing functions to check functions' outputs given certain
# inputs defined above. This also includes functions that don't take any inputs.

def test_sound_effect_keys():
    """
    Check that the newly defined categories related to sound effects have been
    added to the list '_sound_effect_keys'.
    """
    book_sess = BookSession()
    huff = "Huff" in book_sess.get_sound_effect_keys()
    fire = "Fire" in book_sess.get_sound_effect_keys()
    footsteps = "Footsteps" in book_sess.get_sound_effect_keys()
    laughter = "Laughter" in book_sess.get_sound_effect_keys()
    horse = "Horse" in book_sess.get_sound_effect_keys()
    clock = "Clock" in book_sess.get_sound_effect_keys()
    knock = "Knock" in book_sess.get_sound_effect_keys()

    assert huff and fire and footsteps and laughter and horse and clock and \
        knock is True

def test_music_keys():
    """
    Check that the newly defined categories related to sound effects have been
    added to the list '_sound_effect_keys'.
    """
    book_sess = BookSession()
    beginning = "Beginning" in book_sess.get_music_keys()
    sad = "Sad" in book_sess.get_music_keys()

    assert beginning and sad is True

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
    book_sess = BookSession()
    assert book_sess.check_for_key_word(audio_cue) == category_name

def test_get_sound_effect_keys():
    """
    Check that get_sound_effect_keys returns the correct list of keys.
    """
    book_sess = BookSession()
    assert book_sess.get_sound_effect_keys() == ["Huff", "Fire", "Footsteps", \
        "Laughter", "Horse", "Clock", "Knock"]

def test_get_music_keys():
    """
    Check that get_music_keys returns the correct list of keys.
    """
    book_sess = BookSession()
    assert book_sess.get_music_keys() == ["Beginning", "Sad"]

@pytest.mark.parametrize("text, key_word", check_for_key_word_cases)
def test_check_for_key_word(text, key_word):
    """
    Check that an inputted string of text is correctly checked for any audio
    cues by check_for_key_word and that the correct key word is returned. Ensure
    that None is returned if there are no key words in the text.

    Args:
        text: A string representing the text to be checked for an audio cue.
        key_word: A string representing the key word that is supposed to be
            found in the text by the function and the type None if there
            is supposed to be no key word in the text.
    """
    book_sess = BookSession()
    assert book_sess.check_for_key_word(text) == key_word

@pytest.mark.parametrize("key, location", find_audio_location_cases)
def test_find_audio_location(key, location):
    """
    Check that find_audio_location updates the _location variable for
    BookSession with the correct list representing the location.

    Args:
        key: A string representing the category name for the audio cue for which
            the location is to be found.
        location: A list of two strings representing the directory location of
            the audio files corresponding to the category name (key) inputted.
    """
    book_sess = BookSession()
    book_sess.find_audio_location(key)
    assert book_sess.get_location() == location

@pytest.mark.parametrize("key", pick_random_audio_cases)
def test_pick_random_audio(key):
    """
    Check that for the given location, a random file from the folder of audio
    files corresponding to it's location is given.

    Args:
        key: A string representing the category name related to which the
            audio file will be randomly chosen.
    """
    book_sess = BookSession()
    book_sess.find_audio_location(key)
    assert book_sess.pick_random_audio() in os.listdir\
        (f"Audio/{book_sess.get_location()[0]}/{book_sess.get_location()[1]}/")

@pytest.mark.parametrize("key", pick_random_audio_cases)
def test_play_audio(key):
    """
    Check that for the given location, a random file from the folder of audio
    files corresponding to it's location is played through pygame.

    Args:
        key: A string representing the category name related to which the
            audio file will be randomly played.
    """
    book_sess = BookSession()
    book_sess.find_audio_location(key)
    assert book_sess.play_audio() is True


@pytest.mark.parametrize("key_to_word_list", add_key_word_cases)
def test_add_key_word(key_to_word_list):
    """
    Check that the new audio cues from the list inputted are correctly added
    to the dictionary.

    Args:
        key_to_word_list: A list of strings where the first string is the name
            of the category (the key) and the second is the audio cue to add to
            that category (the value).
    """
    book_sess = BookSession()
    book_sess.add_key_word(key_to_word_list)

    all_added_correctly = True
    for new_audio_cue in key_to_word_list:
        if book_sess.check_for_key_word(new_audio_cue[1]) is None:
            all_added_correctly = False

    assert all_added_correctly is True
