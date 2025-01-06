def upperBoundBinaryIterative(arr, n, key):
    """_summary_ = Iterative approach to find a lower index of an element,
                   which is (arr[mid]) > key

    Args:
        arr (list): List of integers
        n (int): length of array
        key (int): key element or target

    Returns:
        int: lower index of a element which is > key
    """
        
    low = 0
    high = n - 1

    ans = n

    while(low <= high):
        mid = (low + high) // 2

        if arr[mid] > key:
            ans = mid
            high = mid - 1

        else:
            low = mid + 1


    return ans


def upperBoundBinaryRecursion(arr, low, high, key, ans):
    """_summary_ = Recursive approach to find a lower index of an element,
                   which is (arr[mid]) > key

    Args:
        arr (list): List of integers
        low (int): low pointer
        high (int): high pointer
        key (int): key element or target
        ans (int): lower index of a element which is > key

    Returns:
        int: ans = lower index of a element which is > key
    """

    if low > high:
        return ans
    
    else:
        mid = (low + high) // 2

        if arr[mid] > key:
            ans = mid
            return upperBoundBinaryRecursion(arr, low, mid - 1, key, ans)

        else:
            return upperBoundBinaryRecursion(arr, mid + 1, high, key, ans)


lst = [1, 3, 5, 9, 9, 12, 14, 14, 14, 16, 17]
key = int(input("Enter key element to search : "))

print(upperBoundBinaryIterative(lst, len(lst), key))

print(upperBoundBinaryRecursion(lst, 0, len(lst) - 1, key, len(lst)))


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