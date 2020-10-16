
def main():
    
    ## Create a grid of color strings, which could be pixels in an image.
    colors = [["green", "orange", "brown", "orange"],
              ["blue", "green", "green", "orange"],
              ["purple", "red", "blue", "red"],
              ["yellow", "red", "green", "yellow"]]
    
    no_repeats = [["yellow", "blue"],
                  ["orange", "red"]]
    
    ### Write a function that finds the row and column of an element in a grid

#     print("brown:", find_element(colors, "brown"))
#     print("red:", find_element(colors, "red"))
#     print("elephant:", find_element(colors, "elephant"))
#     
    ### What if we want all locations of an element in the grid?
#     print("green:", find_all(colors, "green"))
#     print("elephant:", find_all(colors, "elephant"))
    
    
    ### Want to find adjacent elements that are the same
#     print(find_adjacent_same_element(colors))
#     print(find_adjacent_same_element(no_repeats))


    ### What if we want adjacent same elements in the same column?
    print(find_adjacent_same_element_column(colors))
    print(find_adjacent_same_element_column(no_repeats))


def find_adjacent_same_element_column(grid):
    """Finds two elements that are adjacent in the same column of the grid.
    Returns the (row, col) of the first one.
    If elements aren't found, returns None."""
    
    ### len(grid[0]) gives us the number of columns
    for col_num in range(len(grid[0])):
        for row_num in range(len(grid) - 1):
            element = grid[row_num][col_num]
            next_element = grid[row_num + 1][col_num]
            
            if element == next_element:
                return (row_num, col_num)
    
    return None


def find_adjacent_same_element(grid):
    """Finds two elements that are adjacent in the same row of the grid.
    Returns the (row, col) of the first one.
    If elements aren't found, returns None."""
    
    for row_num in range(len(grid)):
        for col_num in range(len(grid[row_num]) - 1):
            element = grid[row_num][col_num]
            next_element = grid[row_num][col_num + 1]
            
            if element == next_element:
                return (row_num, col_num)
    
    return None
    
    
def find_all(grid, element):
    """Find the row and column indices of all occurences of element
    in the grid, and return them as a list."""
    
    locations = []

    ## First, iterate over the rows
    for row_num in range(len(grid)):
        
        ## Within a row, iterate over the columns
        for col_num in range(len(grid[row_num])):
            
            ## Check if this row_num and col_num has element
            if grid[row_num][col_num] == element:
                locations.append((row_num, col_num))
    
    return locations
    
    
def find_element(grid, element):
    """Find the row and column indices of an element, if it is in the grid.
    Otherwise, returns None to indicate that the element wasn't found."""
    
    ## First, iterate over the rows
    for row_num in range(len(grid)):
#         num_cols = len(grid[row_num])
        
        ## Within a row, iterate over the columns
        for col_num in range(len(grid[row_num])):
            #print(row_num, col_num)
    
            ## Check if this row_num and col_num has element
            if grid[row_num][col_num] == element:
                return (row_num, col_num)
    
    return None
    
    

def print_grid(grid):
    """Prints a grid in a nicer way."""
#     for row in grid:
#         print(row)

    for row_num in range(len(grid)):
        row = grid[row_num]
        print(row_num, row)
    


if __name__ == "__main__":
    main()
    