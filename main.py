import pygame
import time

pygame.init()
pygame.mixer.init()
sounda = pygame.mixer.Sound("Audio/Sound_Effects/Footsteps/footsteps_1.wav")
sounda.play()
time.sleep(8) # specify sleep time as length of file/time wanted to play for
