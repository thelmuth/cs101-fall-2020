
def main():

#     numbers = [[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9],
#                [10, 11, 12],
#                [13, 14, 15]]

#     numbers = [[-1, -2.02, 3],
#                [4, 5, 6],
#                [7.03, 8, 9.01],
#                [10, 11, 12],
#                [13, -14, -15]]

#     numbers = [[1, 2, 3, 4, 5, 6, 7]]

#     numbers = [[1],
#                [2],
#                [3],
#                [4]]

#     numbers = [[],
#                [],
#                []]

    numbers = []

    strings = [["a", "b", "c"],
               ["d", "e", "f"]]

#     sum_of_grid = sum_grid(numbers)
#     print(sum_of_grid)

#     print(sum_grid(strings))


    div_by_3 = indices_of_all_numbers_divisible_by_3(numbers)
    print(div_by_3)

def sum_grid(grid):
    """Calculates the sum of all of the numbers in the grid."""

    total = 0

#     total = ""
    for row in grid:
        for element in row:
            total += element


#             print(element)
#
#         print("------")

    return total


def indices_of_all_numbers_divisible_by_3(grid):
    """List of all indices in the grid whose elements are divisible by 3"""

    if grid == []:
        print("The number of rows in the grid is", 0)
        print("The number of columns in the grid is", 0)
        return []

    print("The number of rows in the grid is", len(grid))
    print("The number of columns in the grid is", len(grid[0]))

    div_by_3 = []
    for row_number in range(len(grid)):
        for col_number in range(len(grid[0])):
            element = grid[row_number][col_number]
            if element % 3 == 0:
                div_by_3.append((row_number, col_number))

#             print(row_number, col_number)
#
#         print("-----")

    return div_by_3


if __name__ == "__main__":
    main()
    
