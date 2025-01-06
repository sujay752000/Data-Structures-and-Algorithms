class Solution:


    def maxLen_Optimal(self, arr):
        # code here
        res = 0
        prefixSum = 0
        hashMap = {0 : -1}
        for i in range(0, len(arr)):
            prefixSum += arr[i]

            if prefixSum in hashMap:
                res = max(res, i - hashMap[prefixSum])
            else:
                hashMap[prefixSum] = i

        return res
    

    def maxLen_Brute(self, arr):
        
        for i in range(0, len(arr)):
            prefixSum = 0
            for j in range(i, len(arr)):
                prefixSum += arr[j]

                if prefixSum == 0:
                    print(arr[i : j + 1])




S = Solution()
# arr = [-21, 6, 7, 22, 22, -29, 27, -42]
arr = [2, 3, 1, -2, -2]

print(S.maxLen_Optimal(arr))
S.maxLen_Brute(arr)