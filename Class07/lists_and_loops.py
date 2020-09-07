
def main():
    
    # List methods
    
    numbers = [15, 30, 45, 60]
    
    numbers[1] = -15
    
    print("1.", numbers)
    
    numbers.append(75) # This adds 75 to the end of numbers
    
    print("2.", numbers)
    
    numbers.extend([90, 7, 32]) # This adds elements to the end of list
    
    # numbers.extend(45) # Don't do this, error because arg needs to be a list
    
    primes = [2, 3, 5, 7, 11]
    
    numbers.extend(primes)
    
    print("3.", numbers)
    
    # takes an index and the element you want to insert at that index
    numbers.insert(3, 20)
    
    print("4.", numbers)
    
    # pop: removes an element at a specific index
    numbers.pop(2)
    
    print("5.", numbers)
    
    # this will sort your list:
    numbers.sort()
    
    print("6.", numbers)
    
    names = ["Tammy", "bruce", "Tom", "Elroy", "Amy"]
    
    names.sort()
    
    print(names)
    
    nested = [[3], [4, 5], [6, 3, 1], [1, -4], [4, 1, 2]]
    
    nested.sort()
    
    print(nested)
    
#     stuff = [4, "hi", "yay", 1]
#     
#     stuff.sort()
#     
#     print(stuff)
    
    numbers.reverse()
    
    print(numbers)
    
    nums_and_names = numbers + names
    
    print("N+N.", nums_and_names)
    
    print("Length of N+N:", len(nums_and_names))
    
    #####
    x = [1, 2, 3]
    y = x
    y[0] = 500
    
    print("y = ", y)
    print("x = ", x)
    
    # This is an effect called "list aliasing"
    
    
    
    
main()