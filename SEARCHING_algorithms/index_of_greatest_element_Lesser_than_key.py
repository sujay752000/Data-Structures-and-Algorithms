""" HELPS TO GET THE INDEX OF SMALLEST ELEMENT """

def smallestBinarySearch(arr, low, high, key, ans):
    if low > high:
        return ans
    else:
        mid = (low + high) // 2
        if arr[mid] < key:
            ans = mid
            return smallestBinarySearch(arr, mid + 1, high, key, ans) # low = mid + 1
        else:
            return smallestBinarySearch(arr, low, mid - 1, key, ans)  # high = mid - 1
        

lst = [1, 3, 5, 9, 9, 12, 14, 14, 14, 16, 17]
key = int(input("Enter key element to search : "))

print(smallestBinarySearch(lst, 0, len(lst) - 1, key, -1))

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