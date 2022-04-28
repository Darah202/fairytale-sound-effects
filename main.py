import pygame
import os

os.chdir("Audio/Sound_Effects/Footsteps/")

pygame.init()
pygame.mixer.init()
sounda = pygame.mixer.Sound("Footsteps Sound Effect (Royalty Free)-nS9VmrOzd7o.wav")
sounda.play()

# youtube-dl -x --audio-format mp3 --audio-quality 256K 'URL'

# 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