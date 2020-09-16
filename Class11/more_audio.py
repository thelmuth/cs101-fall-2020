from cs101audio import *
import random

song = Audio()

song.open_audio_file("star-wars.wav")

print("The length of this song in miliseconds is", len(song))


### Make every other second loud and soft

loud_and_quiet = Audio()
for index in range(0, len(song), 1000):
    second = song[index : index + 1000]
    
    print(index)
    
    if (index // 1000) % 2 == 0:
        second.apply_gain(10)
    else:
        second.apply_gain(-10)
    
    loud_and_quiet += second

loud_and_quiet.play()
    
### We want to split song into 1-second chunks and scramble them

samples = []
for index in range(0, len(song), 1000):
    second = song[index : index + 1000]
    samples.append(second)
    
random.shuffle(samples)

remix = Audio()
for sample in samples:
    remix += sample

remix.save_to_file("remixed_star_wars2.wav")
remix.play()
    
    
    
    

