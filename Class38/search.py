import random

def main():

    numbers = [1, 3, 5, 7, 9]
    
    print(my_in(5, numbers))
    print(my_in(12, numbers))
    
    
def my_in(target, lst):
    """Does the same thing as 'in', without using it."""
    
    for element in lst:
        if element == target:
            return True

    return False
    
    
    


    
if __name__ == "__main__":
    main()
