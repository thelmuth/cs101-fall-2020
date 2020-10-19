import csv

def main():

    # Write a function that turns our CSV into a grid
    room = csv_to_grid("room2.csv")

    ### Write a function that prints a room nicely
    print_room(room)
    
    ### Get the location of the vacuum
    location = find_element(room, "vacuum")
    print(location)
    
    ### Test the room_distance function
#     print(room_distance((3, 2), (1, 8)))
    
    
    ### Test out finding the closest dirt to location
#     dirt_location = find_nearest_dirt(room, location)
#     print("nearest dirt is", dirt_location)
    
    ### Test the all_clean function
#     print(all_clean(room))
#     
#     (room, location) = move_vacuum(room, location, "R")
#     (room, location) = move_vacuum(room, location, "R")
#     (room, location) = move_vacuum(room, location, "R")
#     (room, location) = move_vacuum(room, location, "R")
#     (room, location) = move_vacuum(room, location, "D")
#     
#     print_room(room)
#     
#     print(all_clean(room))
    
    ### Write a function that cleans an entire room efficiently
    room = clean_the_room(room, location)
    print_room(room)
    
    
def room_distance(location1, location2):
    """Finds the distance between 2 locations in a room.
    Uses Mahattan distance, i.e. distance in rows + distance in columns."""
    
    (row1, col1) = location1
    (row2, col2) = location2
    
    row_difference = abs(row1 - row2)
    col_difference = abs(col1 - col2)
    
    return row_difference + col_difference
    
    
def find_nearest_dirt(room, location):
    """Finds the dirt nearest to location.
    We'll do this by looking at every cell, and find the dirt cell closest
    to the vacuum."""
    
    
    min_distance = 1000000000000000
    closest_location = None
    
    for row_num in range(len(room)):
        for col_num in range(len(room[0])):
            
            if room[row_num][col_num] == "dirt":
                
                ### Find the distance between (row_num, col_num) and vacuum
                distance = room_distance(location, (row_num, col_num))
                if distance < min_distance:
                    min_distance = distance
                    closest_location = (row_num, col_num)
                    
    return closest_location
    
def all_clean(room):
    """Returns True if there is no dirt in the room, and False otherwise."""
    
    return find_element(room, "dirt") == None
    
    
def clean_the_room(room, location):
    """Moves the vacuum "intellegently" until the room is clean."""
    
    while not all_clean(room):
    
        (vacuum_row, vacuum_col) = location
    
        (dirt_row, dirt_col) = find_nearest_dirt(room, location)
        
        ### Move toward closest dirt location
        if vacuum_col < dirt_col:
            (room, location) = move_vacuum(room, location, "R")
            print_room(room)
            input("Moved right")
        elif vacuum_col > dirt_col:
            (room, location) = move_vacuum(room, location, "L")
            print_room(room)
            input("Moved left")  
        elif vacuum_row < dirt_row:
            (room, location) = move_vacuum(room, location, "D")
            print_room(room)
            input("Moved down")   
        elif vacuum_row > dirt_row:
            (room, location) = move_vacuum(room, location, "U")
            print_room(room)
            input("Moved up")            
        
        
    ### Return the cleaned room
    return room




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
    