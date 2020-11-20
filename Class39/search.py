import random
import time

def main():

    numbers = [1, 3, 5, 7, 9]
    
#     print(my_in(5, numbers))
#     print(my_in(12, numbers))
#     
#     print(binary_in(5, numbers))
#     print(binary_in(12, numbers))

    large = list(range(10000000))
                    #   9876543
                    
    print("done making list")
    
    start_time = time.time()
    
#     print(my_in(9876544, large))
#     print(my_in(-1, large))
    
    print(binary_in(9876544, large))
    print(binary_in(-1, large))
    
    end_time = time.time()
    
    print("Total time it took:", end_time - start_time)
    
def my_in(target, lst):
    """Does the same thing as 'in', without using it."""
    
    for element in lst:
        if element == target:
            return True

    return False
    

def binary_in(target, sorted_list):
    """In a sorted list, runs binary search to find target."""
    
    left = 0
    right = len(sorted_list) - 1
    
    iterations = 0
    
    while left <= right:
        iterations += 1
        midpoint = (right + left) // 2
        
        if target == sorted_list[midpoint]:
            print("Number of lookups:", iterations)
            return True
        elif target < sorted_list[midpoint]:
            right = midpoint - 1
        else:
            left = midpoint + 1
    
    print("Number of lookups:", iterations)
    
    return False
    
    


    
if __name__ == "__main__":
    main()
