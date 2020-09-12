
### We often want to accumulate a value in a variable each time
### through a loop.
### Need a variable with a starting value
### We call this variable the _accumulator_
# numbers = [16, 2999, 308, 0, 10000]
# the_sum = 0 # This is the accumulator
# 
# for num in numbers:
#     print(the_sum)
#     the_sum = the_sum + num
#     
# print("The numbers in", numbers, "add up to", the_sum)


# colors = ["red", "blue", "yellow"]
# for color in colors:
#     mo.pencolor(color)
#     mo.forward(100)


## Sum all of the numbers between 0 and 1 million
# the_sum = 0
# for num in range(1000000):
#     the_sum = the_sum + num
# print("The sum of all ints between 0 and 1 million is", the_sum)

# the_sum = 0
# for num in range(1000000):
#     the_sum += num
# print("The sum of all ints between 0 and 1 million is", the_sum)

# product = 1
# for number in range(1, 21): # actually multiplies up to 20
#     product *= number
# print(product)

### Want to find a list of each of these numbers squared
# numbers = [16, 2999, 308, 0, 10000]
# squares = []
# for num in numbers:
#     squares.append(num * num)
# print(squares)

### Accumulate over a string
city = "NYC"
new_string = ""
for char in city:
    #new_string = new_string + char + "."
    new_string += char + "."
print(new_string)




