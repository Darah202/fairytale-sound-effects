"""
Contains subclass of BookSession specifically for the story Three Little Pigs
"""
from book_session import BookSession

class ThreeLittlePigs(BookSession):
    """
    A Three Little Pigs version of BookSession that adds more audio cues
    specific to this story.

    Attributes:
        _new_keywords: A list of lists containing two strings where the first
            string represents the category name (the key) and the second string
            represents the audio cue (the value to be added to the key).
        _key_words: A dictionary mapping lists of audio cue to general category
            names. Here, the keys are strings and the values are lists of
            strings. This is inherited from the parent class and amended through
            the initialization process to include the new keywords from
            '_new_keywords'
        _sound_effect_keys: A list of strings representing all the category
            names for sound effect related cues. This is inherited from the
            parent class and amended to include the new sound effect related
            keys specific to this class.
        _music_keys: A list of strings representing all the category names for
            background music related cues. This is inherited from the
            parent class and amended to include the new background music related
            keys specific to this class.
    """
    def __init__(self):
        """
        Initialize ThreeLittlePigs by first inheriting from the parent class
        'BookSession' and then adding the new audio cues specific to this book.
        """
        # Initialize with variables from BookSession
        super().__init__()

        # Add specific words to the keys for each music group
        self._new_keywords = [["Festive", "you can"], ["Festive", "playing"], \
            ["Festive", "happy"], ["Straw", "straw"], ["Stick", "stick"], \
            ["Brick", "brick"], ["Howl", "wolf"], ["Fire", "boil"], \
            ["Water", "splash"], ["Water", "kettle"], ["Festive", "trouble"], \
            ["Huff", "blue"]]

        self._key_words = self.add_key_word(self._new_keywords)
        self._sound_effect_keys = self._sound_effect_keys + ["Straw", "Stick", \
            "Brick", "Howl", "Water"]
        self._music_keys = self._music_keys + ["Festive"]
