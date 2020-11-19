import random
import time

def main():

    short = [8,4,3,7,2,1,6,5]
    long = list(range(10000))
    random.shuffle(long)
    
    print("Original:", long[:10])


    ### Sort short list
#     selection_sort(short)

    ### Sort long list
    start_time = time.time()
    
    selection_sort(long)

    ### Test out built-in sorting
#     long.sort()
    
    end_time = time.time()
    
    print("Sorted long list:", long[:10])
    total_time = end_time - start_time
    print("Sorting took", total_time, "seconds.")
    
    
    
def swap(lst, i, j):
    """Swaps the elements at indices i and j in lst"""
    temp = lst[j]
    lst[j] = lst[i]
    lst[i] = temp
    
    
def selection_sort(lst):
    """Sorts a list by finding the next smallest element.
    No need to return, since we're changing the actual object."""
    
    ## Consider every index in the list
    for i in range(len(lst)):
        
        ## Find the smallest element starting at index i
        smallest_index = i
        for j in range(i, len(lst)):
            
            if lst[j] < lst[smallest_index]:
                smallest_index = j
                
        swap(lst, i, smallest_index)
            
#         print(lst)
#         input("Hit enter to continiue. We're at index" + str(i))
#         print()
    



    
if __name__ == "__main__":
    main()
