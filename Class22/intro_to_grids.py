
def main():
    
    ## Create a grid of color strings, which could be pixels in an image.
    colors = [["green", "orange", "brown", "orange"],
              ["blue", "green", "green", "orange"],
              ["purple", "red", "blue", "red"],
              ["yellow", "brown", "green", "yellow"]]
    
#     print(colors)

    ## What happens when we index an element of colors?
#     mystery = colors[2]
#     print(mystery)
#     print(mystery[1])
#     print(colors[0])
    
    ### We can use double indexing to get a specific element from the grid
#     print(colors[2][1])
    
    ### We can index in the string???
#     print(colors[2][1][0])
#     print(colors[2][1][1][0][0][0][0]) ### Silly example, but shows that you can repeatedly index a single character at index 0
    
    ### Write a function that prints a grid in a nicer way
#     print_grid(colors)
    
    
    ### Write a function that finds the row and column of an element in a grid

    print("brown:", find_element(colors, "brown"))
    print("red:", find_element(colors, "red"))
    print("elephant:", find_element(colors, "elephant"))
    
    
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
    