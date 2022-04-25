"""
Transcribing speech from microphone input
"""

import speech_recognition as sr
import pyaudio
import nltk
from nltk.tokenize import PunktSentenceTokenizer

# Creates a recognizer instance
r = sr.Recognizer()

# Use default system microphone as source
print("use default microphone as source:")
mic = sr.Microphone()

# Use specified microphone as source
#mic = sr.Microphone(device_index = 2)

try:
    # Record Data from Microphone input
    print("Start reading!")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Invokes Google Web Speech API & outputs text
    print("Here's what you said: ")
    text_output = r.recognize_google(audio)
    print(text_output.lower())

except:
    print("Could not Recognize speech")
    understood_speech = 0
