from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        destination = n - 1
        for i in range(n - 2, -1, -1):
            if nums[i] >= destination - i:
                destination = i

        return destination == 0



S = Solution()
nums = [2, 3, 1, 1, 4]
# nums = [3, 2, 1, 0, 4]
# nums = [3,2,1,0,4]
print(S.canJump(nums))