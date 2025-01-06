from typing import List

class Solution:
    def maxProduct_Brute(self, nums: List[int]) -> int:
        ans = 0
        for i in range(0, len(nums)):
            prod = 1
            for j in range(i, len(nums)):
                prod *= nums[j]
                if ans < prod:
                    print(nums[i : j + 1])
                    ans = prod

        print(ans)


    def maxProduct_Optimal(self, nums: List[int]) -> int:

        left_product = 1
        right_product = 1
        n = len(nums)
        max_prod = float("-inf")


        for i in range(0, n):

            left_product *= nums[i]
            right_product *= nums[n - 1 - i]

            max_prod = max(max_prod, left_product, right_product)

            if left_product == 0:
                left_product = 1

            if right_product == 0:
                right_product = 1

        return max_prod


            





    


S = Solution()
nums = [3, 2, 0, -1, 4, 0, -6, 3, -2, 6]
S.maxProduct_Brute(nums)
print(S.maxProduct_Optimal(nums))

