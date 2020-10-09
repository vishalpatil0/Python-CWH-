#Healthy Programmer
# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log - Every 40 min
# Eyes - eyes.mp3 - every 30 min - EyDone - log - Every 30 min
# Physical activity - physical.mp3 every - 45 min - ExDone - log
# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from time import time


def musiconloop(file,stopper):
    # mixer.pre_init(44100, -16, 2, 2048)
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(2)
    while True:
        ip1=input()
        if ip1==stopper:
            mixer.music.stop()
            break

def logs(msg):
    with open("mylogs.txt",'a') as f:
        f.write(f"{msg} {datetime.now()}\n")



if __name__=="__main__":

    init_water=time()
    init_eyes=time()
    watersecs=6
    eyesecs=10

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time. Enter 'drank' to stop the alarm.")
            musiconloop('sounds/It\'s time to drink water.mp3', 'drank')
            init_water = time()
            logs("Drank Water at")

        if time() - init_eyes >eyesecs:
            print("Eye exercise time. Enter 'done' to stop the alarm.")
            musiconloop('sounds/it is time for eye exercise.mp3', 'done')
            init_eyes = time()
            logs("Eyes Relaxed at")

     