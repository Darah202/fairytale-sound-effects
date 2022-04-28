"""
Transcribing speech from microphone input
"""

import speech_recognition as sr
import pyaudio

class Listener:
    """
    This class is used to record audio data and transcribe the spoken words to
    text

    Attributes:
        _recognizer:  A 'speech_recognition.Recognizer' instance which is used
        to recognize speech
    """

    def __init__(self):
        """
        This method creates a recognizer instance
        """

        # Creates a recognizer instance
        self._recognizer = sr.Recognizer()

    def listening(self):
        """
        This method records 3 seconds of audio and transcribes it to text.

        """
        # Use default system microphone as source
        print("use default microphone as source:")
        mic = sr.Microphone()

        try:
            # Record Data from Microphone input for 3 seconds
            print("Start reading!")
            with mic as source:
                self._recognizer.adjust_for_ambient_noise(source)
                audio = self.recognizer.listen(source, duration=3)

            # Invokes Google Web Speech API & outputs text
            print("Here's what you said: ")
            text_output = self._recognizer.recognize_google(audio)
            print(text_output.lower())

        except:
            print("Could not Recognize speech")
            understood_speech = 0