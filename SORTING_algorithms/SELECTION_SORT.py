def selection_Sort(arr, n):
    """_summary_ = sorting algorithm that works by repeatedly selecting the smallest (or largest) element from the unsorted portion of the list
                   and moving it to the sorted portion of the list. 

    Args:
        arr (list): Array of elements
        n (int): length of array
    """

    for i in range(0, n - 1):
        mini = i
        for j in range(i, n):
            if arr[mini] > arr[j]:
                mini = j

        arr[i], arr[mini] = arr[mini], arr[i]



lst = [12, 3, 6, 5, 1, 4]
selection_Sort(lst, len(lst))
print(lst)

"""_summary_ = Time and Space Complexity

    TC = Best =  O(n^2)
         Avg  =  O(n^2)
         Worst = O(n^2)

    SC = O(1)

    
    _Additionals_

    In-place = Yes, its a in-place alogo, beacuse it doesn't uses additional temporary space to sort array
    Stablity = No, it doesn't keeps relative oreder of equal elements in array
"""