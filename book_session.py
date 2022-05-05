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
        _key_words: A dictionary mapping lists of audio cue to general category
            names. Here, the keys are strings and the values are lists of
            strings.
        _sound_effect_keys: A list of strings representing all the category
            names for sound effect related cues.
        _music_keys: A list of strings representing all the category names for
            background music related cues.
        _location: A list containing two strings representing the path
            containing the files from which one is to be randomly returned.
            Here, the first string represents the directory "Sound_Effects"
            or "Music", while the second string represents the more narrow
            category name, such as "Clock" or "Fire".
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
        self._location = []

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
        print(f"final location:  {location}")


        self._location = location

    def pick_random_audio(self):
        """
        Return a random file from the folder given through the '_location'.

        Returns:
        A string representing the name of a random file inside the path
        specified.
        """

        all_files = os.listdir(f"Audio/{self._location[0]}/" +
            f"{self._location[1]}/")
        return random.choice(all_files)

    def play_audio(self):
        """
        Select and play the audio for a random file in the location specified
        through the input

        Pick a random file using the function 'pick_random_audio' and through
        pygame's mixer, load and play the file for up to 6 seconds.
        """
        # Load random file from location.
        location = self._location
        file_name = self.pick_random_audio()

        # Play the file for up to 6 seconds.
        pygame.mixer.music.load(f"Audio/{location[0]}/" +
            f"{location[1]}/{file_name}")
        pygame.mixer.music.play()
        time.sleep(6)

    def add_key_word(self, key_words_dict, key_to_word_list):
        """
        Given a pre-existing dictionary of keys mapping to lists, from a list
        of lists, map the second string to the first one.

        For example:
        Given a dictionary:
            {"Greetings": ["Hello", "Hola"], "Goodbyes": ["Bye", "Adios"]}
        and a list of lists:
            [["Greetings", "Annyeong"], ["Questions", "How are you"]]
        map the second string to the first one:
            {"Greetings": ["Hello", "Hola", "Annyeong],
             "Goodbyes": ["Bye", "Adios"],
             "Questions": ["How are you"]}

        Args:
            key_words_dict: A dictionary mapping lists of audio cue to general
                category names. Here, the keys are strings and the values are
                lists of strings.
            key_to_word_list: A list of lists of length two containing strings
                where the first string is the name of the category (the key)
                and the second is the audio cue to add to that category (the
                value).

        Returns:
        The same dictionary with the new audio cues and categories added to it.
        """
        for key_and_word_group in key_to_word_list:
            key = key_and_word_group[0]
            word = key_and_word_group[1]

            # Add to the current list under the key if the key exists.
            if key in key_words_dict.keys():
                key_words_dict.get(key).append(word)

            # Create a new list under the new key if the key does not exist.
            else:
                key_words_dict[key] = [word]

        return key_words_dict
