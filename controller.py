"""
audio controller.
"""
from abc import ABC, abstractmethod


class AudioPlayerController(ABC):
    """
    Control the audio player.
    """
    def __init__(self, AudioController):
        """
        This method takes an instance of a AudioController as a parameter and
        stores it as a private instance attribute.
        """
        self._audio_controller = AudioController

    @property
    def audio(self):
        """
        This property returns the audio controller stored in the
        AudioPlayerController instance.
        """
        return self._audio_controller

    @abstractmethod
    def play(self):
        """
        This abstract method does nothing
        """

class SoundController(AudioPlayerController):
    """
    Control the audio player.
    """

    def play(self, book_chosen):
        """
        This method gets input from the user and makes the appropriate move
        on the board. The user's input is expected to be in the form 0 1, where
        the first number represents the row of the board to mark and the second
        number represents the column. In this example 0 1 should try to mark
        row 0, column 1, which is the top center square of the board.
        """

        # Listen for audio cues for the book chosen
        sound_effects = self._audio_controller(book_chosen)
        sound_effects.self._audio_controller.combine_listening()
    