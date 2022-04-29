"""
"""
from book_session import BookSession


class Cinderella(BookSession):
    """
    """
    def __init__(self):
        super(Cinderella, self).__init__()

        # Add specific words to the keys for each music group
        self.key_words = add_key_word(self.key_words, "Beginning", "poof")
        self.key_words = add_key_word(self.key_words, "Beginning", "grant")
        self.key_words = add_key_word(self.key_words, "Beginning", "wand")
        self.key_words = add_key_word(self.key_words, "Beginning", "gone")
        self.key_words = add_key_word(self.key_words, "Beginning", "turned")
        self.key_words = add_key_word(self.key_words, "Wind", "blow")
        self.key_words = add_key_word(self.key_words, "Scary", "shout")
        self.key_words = add_key_word(self.key_words, "Scary", "scream")
        self.key_words = add_key_word(self.key_words, "Scary", "yell")
        self.key_words = add_key_word(self.key_words, "Scary", "only")
        self.key_words = add_key_word(self.key_words, "Scary", "cried")
        self.key_words = add_key_word(self.key_words, "Scary", "scream")
        self.key_words = add_key_word(self.key_words, "Scary", "quiet")
        self.key_words = add_key_word(self.key_words, "Festive", "bride")
        self.key_words = add_key_word(self.key_words, "Festive", "joy")
        self.key_words = add_key_word(self.key_words, "Festive", "wonderful")
        self.key_words = add_key_word(self.key_words, "Festive", "heart")
        self.key_words = add_key_word(self.key_words, "Festive", "room") # Second only
        self.key_words = add_key_word(self.key_words, "Festive", "perfect")
        self.key_words = add_key_word(self.key_words, "Sad", "work")
        self.key_words = add_key_word(self.key_words, "Sad", "dirty")
        self.key_words = add_key_word(self.key_words, "Sad", "wrong")
        self.key_words = add_key_word(self.key_words, "Sad", "left")
        self.key_words = add_key_word(self.key_words, "Sad", "sad")
        self.key_words = add_key_word(self.key_words, "Horse", "rode")
        self.key_words = add_key_word(self.key_words, "Horse", "off")

def add_key_word(key_words, key, word):
    """
    """
    if key in key_words.keys():
        key_words[key] = key_words.get(key).append(word)
    else:
        key_words[key] = [word]

    return key_words

c = Cinderella()
print(c)
