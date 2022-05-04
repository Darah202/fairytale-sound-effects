"""
"""
import pygame
import time
import os
import random


class BookSession():
    """
    """
    def __init__(self):
        """
        """
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
        """
        for key, value in self._key_words.items():
            for word in value: 
                if word in transcribed_text:
                    return key
        return None

    def find_audio_location(self, key):
        """
        """
        location = []
    
        if key in self._sound_effect_keys:
            location = location + ["Sound_Effects"]
        else:
            location = location + ["Music"]
        
        location = location + [key]
        return location

    def pick_random_audio(self, location):
        """
        """
        return random.choice(os.listdir(f"Audio/{location[0]}/{location[1]}/"))

    def play_audio(self, location, file_name):
        """
        """
        file_name = self.pick_random_audio(location)
        pygame.mixer.music.load(f"Audio/{location[0]}/{location[1]}/" +\
            "{file_name}")
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
