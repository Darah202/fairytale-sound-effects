"""
"""
import pygame
import time
import cinderella as cd
import listener as ls

class SoundEffectsController():
    """
    """
    def __init__(self):
        """
        """
        self._listener = ls.Listener()
        self._session = cd.Cinderella()

    def listen_for_key_word(self):
        """
        """
        key_word_found = ""
        text_and_key_word = [""]

        # Keep listening until a keyword is said
        while (len(key_word_found) < 1):
            text = self._listener.listening()
            text_and_key_word[0] = text

            if "the end" in text:
                text_and_key_word[0] = "the end"
                key_word_found = "the end"
            else:
                key_word_found = str(self._session.check_for_key_word(text))

        text_and_key_word.append(key_word_found)
        return text_and_key_word
    
    def find_and_play_key_word(self, key_word):
        """
        Args:
        """
        location = self._session.find_audio_location(key_word)
        audio = self._session.pick_random_audio()
        self._session.play_audio()

    def combine_listening(self):
        """
        """
        while True:
            text_and_key_word = self.listen_for_key_word()
            print(text_and_key_word)
            self.find_and_play_key_word(text_and_key_word[1])
