"""
Parent class to create audio cues for a specific book.
"""
import pygame
import time
import os
import random
import listener as ls


class BookSession():
    """
    Audio cues for storybooks in general and basic functionality to play the 
    audio.

    Attributes:
        _key_words: A dictionary mapping each audio cue to a general category of
            sound effects or music. Here, the keys are strings and the values
            are lists of strings.
        _sound_effect_keys: A list of strings representing all the category
            names for sound effect related cues.
        _music_keys: A list of strings representing all the category names for
            background music related cues.
    """

    def __init__(self):
        """
        Initialize the session by initializing pygame's music and adding basic
        audio cues to the dictionary and lists.
        """
        # Initalize pygame and pygame's music mixer.
        pygame.init()
        pygame.mixer.init()

        self._key_words = {"Beginning": ["once upon a time", \
            "happily ever after"], "Huff": ["huff"], \
            "Fire": ["fire"], "Footsteps": ["running", "ran", "walk", "walking"\
            ], "Laughter": ["laugh"], "Sad": ["sad"], "Horse": ["horse"], \
            "Clock": ["dong"], "Knock": ["knock", "knocked"]}
        self._sound_effect_keys = ["Huff", "Fire", "Footsteps", "Laughter", \
            "Horse", "Clock", "Knock"]
        self._music_keys = ["Beginning", "Sad"]

    def check_for_key_word(self, transcribed_text):
        """
        Given a string of text, check for any of the audio cues and returns
        which one is present. 

        If there is more than one cue present in the text, only the first one's
        category (key) will be returned.

        Args:
            transcribed_text: A string representing the text to check for audio
                cues.

        Returns:
        A string representing the category name, the key from the dictionary,
        mapping to the audio cue that was first found in the text and None if
        there are no cues present.
        """
        for key, value in self._key_words.items():
            for word in value: 
                if word in transcribed_text:
                    return key
        return None

    def find_audio_location(self, key):
        """
        Inside of the directory 'Audio', find the location of the category (key)
        entered. 

        Current setup of files separates them into directories labeled 'Sound
        Effects' and 'Music', and further into directories for each narrower
        category (the key entered).

        For example: Audio files for a clock ticking are present in
        'Audio/Sound_Effects/Clock'. Therefore, ["Sound_Effects", "Clock"] is
        returned.

        Args:
            key: A string representing the name of the category for which the
                location is to be found.

        Returns:
        A list (length 2) of strings representing the two folders inside which
        the audio files for the category (key) inputted exist.
        """
        location = []
    
        # Pick whether the folder is Sound_Effects or Music.
        if key in self._sound_effect_keys:
            location = location + ["Sound_Effects"]
        else:
            location = location + ["Music"]
        
        # Pick the nested folder
        location = location + [key]

        return location

    def pick_random_audio(self, location):
        """
        Return a random file from the folder given through the input 'location'.

        Args:
            location: A list containing two strings representing the path
                containing the files from which one is to be randomly returned.
                Here, the first string represents the directory "Sound_Effects"
                or "Music", while the second string represents the more narrow
                category name, such as "Clock" or "Fire". 

        Returns:
        A string representing the name of a random file inside the path
        specified.
        """
        return random.choice(os.listdir(f"Audio/{location[0]}/{location[1]}/"))

    def play_audio(self, location):
        """


        Args:
            location: A list containing two strings representing the beginning
                part of the path containing the single file that is to be
                played. Here, the first string represents the directory
                "Sound_Effects" or "Music", while the second string represents
                the more narrow category name, such as "Clock" or "Fire". 
        """
        file_name = self.pick_random_audio(location)
        pygame.mixer.music.load(f"Audio/{location[0]}/{location[1]}/" +
            f"{file_name}")
        pygame.mixer.music.play()
        time.sleep(6)

    def add_key_word(self, key_words_dict, key_to_word_list):
        """
        """
        for key_and_word_group in key_to_word_list:
            key = key_and_word_group[0]
            word = key_and_word_group[1]

            if key in key_words_dict.keys():
                key_words_dict.get(key).append(word)
            else:
                key_words_dict[key] = [word]

        return key_words_dict
