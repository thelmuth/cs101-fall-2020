import random
import matplotlib.pyplot as plt
from cs101audio import *

def main():
    
#     x = 0
#     while x ** 3 < 10000:
#         print(x, "cubed is", x ** 3)
#         x += 1

    ### Imagine we want 10 seconds of a snare drum sample
    ### repeating. But, we don't know how many times to play it.
    ### We can use a while loop until the song is 10 seconds long.

#     ten_second_snare = Audio()
#     snare = Audio()
#     snare.open_audio_file("Snare.wav")
#     
#     count = 0
#     while len(ten_second_snare) < 10000:
#         ten_second_snare += snare
#         count += 1
#         
#     print(len(ten_second_snare))
#     print("number of snare taps:", count)
#     ten_second_snare.play()
#     ten_second_snare = ten_second_snare[:1000]

    ### Want to plot y values of 2^x until y > 1000000
#     (x_vals, y_vals) = make_exp_data_max_y(1000000)
#     print(x_vals)
#     print(y_vals)
#     
#     plt.plot(x_vals, y_vals)
#     plt.show()

    ### Guessing game
    ### Computer picks a random number in range 0 to 100
    ### Human repeatedly guesses a number until they get it right

    answer = random.randint(0, 100)
    user_guess = int(input("Enter a guess: "))
    list_of_guesses = []
    
    while user_guess != answer:
        list_of_guesses.append(user_guess)
        print(list_of_guesses)
        
        if user_guess > answer:
            print("Your guess is too high")
        else:
            print("Your guess is too low")
        
        user_guess = int(input("Enter a guess: "))
    
    
    list_of_guesses.append(user_guess)
    print("Yay, you got it!")
    
    plt.plot(list_of_guesses)
    plt.show()
    

def make_exp_data_max_y(max_y):
    """Makes data for the equation y = 2^x
    until the y value is >= max_y."""
    
    x_values = []
    y_values = []
    x = 0
    y = 2 ** x
    
    while y < max_y:
        x_values.append(x)
        y_values.append(y)
        
        x += 1
        y = 2 ** x
    
    return (x_values, y_values)

if __name__ == "__main__":
    main()