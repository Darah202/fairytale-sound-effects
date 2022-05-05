"""
File to integrate mic input to text and playing of audio files.
"""
import pygame
import time
import book_session as bs
import cinderella as cd
import three_little_pigs as tlp
import listener as ls

class AudioController():
    """
    A controller for the audio input and playing.

    Attributes:
        _listener: An instance of Listener.
        _session_name: An string representing the name of the BookSession chosen
            by the user.
        _session: An instance of BookSession or a subclass of BookSession that
            was chosen by the user.
    """
    def __init__(self, book_session_chosen):
        """
        Intialize the Controller with a Listener to manage mic input and a
        BookSession containing the audio cues. If the inputted name for the book
        is one that already has special cues mapped to it (ex: Cinderella),
        an instance of that subclass is made instead.
        """
        self._listener = ls.Listener()
        self._session_name = book_session_chosen
        self._session = bs.BookSession()

        if self._session_name == "Cinderella":
            self._session = cd.Cinderella()
        if self._session_name == "The 3 Little Pigs":
            self._session = tlp.ThreeLittlePigs()

    def listen_for_key_word(self):
        """
        """
        key_word_found = ""
        text_and_key_word = [""]

        # Keep listening until a keyword is said
        while True:
            text = self._listener.listening()
            text_and_key_word[0] = text

            if "the end" in text:
                text_and_key_word[0] = "the end"
                key_word_found = "the end"
                break
            else:
                key_word_found = self._session.check_for_key_word(text)
                if key_word_found != None:
                    break

        text_and_key_word.append(key_word_found)
        return text_and_key_word
    
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
            text_and_key_word = self.listen_for_key_word()
            print(text_and_key_word)
            
            if text_and_key_word[0] == "the end":
                break

            self.find_and_play_key_word(text_and_key_word[1])
