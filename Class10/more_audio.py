from cs101audio import *
import random

song = Audio()

# song.open_audio_file("star-wars.wav")
song.open_audio_file("skyward-sword.wav")

print("The length of this song in miliseconds is", len(song))
# song.play()


reverse = Audio()

song_list = song.get_sample_list()
song_list.reverse()
reverse.from_sample_list(song_list)

reverse.save_to_file("reversed-ss.wav")

reverse.play()
