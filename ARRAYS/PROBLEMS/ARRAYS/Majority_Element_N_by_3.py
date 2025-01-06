from typing import List
from collections import defaultdict

class Solution:
    def majorityElement_Brute(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(0, len(nums)):
            element = nums[i]
            count = 0

            if res and res[0] == element:
                continue

            if len(res) == 2:
                return res

            for j in range(0, len(nums)):
                if element == nums[j]:
                    count += 1

            if count > len(nums) // 3:
                res.append(element)

        return res




    def majorityElement_Better(self, nums: List[int]) -> List[int]:
        counterMap = defaultdict(int)
        minCount = (len(nums) // 3) + 1
        res = []

        for num in nums:
            counterMap[num] += 1

            if counterMap[num] == minCount:
                res.append(num)

            if len(res) == 2:
                return res

        return res


    def majorityElement_Optimal(self, nums: List[int]) -> List[int]:

        minCount = len(nums) // 3

        element_1 = None; count_1 = 0
        element_2 = None; count_2 = 0

        for num in nums:
            if count_1 == 0 and element_2 != num:
                element_1 = num
                count_1 += 1
            elif count_2 == 0 and element_1 != num:
                element_2 = num
                count_2 += 1

            elif num == element_1:
                count_1 += 1
            elif num == element_2:
                count_2 += 1

            else:
                count_1 -= 1
                count_2 -= 1

        count_1 = 0
        count_2 = 0
        for num in nums:
            if num == element_1:
                count_1 += 1

            if num == element_2:
                count_2 += 1

        res = []
        if count_1 > minCount:
            res.append(element_1)
        if count_2 > minCount:
            res.append(element_2)

        return res
    
    def majorityElement_Better(self, nums: List[int]) -> List[int]:
        hashMap = defaultdict(int)
        res = []

        for num in nums:
            hashMap[num] += 1

            if hashMap[num] == (len(num) // 3) + 1:
                res.append(num)

                

        return res

        
    


S = Solution()
nums = [3, 2, 1, 3, 3, 3, 2, 2, 2, 1]
print(S.majorityElement_Brute(nums))
print(S.majorityElement_Better(nums))
print(S.majorityElement_Optimal(nums))