
### Imagine we're creating a website and want the user
### to create a password with at least 8 characters in it.

# password = input("Enter a password: ")
# 
# while len(password) < 8:
#     print("Sorry, password must be at least 8 characters.")
#     password = input("Enter a password: ")
#     
# print("Congrats, your password is", password)

### Get integers from the user (perhaps these are polling numbers)
### until the user enters a blank line. Store these integers
### in a list, so that we can plot them.

integers = []

integer = input("Enter data: ")

while integer != "":
    real_integer = int(integer)
    integers.append(real_integer)
    integer = input("Enter data: ")
    
print(integers) 
    
    
    
    
