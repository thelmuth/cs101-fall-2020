
NUMBERS = "0123456789"

def main():
    
    #                                   V-- the argument
    first = first_number_in_string("You owe $5.99")
    print(first)
    print("we got here")
    
    no_numbers = first_number_in_string("This has no numbers :(")
    print(no_numbers)
    
    ### Write a function that returns True if a number is even
    print(even(5))
    print(even(6))
    
    
def first_number_in_string(string):
    """Returns the first character in the string that is a number.
    Note: string is the parameter to this function.
    If there are no numbers in string, return 'sorry'.
    """
    
    for character in string:
        if character in NUMBERS:
            return character
        
    return 'sorry'

def even(number):
    """Returns True if number is even, False otherwise."""
    
    ### This is unnecesarily long:
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
    # Q: What does the expression (number % 2 == 0) give us?
    # A: Boolean, which is true if number is even!
    return number % 2 == 0
    
    
    
if __name__ == "__main__":
    main()