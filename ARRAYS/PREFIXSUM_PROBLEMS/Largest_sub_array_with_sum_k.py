def lengthSubArraySumBetter(arr, n, k):
    hashMap = {}
    prefixSum = 0
    ans = 0

    for i in range(0, n):
        prefixSum += arr[i]

        if prefixSum == k:
            ans = max(ans, i + 1)
        else:
            rem = prefixSum - k

            if rem in hashMap:
                resInd = hashMap[rem]
                ans = max(ans, i - resInd)

        if prefixSum not in hashMap:
            hashMap[prefixSum] = i

    return ans
        


def lengthSubArraySumBrute(arr, n, k):

    ans = 0
    for i in range(0, n):
        prefixSum = 0

        for j in range(i, n):
            prefixSum += arr[j]

            if prefixSum == k:
                ans = max(ans, (j - i) + 1)

            elif prefixSum > k:
                break # if prefixSum is greater than k then no need to go for adding sums


    return ans



def lengthSubArraySumOptimal(arr, n, k):
    # Omly works with positives ans zeros
    left = right = 0
    prefixSum = 0
    ans = 0

    while right < n:
        prefixSum += arr[right]

        while prefixSum > k and left <= right:
            prefixSum -= arr[left]
            left += 1

        if prefixSum == k:
            ans = max(ans, (right - left) + 1)

        right += 1

    return ans



# lst = [-1, -2, 3, 2, 1, 1, -2, 1, 1, 2, 3]
lst = [1, 2, 3, 1, 1, 1, 1, 3, 4, 5]
print("Brute Approach - 2 for loop")
print(lengthSubArraySumBrute(lst, len(lst), 4))

print("\nBetter Approach - HashMap Approach")
print(lengthSubArraySumBetter(lst, len(lst), 4))

print("\nOptimal Approach - 2 pointer Approach")
print(lengthSubArraySumOptimal(lst, len(lst), 4))
