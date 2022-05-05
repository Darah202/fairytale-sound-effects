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

        # Keep listening until a keyword is said
        while (len(key_word_found) < 1):
            text_heard = self._listener.listening()
            key_word_found = str(self._session.check_for_key_word(text_heard))

        return text_heard, key_word_found
    
    def find_and_play_key_word(self, key_word):
        """
        Args:
        """
        print(f"key_word:  {key_word}")
        location = self._session.find_audio_location(key_word)
        print(f"location:  {location}")
        audio = self._session.pick_random_audio()
        print(f"audio:  {audio}")
        self._session.play_audio()

    def combine_listening(self):

        while True:
            key_word = self.listen_for_key_word()
            self.find_and_play_key_word(key_word[1])

            if "the end" in key_word[0]:
                break
