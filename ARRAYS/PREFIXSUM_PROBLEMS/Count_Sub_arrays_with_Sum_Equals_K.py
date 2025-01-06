def countSubArraysBrute(arr, n, k):
    count = 0
    for i in range(0, n):
        prefixSum = 0
        for j in range(i, n):
            prefixSum += arr[j]

            if prefixSum == k:
                count += 1

    return count



from collections import defaultdict

def countSubArraysOptimal(arr, n, k) -> int:
    count = 0
    hashMap = defaultdict(int) # using defaultdict help to increment prefixSum count easily
    hashMap[0] = 1
    prefixSum = 0

    for i in range(0, n):
        prefixSum += arr[i]

        rem = prefixSum - k
        count += hashMap[rem]

        hashMap[prefixSum] = hashMap[prefixSum] + 1

    return count



lst = [1, 2, 3, -3, 1, 1, 1, 4, 2, -3]
n = len(lst)
k = 3

print("\nBrute Approach - 2 for loops")
print(countSubArraysBrute(lst, n, k))

print("\nOptimal Approach - Hashing")
print(countSubArraysOptimal(lst, n, k))