"""
"""
from book_session import BookSession
from book_session import add_key_word


class ThreeLittlePigs(BookSession):
    """
    """
    def __init__(self):
        super(ThreeLittlePigs, self).__init__()

        # Add specific words to the keys for each music group
        self._key_words = add_key_word(self._key_words, "Beginning", "poof")
        
