def partition(arr, low, high) -> int:
    """_summary_ = returns the partition index
                   picks a pivot and places it in correct position

    Args:
        arr (list): Array of elements
        low (int): low pointer
        high (int): high pointer

    Returns:
        int: partition index (jth index)
    """
    pivot = arr[low]
    i = low
    j = high

    while i < j:

        while arr[i] <= pivot and i < high:
            i += 1

        while arr[j] >= pivot and j > low:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    
    arr[low], arr[j] = arr[j], arr[low]

    return j 
        

def quick_Sort(arr, low, high):
    """_summary_ = QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot,
                   and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.

    Args:
        arr (list): Array of elements
        low (int): low pointer
        high (int): high pointer
    """
    if low < high:
        partition_index = partition(arr, low, high)
        quick_Sort(arr, low, partition_index - 1)
        quick_Sort(arr, partition_index + 1, high)


lst = [12, 3, 6, 5, 1, 4]
quick_Sort(lst, 0, len(lst) - 1)
print(lst)


"""_summary_ = Time and Space Complexity

    TC = Best =  O(n log n)
         Avg  =  O(n log n)
         Worst = O(n^2) : When a sorted array is provided

    SC = O(1), O(n) : on considering function call stack space

    
    _Additionals_

    In-place = Yes, its a in-place alogo, beacuse it doesn't uses additional temporary space to sort array
    Stablity = No, it doesn't keeps relative order of equal elements in array,
               because we do swapping of elements according to pivot's position (without considering their original positions

"""
