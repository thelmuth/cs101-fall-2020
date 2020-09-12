from cs101audio import *

song = Audio()

# song.open_audio_file("Kanye-West-Stronger.wav")
song.open_audio_file("Beatles-Hey-Jude.wav")

# song.play()

### Each Audio object allows us to access them in 1 millisecond increments
### We can use operators like indexing and slicing, just
### like we do with lists and strings.

### Break the song into 3 parts:
# intro = song[:5000]
# kanye = song[5000:23200] # Used guess and check to get the right part
# rest = song[23200:]
# 
# # Speed up this portion of the music
# kanye.change_speed(1.5)
# 
# new_song = intro + kanye + rest
# new_song.play()

# new_song.save_to_file("chipmunk.wav")


#### Speed up a song by 1% for each second it plays

speed = 1

# print(len(song)) ## length in miliseconds

# for index in range(0, len(song), 1000):
#     print("At index", index, ", the speed is", speed)
#     clip = song[index : index + 1000]
#     clip.change_speed(speed)
#     clip.play()
#     speed += 0.01
    
    
# If we want a new Audio object:
new_song = Audio()
for index in range(0, len(song), 1000):
    print("At index", index, ", the speed is", speed)
    clip = song[index : index + 1000]
    clip.change_speed(speed)
#     clip.play()
    new_song += clip
    speed += 0.01

new_song.play()
    
    
    
    


