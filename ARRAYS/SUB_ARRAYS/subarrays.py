def subArrays(arr, n):
    """_summary_ = A subarray is a contiguous part of the array. An array that is inside another array
                   In general, for an array/string of size n, there are  n*(n+1) / 2  non-empty subarrays/substrings.

    Args:
        arr (_type_): Array of elements
        n (_type_): Size of array
    """

    for i in range(0, n): # starting index
        print("\n")

        for j in range(i, n): # Ending index
            print("\n")

            for k in range(i, j + 1): # printing sub arrays between range starting i and ending j, including (i, j)
                print(f"{arr[k]}, ", end="")

    """_summary_ = Time and Space Complexity

            TC = Best  = O(n^3) 
                 Avg   = O(n^3) 
                 Worst = O(n^3) 

            SC = O(1) 
    """



def subArraysSum(arr, n):
    totalSubArray = 0       # also same as n*(n + 1) / 2
    totalSubArraySum = 0    # we can find each subarray's sum and can add it which formulates total sub arrays sum
    for i in range(0, n):

    # If the question demands only sub arrays sum we can go for prefixsum ...
        prefixSubArraySum = 0   # prefixsum is a better approach so that it takes only O(n^2) to find sub arrays sum
        for j in range(i, n):
            subArraySum = 0     # another way of finding subarray sum.. it uses one extra loop.. so Total TC = O(n^3)
            totalSubArray += 1
            prefixSubArraySum += arr[j]

            for k in range(i, j + 1):   # if we want to print all sub arrays we need this extra loop
                subArraySum += arr[k]
                print(f"{arr[k]}, ", end="")

            print(f"\t==> Sub array {i,'->',j} index with length {(j - i) + 1},  sum ==> {prefixSubArraySum}\t{subArraySum}") 
            # just showing both prefixSubArraySum and subArraySum are same

        totalSubArraySum += prefixSubArraySum   # totalSubArraySum = addition of all sub arrays sum

    
    print(f"\nTotal Sub arrays ==> {totalSubArray}")
    print(f"Total sum of Sub arrays sum ==> {totalSubArraySum}")



lst = [1, 2, 3, 4]

print("\n============== Sub arrays ==============\n")
subArrays(lst, len(lst))

print("\n\n============== Sum of Sub arrays ==============\n")
subArraysSum(lst, len(lst))
