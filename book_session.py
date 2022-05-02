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
        
        return ""

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
        return random.choice(os.listdir(f"Audio/Sound_Effects/Footsteps"))
        #{location[0]}/{location[1]}/

    def play_audio(self, location, audio_name):
        """
        """
        pygame.init()
        pygame.mixer.init()
        file_name = self.pick_random_audio(location)
        sounda = pygame.mixer.Sound(f"Audio/Sound_Effects/Footsteps/{file_name}")
       #{location[0]}/{location[1]}/{file_name}
        sounda.play()
        time.sleep(8)

    def __repr__(self):
        """
        """
        return str(self._key_words)


def add_key_word(key_words, key, word):
    """
    """
    if key in key_words.keys():
        key_words.get(key).append(word)
    else:
        key_words[key] = [word]

    return key_words
