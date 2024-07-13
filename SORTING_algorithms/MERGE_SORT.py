def merge(arr, low, mid, high):
    """_summary_ = Merge two Sorted array

    Args:
        arr (list): Array of elements
        low (int): low pointer
        mid (int): mid pointer
        high (int): high pointer
    """
    temp = []
    i = low
    j = mid + 1

    while i <= mid and j <= high:

        if arr[i] < arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1


    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    
    for i in range(0, len(temp)):
        arr[low + i] = temp[i]




def merge_Sort(arr, low, high):
    """_summary_ = is a sorting algorithm that follows the divide-and-conquer approach.
                   It works by recursively dividing the input array into smaller subarrays and sorting those subarrays,
                   then merging them back together to obtain the sorted array.

    Args:
        arr (list): Array of elements
        low (int): low pointer
        high (int): high pointer
    """

    if low < high:
        mid = (low + high) // 2

        merge_Sort(arr, low, mid)
        merge_Sort(arr, mid + 1, high)
        merge(arr, low, mid, high)

lst = [12, 3, 6, 5, 1, 4]
merge_Sort(lst, 0, len(lst) - 1)
print(lst)


"""_summary_ = Time and Space Complexity

    TC = Best =  O(n log n)
         Avg  =  O(n log n)
         Worst = O(n log n) 

    SC = O(n) : temporary array is used to store sorted array and copies those sorted elements back to array

    
    _Additionals_

    In-place = No, its not a in-place alogo, beacuse it  uses additional temporary space to sort array
    Stablity = Yes, it keeps relative oreder of equal elements in array
"""