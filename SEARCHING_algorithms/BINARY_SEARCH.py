
def binarySearchIterative(arr, key, n)  -> int:
    """ Iterative approach for binary search
        index position of key element will be returned if present
        else return -1 indicates not present

    Args:
        arr (list): List of integers
        key (int): Key element to find
        n (int): Length of the array

    Returns:
        int: index position of key element
    """
    low = 0
    high = n - 1

    while(low <= high):
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1




def binarySearchRecursion(arr, key, low, high):
    """ Recursive Approach to find a key element using binary search
        index position of key element will be returned if present
        else return -1 indicates not present

    Args:
        arr (list): List of integers
        key (int): Key element to find
        low (int): low pointer
        high (int): high pointer

    Returns:
        int: index position of key element
    """
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            return binarySearchRecursion(arr, key, mid + 1, high)
        else:
            return binarySearchRecursion(arr, key, low, mid - 1)




lst = [1, 2, 3, 5, 9, 12, 17, 22]
n = len(lst)
key = int(input("Enter a key element to search : "))

print(binarySearchIterative(lst, key, n))

print(binarySearchRecursion(lst, key, 0, n - 1))


"""_summary_ = Time and Space Complexity

    TC = O(log n)  (log base 2)
        if arr has length n = 32
            32 -> 16 -> 8 -> 4 -> 2 -> 1 = so total 5 steps
            32 = 2^5

            so log 32 = log 2^5
                      = 5 * log 2 (2)
                      = 5 * 1
                      = 5
    SC = O(1)
    
"""