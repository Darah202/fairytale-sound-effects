Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@emascillaro 
emascillaro
/
SeniorProject_FALL
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
SeniorProject_FALL/Final/Speech_Recognition.py /
@emascillaro
emascillaro for Dec 23
Latest commit 7076e8e on Dec 20, 2020
 History
 1 contributor
50 lines (39 sloc)  1.17 KB
  
import speech_recognition as sr
import pyaudio
import nltk
from nltk.tokenize import PunktSentenceTokenizer

# Creates a recognizer instance
r = sr.Recognizer()

"""
Transcribing speech from microphone input
"""

# Use default system microphone as source,
print("use default microphone as source:")
mic = sr.Microphone()

# Use specified microphone as source
#mic = sr.Microphone(device_index = 2)

try:
    # Record Data from Microphone input
    print("record data from microphone input:")
    with mic as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # Invokes Google Web Speech API & outputs text
    print("Entire Phrase: ")
    text_output = r.recognize_google(audio)
    print(text_output.lower())

    #Part of Speech Stuff
    sentences = nltk.sent_tokenize(text_output.lower())

    data = []
    noun_list = []
    for sent in sentences:
        data = data + nltk.pos_tag(nltk.word_tokenize(sent))

    for word in data:
        if 'NN' in word[1]:
            #print(word)
            noun_list.append(word[0])

    print("nouns:", noun_list)
    understood_speech = 1

except:
    print("Could not Recognize speech")
    understood_speech = 0
© 2022 GitHub, Inc.
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
Loading complete