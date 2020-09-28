import matplotlib.pyplot as plt
import random
from cs101audio import *

def main():
    
    ### Let's plot the predicted high temp this week
    days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"]
    highs = [81,     68,     60,     63,    61,    58,    57]
    
    # Make a bar chart!
#     plt.bar(days, highs)
#     plt.show()

    # Make a line chart!
#     plt.plot(days, highs)
#     plt.show()
    
    lows = [67, 53, 51, 44, 42, 38, 40]
    
#     plt.plot(days, highs)
#     plt.plot(days, lows)
#     
#     plt.legend(("High Temps", "Low Temps"))
#     plt.show()
    
    ### Let's make data for the function y = 2^x

#     values = make_exp_data(10)
#     x_values = values[0]
#     y_values = values[1]

    ## This is equivalent in Python
    (x_vals, y_vals) = make_exp_data(10)
#     print(x_vals)
#     print(y_vals)

#     plt.plot(x_vals, y_vals)

    # Make the line green and have circles at data points
#     plt.plot(x_vals, y_vals, color="green", marker="o")
    
    # Make the line disappear and make orange circles
#     plt.plot(x_vals, y_vals, color="orange", marker="o", linestyle="none")
#     
#     plt.show()

    ### Visualize music

#     zelda = Audio()
#     zelda.open_audio_file("zelda.wav")
#     
# #     zelda.play()
# 
#     five_ms = zelda[100:105]
#     
#     # Get the sample list, which tells what the amplitude of the sound wave
#     # is at each given moment.
#     
#     sample_list = five_ms.get_sample_list()
#     print(len(sample_list))
#     print(sample_list)
#     
#     plt.plot(sample_list)
#     plt.show()

    ### Visualize some simple generated audio

#     sound = generate_music_note("c4", 500, "sawtooth")
#     sound.play()
# 
#     sound_samples = sound.get_sample_list()
# #     plt.plot(sound_samples)
# #     plt.show()
# 
#     short_sound = sound_samples[5000: 5440]
#     plt.plot(short_sound)
#     plt.show()

    ### Visualize snare hit
    snare = Audio()
    snare.open_audio_file("Snare.wav")
    snare.play()
    
    sample_list = snare.get_sample_list()
    
#     plt.plot(sample_list)


    plt.plot(sample_list[:1000])
    plt.show()
    


def make_exp_data(max_x):
    """Makes data from 0 to max_x for the equation y = 2^x"""
    
    x_values = []
    y_values = []
    
    for x in range(max_x):
        x_values.append(x)
        y_values.append(2 ** x)
    
    return (x_values, y_values)
    
    
    
if __name__ == "__main__":
    main()
    