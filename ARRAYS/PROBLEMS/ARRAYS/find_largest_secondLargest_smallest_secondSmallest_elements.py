def smallestAndLargest(arr):

    largest = secondLargest = float('-inf') # negative infinity
    secondLargest_ind = -1
    Largest_ind = -1

    smallest = secondSmallest = float('inf') # positive infinity
    smallest_ind = -1
    secondSmallest_ind = -1

    for i in range(0, len(arr)):
        if arr[i] > largest: # used to track the largest element, when largest element at last
            secondLargest = largest
            secondLargest_ind = Largest_ind
            largest = arr[i]
            Largest_ind = i

        elif arr[i] > secondLargest and arr[i] < largest: # when the second largest is at last index
            secondLargest = arr[i]
            secondLargest_ind = i

        """ same as the largest and second largest concept except the < sign difference"""
        if arr[i] < smallest:
            secondSmallest = smallest
            secondSmallest_ind = smallest_ind
            smallest = arr[i]
            smallest_ind = i

        elif arr[i] < secondSmallest and arr[i] > smallest:
            secondSmallest = arr[i]
            secondSmallest_ind = i


    result = {'largest' : (largest, Largest_ind),
              'second_largest' : (secondLargest, secondLargest_ind),
              'smallest' : (smallest, smallest_ind),
              'second_smallest' : (secondSmallest, secondSmallest_ind)
               }

    return result


lst = [-232, 10055, 0, 1, 31, -555, 23, 800]

print(smallestAndLargest(lst))

"""_summary_ = Time and Space Complexity

    TC = Best =  O(n)
         Avg  =  O(n)
         Worst = O(n)

    SC = O(1)
"""