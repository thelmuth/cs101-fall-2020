
# print(0)
# print(1)
# print(2)
# print(3)
# print(4)
# print(5)

# for x in range(6):
#     print(x)
    
# for x in range(-5, 10):
#     print(x)
#     x_squared = x * x
#     print("squaring x gives", x_squared)
#     print()

# for x in range(5, 20, 3):
#     print(x)


# for time in range(10, -1, -1):
#     print("T-minus", time, "seconds")

### Example of changing range's values during loop
### This doesn't have an effect on range
# start = 10
# end = -1
# step = -1
# for time in range(start, end, step):
#     step = step - 1
#     print("T-minus", time, "seconds")


### We have a string and want to do something for every
### character in the string
# animal = "panda"
# for index in range(len(animal)):
#     char = animal[index]
#     print("The character at index", index, "is", char)
    
### What's this going to do
# animal = "panda"
# for index in range(len(animal)):
#     print(animal[:index])

### We can also directly iterate over a string.
### This will assign each character in the string to the
### loop variable
# animal = "panda"
# for char in animal:
#     print("The character is", char)
# print("This way, you don't have access to the index :(")
    
# numbers = [16, 2999, 308, 0, 10000]
# for num in numbers:
#     print("The num is", num)

### We often want to accumulate a value in a variable each time
### through a loop.
### Need a variable with a starting value
### We call this variable the _accumulator_
# numbers = [16, 2999, 308, 0, 10000]
# the_sum = 0 # This is the accumulator
# for num in numbers:
#     the_sum = the_sum + num
# print("The numbers in", numbers, "add up to", the_sum)





