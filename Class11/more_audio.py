from cs101audio import *
import random

song = Audio()

song.open_audio_file("star-wars.wav")

print("The length of this song in miliseconds is", len(song))
song.play()


