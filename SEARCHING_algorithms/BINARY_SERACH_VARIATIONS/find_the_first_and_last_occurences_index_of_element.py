def lowerBound(arr, low, high, key, ans):
    if low > high:
        return ans
    else:
        mid = (low + high) // 2
        if arr[mid] >= key:
            ans = mid
            return lowerBound(arr, low, mid - 1, key, ans)
        else:
            return lowerBound(arr, mid + 1, high, key, ans)
        


def upperBound(arr, low, high, key, ans):
    if low > high:
        return ans
    else:
        mid = (low + high) // 2
        if arr[mid] > key:
            ans = mid
            return upperBound(arr, low, mid - 1, key, ans)
        else:
            return upperBound(arr, mid + 1, high, key, ans)
        
        

def startIndexSearch(arr, low, high, key, ans):
    if low > high:
        return ans
    else:
        mid = (low + high) // 2

        if arr[mid] == key:
            ans = mid
            return startIndexSearch(arr, low, mid - 1, key, ans)
        elif arr[mid] < key:
            return startIndexSearch(arr, mid + 1, high, key, ans)
        else:
            return startIndexSearch(arr, low, mid - 1, key, ans)
        

        
def finalIndexSearch(arr, low, high, key, ans):
    if low > high:
        return ans
    else:
        mid = (low + high) // 2

        if arr[mid] == key:
            ans = mid
            return finalIndexSearch(arr, mid + 1, high, key, ans)
        elif arr[mid] < key:
            return finalIndexSearch(arr, mid + 1, high, key, ans)
        else:
            return finalIndexSearch(arr, low, mid - 1, key, ans)




""" Question"""
#input = 6
#output = [3, 5] indexes

#input = 3
#output =[-1, -1]

lst = [1, 1, 5, 6, 6, 6, 7, 8, 9, 10]
key = int(input("Enter key element to search : "))




""" Approach - 1 Apply Lower Bound and check whether its the key --- if it is key then we found Upper Bound - 1 """
print("\n ************************ Approach 1 ************************ \n")

start_ind = lowerBound(lst, 0, len(lst) - 1, key, -1)

if start_ind != -1 and lst[start_ind] == key:
    final_ind = upperBound(lst, start_ind, len(lst) - 1, key, len(lst))
    print([start_ind, final_ind - 1])
else:
    print([-1, -1])

"""_summary_ = Time and Space Complexity

    TC = Lower Bound = O(log n)
         Upper Bound = O(log n)
         Total = O(log n + log n) => O(2 log n) => O(log n)
    SC = O(1)
    
"""





""" Approach - 2 Mofiying the base binary search to find starting index and final index """
print("\n ************************ Approach 2 ************************ \n")

start_ind = startIndexSearch(lst, 0, len(lst) - 1, key, -1)

if lst[start_ind] == key and start_ind != -1:
    final_ind = finalIndexSearch(lst, start_ind, len(lst) - 1, key, -1)
    print([start_ind, final_ind])
else:
    print([-1, -1])

"""_summary_ = Time and Space Complexity

    TC = Start index = O(log n)
         Final index = O(log n)
         Total = O(log n + log n) => O(2 log n) => O(log n)
    SC = O(1)
    
"""
