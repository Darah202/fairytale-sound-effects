import pygame
import pydub
from pydub import AudioSegment
import os

os.chdir("Audio/Sound_Effects/Footsteps/")

pygame.init()
pygame.mixer.init()
sounda = pygame.mixer.Sound("Footsteps Sound Effect (Royalty Free)-nS9VmrOzd7o.wav")
sounda.play()

# youtube-dl -x --audio-format mp3 --audio-quality 256K 'URL'