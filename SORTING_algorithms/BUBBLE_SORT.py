def bubble_Sort(arr, n):
    """_summary_ = sorts the array by pushing the largest bubble element to end at each iterations
                    n - 1 sets of comparisons is need , and its handled by i loop
                        at each i iterations, largest element gets pushed to end
                    and n - 1 - i ajacent element comparisons needed, handled by j loop, (i represents largest element at each iteration sets)

    Args:
        arr (list): Array of elements
        n (int): length of array
    """

    for i in range(0, n - 1):
        swap = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swap = True
        
        if swap == False:
            break
        
        

lst = [12, 3, 6, 5, 1, 4]
# lst = [1, 3, 4, 5, 6, 12]
bubble_Sort(lst, len(lst))
print(lst)


"""_summary_ = Time and Space Complexity

    TC = Best =  O(n), if array is already sorted 
         Avg  =  O(n^2)
         Worst = O(n^2)

    SC = O(1)

    
    _Additionals_

    In-place = Yes, its a in-place alogo, beacuse it doesn't uses additional temporary space to sort array
    Stablity = Yes, it keeps relative oreder of equal elements in array
"""