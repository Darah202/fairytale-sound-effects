"""
"""
import pygame
import time
import cinderella as cd
import listener as ls

class Controller():
    """
    """
    def __init__():
        """
        """
        _listener = ls.Listener()
        _session = cd.Cinderella()

    def listen_for_key_word(self):
        """
        """
        key_word_found = ""

        # Keep listening until a keyword is said
        while (len(key_word_found) < 1):
            text_heard = self._listener.listening()
            key_word_found = self._session.check_for_key_word(text_heard)

        return key_word_found
    
    def find_and_play_key_words(self):
        """
        """
        key_word = self.listen_for_key_word()
        if (len(key_word) > 1):
            location = self._session.find_audio_location(key_word)
            audio = self._session.pick_random_audio(location)
            self._session.play_audio(location, audio)
        
        

        

