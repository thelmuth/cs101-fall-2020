import random

def main():


    ### Write a function that tells whether a character occurs
    ### in a string or not (without using the in operator)
    print(char_finder("h", "this is a string"))
    print(char_finder("q", "this is a string"))


    ### Write a function that returns the total number of occurences
    ### of a character in a string
    
    
    ### Given two lists, write a function that returns a list of all elements
    ### that appear in both lists
    
    print(overlap_elements([1, 2, 3, 4, 5], [6, 7, 3, 8, 1]))
    
    ### Write a function that finds the row and column where
    ### two equal elements appear next to each other in a grid.
    ### (next to in a single row)
    grid = [[4, 6, 2, 9, 1],
            [9, 0, 2, 1, 0],
            [1, 3, 3, 2, 3],
            [0, 3, 6, 8, 8]]
    ## Answer should find the 3's in row 2, so should be (2, 1)
    
    
def overlap_elements(list1, list2):
    """All elements in list1 and list2"""
    
    new_list = []
    for element in list1:
        if element in list2:
            new_list.append(element)
            
    return new_list
    
    
def all_elements(list1, list2):
    """All elements in list1 or list2"""
    
    new_list = []
    for element in list1:
        new_list.append(element)
        
    for element in list2:
        new_list.append(element)
        
    return new_list
    



def char_finder(char, word):
    for character in word:
        if char == character:
            return True
    
    return False


    
if __name__ == "__main__":
    main()
