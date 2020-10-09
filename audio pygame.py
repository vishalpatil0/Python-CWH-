import pygame

file = 'song.mp3'
pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
pygame.mixer.music.load(file)

pygame.mixer.music.play()

pygame.event.wait()