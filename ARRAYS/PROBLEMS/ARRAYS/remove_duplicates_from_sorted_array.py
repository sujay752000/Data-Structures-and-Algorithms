from typing import List


class Solution:
    def removeDuplicates_Approach1(self, nums: List[int]) -> int:
        ind = 0
        for element in nums:
            if ind == 0 or ind == 1 or nums[ind - 2] != element:
                nums[ind] = element
                ind += 1

        return ind
    

    def removeDuplicates_Approach2(self, nums: List[int]) -> int:
        left = 0
        right = 0

        while right < len(nums):
            count = 1

            while right + 1 < len(nums) and nums[right] == nums[right + 1]:
                count += 1
                right += 1

            for i in range(0, min(2, count)):
                nums[left] = nums[right]
                left += 1

            right += 1

        return left


S = Solution()
nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
# print(S.removeDuplicates(nums))
# print(nums)

print(S.removeDuplicates_Approach2(nums))
print(nums)