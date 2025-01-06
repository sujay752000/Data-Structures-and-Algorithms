from collections import defaultdict

class Solution:
    def subArrayDivisibleCount_Brute(self, arr, k):
        count = 0
        for i in range(0, len(arr)):
            preSum = 0
            for j in range(i, len(arr)):
                preSum += arr[j]
                if preSum % k == 0:
                    count += 1
                    print(arr[i : j + 1])

        return count

    
    def subArrayDivisibleCount_Optimal(self, arr, k):
        count = 0
        hashMap = defaultdict(int)
        hashMap[0] = 1
        prefixSum = 0

        for num in arr:
            prefixSum += num
            remainder = prefixSum % k
            count += hashMap[remainder]
            hashMap[remainder] += 1

        return count



arr = [1, 0, -2, -2, -2, 4, 3, 5]
k = 4
S = Solution()
print("\n************** Brute **************")
print(S.subArrayDivisibleCount_Brute(arr, k))

print("\n************** Optimal  **************")
print(S.subArrayDivisibleCount_Optimal(arr, k))