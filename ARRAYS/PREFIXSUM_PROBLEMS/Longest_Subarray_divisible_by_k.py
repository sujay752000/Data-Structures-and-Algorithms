class Solution:

    def longestSubarray_Brute(self, arr, k):
        ans = 0
        for i in range(0, len(arr)):
            prefixSum = 0
            for j in range(i, len(arr)):
                prefixSum += arr[j]

                if prefixSum % k == 0:
                    ans = max(ans, (j - i) + 1)
        return ans
    

    def longestSubarray_Optimal(self, arr, k):
        ans = 0
        hashMap = {0 : -1}
        prefixSum = 0
        for i in range(0, len(arr)):
            prefixSum += arr[i]
            rem = prefixSum % k
            if rem in hashMap:
                ans = max(ans, i - hashMap[rem])

            if rem not in hashMap:
                hashMap[rem] = i
        return ans




arr = [1, 0, -2, -2, -2, 4, 3, 5]
k = 4
S = Solution()
print("\n************** Brute **************")
print(S.longestSubarray_Brute(arr, k))

print("\n************** Optimal **************")
print(S.longestSubarray_Optimal(arr, k))