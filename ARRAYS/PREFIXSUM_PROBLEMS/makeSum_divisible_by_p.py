from typing import List

class Solution:

    def minSubarray_Brute(self, nums: List[int], p: int) -> int:
        target_Remainder = sum(nums) % p

        if target_Remainder == 0:
            return 0

        ans = len(nums)
        for i in range(0, len(nums)):
            prefixSum = 0
            for j in range(i, len(nums)):
                prefixSum += nums[j]

                if prefixSum % p == target_Remainder:
                    print(nums[i : j + 1])
                    ans = min(ans, (j - i) + 1)


        return -1 if ans == len(nums) else ans
    


    def minSubarray_Optimal(self, nums: List[int], p: int) -> int:

        target_Remainder = 0
        for num in nums:
            target_Remainder = (target_Remainder + num) % p


        if target_Remainder == 0:
            return 0
        
        ans = len(nums)
        hashMap = {0 : -1}
        prefixSum = 0
        for i in range(0, len(nums)):
            prefixSum += nums[i]
            current_Remainder = prefixSum % p

            previous_Remainder = (current_Remainder - target_Remainder) % p
            if previous_Remainder in hashMap:
                ans = min(ans, i - hashMap[previous_Remainder])

            hashMap[current_Remainder] = i

        return -1 if ans == len(nums) else ans
    

    def minSubarray_Further_Optimization(self, nums: List[int], p: int) -> int:
        Target_Remainder = 0
        for num in nums:
            Target_Remainder = (Target_Remainder + num) % p

        if Target_Remainder == 0:
            return 0
        
        ans = len(nums)
        hashMap = {0 : -1}
        current_Remainder = 0
        for i in range(0, len(nums)):
            current_Remainder = (current_Remainder + nums[i]) % p

            previous_Remainder = (current_Remainder - Target_Remainder) % p
            if previous_Remainder in hashMap:
                ans = min(ans, i - hashMap[previous_Remainder])

            hashMap[current_Remainder] = i

        return -1 if ans == len(nums) else ans



        




S = Solution()
# nums = [26,19,11,14,18,4,7,1,30,23,19,8,10,6,26,3]; p = 26
# nums = [6, 3, 5, 2]; p = 9
# nums = [1, 2, 3]; p = 7
# nums = [3,1,4,2]; p = 6
nums = [1, 3, 5, 3, 2, 2]; p = 6
# print(S.minSubarray_Brute(nums, p))
# print(S.minSubarray_Optimal(nums, p))
print(S.minSubarray_Further_Optimization(nums, p))