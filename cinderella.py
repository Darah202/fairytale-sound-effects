"""
"""
from book_session import add_key_word
from book_session import BookSession


class Cinderella(BookSession):
    """
    """
    def __init__(self):
        super(Cinderella, self).__init__()

        # Add specific words to the keys for each music group
        self._key_words = add_key_word(self._key_words, "Beginning", "poof")
        self._key_words = add_key_word(self._key_words, "Beginning", "grant")
        self._key_words = add_key_word(self._key_words, "Beginning", "wand")
        self._key_words = add_key_word(self._key_words, "Beginning", "gone")
        self._key_words = add_key_word(self._key_words, "Beginning", "turned")
        self._key_words = add_key_word(self._key_words, "Wind", "blow")
        self._key_words = add_key_word(self._key_words, "Scary", "shout")
        self._key_words = add_key_word(self._key_words, "Scary", "scream")
        self._key_words = add_key_word(self._key_words, "Scary", "yell")
        self._key_words = add_key_word(self._key_words, "Scary", "only")
        self._key_words = add_key_word(self._key_words, "Scary", "cried")
        self._key_words = add_key_word(self._key_words, "Scary", "scream")
        self._key_words = add_key_word(self._key_words, "Scary", "quiet")
        self._key_words = add_key_word(self._key_words, "Festive", "bride")
        self._key_words = add_key_word(self._key_words, "Festive", "joy")
        self._key_words = add_key_word(self._key_words, "Festive", "wonderful")
        self._key_words = add_key_word(self._key_words, "Festive", "heart")
        self._key_words = add_key_word(self._key_words, "Festive", "room") # Second only
        self._key_words = add_key_word(self._key_words, "Festive", "perfect")
        self._key_words = add_key_word(self._key_words, "Sad", "work")
        self._key_words = add_key_word(self._key_words, "Sad", "dirty")
        self._key_words = add_key_word(self._key_words, "Sad", "wrong")
        self._key_words = add_key_word(self._key_words, "Sad", "left")
        self._key_words = add_key_word(self._key_words, "Sad", "sad")
        self._key_words = add_key_word(self._key_words, "Horse", "rode")
        self._key_words = add_key_word(self._key_words, "Horse", "off")

        self._sound_effect_keys = self._sound_effect_keys + ["Wind"]
        self._music_keys = self._music_keys + ["Scary", "Festive"]


c = Cinderella()
location = c.find_audio_location(c.check_for_key_word("dong"))
c.play_audio(location, c.pick_random_audio(location))
print("done")