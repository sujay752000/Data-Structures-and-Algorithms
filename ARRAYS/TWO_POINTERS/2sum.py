def twoSumBrute(arr, k):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == k:
                return (i, j)
        

def twoSumBetter(nums, k):
    hashMap = {}

    for i in range(0, len(nums)):
        rem = k - nums[i]
        if rem in hashMap:
            return [i, hashMap[rem]]
            
        hashMap[nums[i]] = i



nums = [3, 2, 3, 2, 3]
target = 20
print(twoSumBrute(nums, target))
print(twoSumBetter(nums, target))