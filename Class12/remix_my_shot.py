from cs101audio import *

song = Audio()
song.open_audio_file("my-shot.wav")

#song.play()

kick_drum = Audio()
# kick_drum.open_audio_file("Bass-Drum-1.wav")
kick_drum.open_audio_file("Bass-Drum-2.wav")
kick_drum.apply_gain(20)


# beat = 16
# seconds = 11
# bpm = 16 / (11 / 60)

bpm = 92
bps = bpm / 60
ms_per_beat = int(1000 / bps)

# First beat in song is 400 ms in
start = 400
remix = song[:start]

for index in range(start, len(song), ms_per_beat):
    print(index)
    beat = song[index : index + ms_per_beat]
    beat.overlay(kick_drum)
    remix += beat

remix.play()




