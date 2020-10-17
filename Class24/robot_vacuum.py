import csv

def main():

    # Write a function that turns our CSV into a grid
#     room = csv_to_grid("room1.csv")
#     
# #     print(room)
# 
# #     for row in room:
# #         print(row)
# 
#     ### Write a function that prints a room nicely
#     print_room(room)
#     
#     ### Get the location of the vacuum
#     location = find_element(room, "vacuum")
#     print(location)


    ### Write a function that moves the vacuum in a given direction
    
    ### Move right, then right, then down
#     print("Moving vacuum right")
#     (room, location) = move_vacuum(room, location, "R")
#     print_room(room)
#     
#     print("Moving vacuum right")
#     (room, location) = move_vacuum(room, location, "R")
#     print_room(room)
# 
#     print("Moving vacuum down")
#     (room, location) = move_vacuum(room, location, "D")
#     print_room(room)
#     
#     ### Try moving vacuum to the right 10 times
#     for _ in range(10):
#         input("Moving vacuum right. Hit enter to continue")
#         (room, location) = move_vacuum(room, location, "R")
#         print_room(room)


    ####################
    room = csv_to_grid("room2.csv")
    
    ### Write a function that prints a room nicely
    print_room(room)
    
    ### Get the location of the vacuum
    location = find_element(room, "vacuum")

    input("Moving vacuum up")
    (room, location) = move_vacuum(room, location, "U")
    print_room(room)
    input("Moving vacuum up")
    (room, location) = move_vacuum(room, location, "U")
    print_room(room)
    input("Moving vacuum left")
    (room, location) = move_vacuum(room, location, "L")
    print_room(room)

    for _ in range(4):
        
        for _ in range(7):
            input("Moving vacuum right")
            (room, location) = move_vacuum(room, location, "R")
            print_room(room)  
            
        input("Moving vacuum down")
        (room, location) = move_vacuum(room, location, "D")
        print_room(room)

        for _ in range(7):
            input("Moving vacuum left")
            (room, location) = move_vacuum(room, location, "L")
            print_room(room)

        input("Moving vacuum down")
        (room, location) = move_vacuum(room, location, "D")
        print_room(room)



def move_vacuum(room, location, direction):
    """Moves the vacuum at location in room in the given direction."""

    ### Get the current row and col:
    (row, col) = location
    
    ### Figure out the row and column where the vacuum intends to go,
    ### in case there's an obstacle there
    
    if direction == "R":
        # increase column by 1
        intended_row = row
        intended_col = col + 1
    elif direction == "L":
        # decrease column by 1
        intended_row = row
        intended_col = col - 1
    elif direction == "D":
        # increase row by 1
        intended_row = row + 1
        intended_col = col
    elif direction == "U":
        # decrease row by 1
        intended_row = row - 1
        intended_col = col
        
    if room[intended_row][intended_col] == "obstacle":
        ### If an obstacle, can't move there, so just return the original room and location
        return (room, location)
    else:
        room[row][col] = "clean"
        room[intended_row][intended_col] = "vacuum"
        return (room, (intended_row, intended_col))
        
        


def print_room(room):
    """Prints a nice version of the room, with one character per cell in the room.
    This might look like:
    OOOOO
    O...O
    O.V.O
    O..~O
    O~~.O
    OOOOO"""
    
    for row in room:
        row_string = ""
        
        for cell in row:
            
            if cell == "obstacle":
                row_string += "O"
            elif cell == "clean":
                row_string += "."
            elif cell == "dirt":
                row_string += "~"
            elif cell == "vacuum":
                row_string += "V"
        
        print(row_string)
    
    print()
    
    
    


def csv_to_grid(filename):
    """Turns the CSV given by the filename into a grid and returns it."""
    
    file = open(filename, "r")
    reader = csv.reader(file)
    
    grid = []
    for row in reader:
        grid.append(row)
        
    return grid


    
def find_element(grid, element):
    """Find the row and column indices of an element, if it is in the grid.
    Otherwise, returns None to indicate that the element wasn't found."""
    
    ## First, iterate over the rows
    for row_num in range(len(grid)):
        ## Within a row, iterate over the columns
        for col_num in range(len(grid[row_num])):
            ## Check if this row_num and col_num has element
            if grid[row_num][col_num] == element:
                return (row_num, col_num)
    
    return None


if __name__ == "__main__":
    main()
    