"""
"""
from book_session import BookSession


class Cinderella(BookSession):
    """
    """
    def __init__(self, listener):
        """
        """
        super(Cinderella, self).__init__(listener)

        # Add specific words to the keys for each music group
        _new_keywords = [["Beginning", "poof"], ["Beginning", "grant"], \
            ["Beginning", "wand"], ["Beginning", "gone"], \
            ["Beginning", "turned"], ["Wind", "blow"], ["Scary", "shout"], \
            ["Scary", "scream"], ["Scary", "yell"], ["Scary", "only"], \
            ["Scary", "cried"], ["Scary", "scream"], ["Scary", "quiet"], \
            ["Festive", "bride"], ["Festive", "joy"], ["Festive", "wonderful"],\
            ["Festive", "heart"], ["Festive", "room"], ["Festive", "perfect"], \
            ["Sad", "work"], ["Sad", "dirty"], ["Sad", "wrong"], \
            ["Sad", "left"], ["Sad", "sad"], ["Horse", "rode"], \
            ["Horse", "off"]]

        self._key_words = self.add_key_word(self._key_words, _new_keywords)
        self._sound_effect_keys = self._sound_effect_keys + ["Wind"]
        self._music_keys = self._music_keys + ["Scary", "Festive"]


c = Cinderella()
