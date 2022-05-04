import pygame
import time

###### Unnecessary code ######################################################
pygame.init()
pygame.mixer.init()
sounda = pygame.mixer.Sound("Audio/Sound_Effects/Footsteps/footsteps_2.wav")
sounda.play()
time.sleep(8) # specify sleep time as length of file/time wanted to play for