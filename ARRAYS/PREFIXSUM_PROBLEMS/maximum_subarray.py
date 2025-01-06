def maxSubArraySum(arr, n):
    maxSum = float("-inf")

    for i in range(0, n):
        prefixSum = 0
        for j in range(i, n):
            prefixSum += arr[j]

            maxSum = max(maxSum, prefixSum)

    return maxSum


def maxSubArraySumOptimal_KadaneALgo(arr, n):
    maxSum = float('-inf')
    prefixSum = 0

    start_index = end_index = -1

    for i in range(0, n):
        prefixSum += arr[i]

        if prefixSum > maxSum:
            maxSum = prefixSum
            end_index = i

        if prefixSum < 0:
            prefixSum = 0
            start_index = i + 1

    return maxSum, (start_index, end_index)



lst = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# lst = [1, -2, 3, -3, 1, 1, 1, 4, 2, -8]
# lst = [1]
print(maxSubArraySum(lst, len(lst)))

print(maxSubArraySumOptimal_KadaneALgo(lst, len(lst)))