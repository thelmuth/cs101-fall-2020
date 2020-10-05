import matplotlib.pyplot as plt

### Recall...

### Get integers from the user (perhaps these are polling numbers)
### until the user enters a blank line. Store these integers
### in a list, so that we can plot them.

# integers = []
# x_vals = []
# x = 1
# 
# int_str = input("Enter polling data: ")
# 
# while int_str != "":
#     real_integer = int(int_str)
#     integers.append(real_integer)
#     x_vals.append(x)
#     
#     int_str = input("Enter polling data: ")
#     x += 1
#     
# plt.plot(x_vals, integers)
# plt.show()

### Let's try a slightly different way

integers = []

while True:
    int_str = input("Enter polling data: ")
    
    if int_str == "":
        # break - immediately exits the current loop
        break
    
    real_integer = int(int_str)
    integers.append(real_integer)
    

    
plt.plot(integers)
plt.show()
    
