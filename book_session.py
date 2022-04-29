"""
"""

class BookSession():
    """
    """
    def __init__(self):
        """
        """
        self.key_words = {"Beginning": ["once upon a time", \
            "happily ever after"], "Huff": ["huff"], \
            "Fire": ["fire"], "Footsteps": ["running", "ran", "walk", "walking"\
            ], "Laughter": ["laugh"], "Sad": ["sad"], "Horse": ["horse"], \
            "Clock": ["dong"], "Knock": ["knock", "knocked"]}

    def __repr__(self):
        """
        """
        return str(self.key_words)

bs = BookSession()
